# import glob
# from PIL import Image as PIL_Image
# from images2gif import writeGif
#
# gif_filename = 'studios-genres-MDS'
# images = [PIL_Image.open(image) for image in glob.glob('images/'+gif_filename+'/*.png')]
# file_path_name = 'images/' + gif_filename + '.gif'
# writeGif(file_path_name, images, duration=0.2)
import pickle
from itertools import product
import pandas as pd
import numpy as np

with open('tree_clf.rick', 'rb') as f:
    clf, completed_columns, target_names = pickle.load(f)


def tree_to_table(clf, target_column):
    def expand_node(curr_node, prefix):
        # three is balanced
        thr_percent = "{0:.1%}".format(threshold[curr_node])
        fname = fnames[feature[curr_node]]
        if children_left[curr_node] == -1 and children_right[curr_node] == -1:
            return [prefix], [targets[curr_node]], [value[curr_node, 0, :]]
        l_res, l_target, l_distr = expand_node(children_left[curr_node], prefix + [fname + ' <= ' + thr_percent])
        r_res, r_target, r_distr = expand_node(children_right[curr_node], prefix + [fname + ' > ' + thr_percent])
        return l_res + r_res, l_target + r_target, l_distr + r_distr

    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    feature = clf.tree_.feature
    threshold = clf.tree_.threshold
    value = clf.tree_.value

    fnames = [i.replace('completed_', '') for i in completed_columns]
    targets = [target_names[np.argmax(v)] for v in value]
    paths, classes, distr = expand_node(0, [])
    distr = np.array(distr)
    indices = pd.MultiIndex.from_tuples(paths)
    df = pd.DataFrame({target_column: classes, 'probability': (distr.max(axis=1) / distr.sum(axis=1))},
                      index=indices)
    df['probability'] = df['probability'].apply(lambda x: "{0:.2f}%".format(x * 100))
    return df


def tree_to_table_old(clf, target_column):
    n_nodes = clf.tree_.node_count
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    feature = clf.tree_.feature
    threshold = clf.tree_.threshold
    value = clf.tree_.value
    max_depth = clf.tree_.max_depth

    fnames = [i.replace('completed_', '') for i in completed_columns]

    res = []
    for i in range(max_depth + 1):
        res += list(product(range(2), repeat=i))
    res.sort()
    # display(res)

    targets = [target_names[np.argmax(v)] for v in value]

    levels = [[] for i in range(max_depth + 1)]
    level_paths = [[] for i in range(max_depth + 1)]
    classes = [[] for i in range(max_depth + 1)]
    values = [[] for i in range(max_depth + 1)]
    for i, path in enumerate(res):
        # print(i, len(path), feature[i], fnames[feature[i]])
        thr_percent = "{0:.1%}".format(threshold[i])
        levels[len(path)].append([fnames[feature[i]] + ' <= ' + thr_percent, fnames[feature[i]] + ' > ' + thr_percent])
        level_paths[len(path)].append([levels[len(path)][-1][-2]])
        level_paths[len(path)].append([levels[len(path)][-1][-1]])
        classes[len(path)].append(targets[i])
        values[len(path)].append(value[i])
        # print(level_paths[len(path)][-2], level_paths[len(path)][-1])
        # print(len(level_paths[len(path)]), 2 ** len(path))
        if len(path) > 0:
            prev_paths = level_paths[len(path) - 1]
            if len(level_paths[len(path)]) <= 2 ** len(path):
                # print('<')
                parent = prev_paths[-2]
            else:
                # print('>')
                parent = prev_paths[-1]
            level_paths[len(path)][-2] = parent + level_paths[len(path)][-2]
            level_paths[len(path)][-1] = parent + level_paths[len(path)][-1]
            # print(level_paths[len(path)][-2], level_paths[len(path)][-1])
    # levels = levels[:-1]
    paths = level_paths[-2]
    indices = pd.MultiIndex.from_tuples(paths)
    distr = np.array(values[-1])
    df = pd.DataFrame({target_column: classes[-1], 'probability': (distr.max(axis=2) / distr.sum(axis=2))[:, 0]},
                      index=indices)
    df['probability'] = df['probability'].apply(lambda x: "{0:.2f}%".format(x * 100))
    return df


print(tree_to_table_old(clf, 'gender'))
print(tree_to_table(clf, 'gender'))
