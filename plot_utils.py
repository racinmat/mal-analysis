# now try the histogram equalization on colormap to better show data
# histogram equalization taken from https://github.com/jobar8/graphics/blob/master/graphics.py and modified little bit
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from skimage import exposure


def cmap_to_array(cmap, N=256):
    """
    Return a Nx3 array of RGB values generated from a colormap.
    """
    return cmap(np.linspace(0, 1, N))[:, :3]  # remove alpha column


def equalize_colormap_base(cmap, data):
    if isinstance(data, (pd.DataFrame, pd.Series)):
        data = data.values
    data = data[~np.isnan(data)].flatten()
    assert np.issubdtype(data.dtype, np.floating), 'Data must be floating, otherwise it does not work'

    cdf, bins = exposure.cumulative_distribution(data, nbins=256)
    # Using it for highly non-uniform data will cause high information loss for extreme values
    # So we do only half equalization, equalizing with histogram averaged with uniform histogram
    # and now the same for uniform distribution of same size
    cdf_u, bins_u = exposure.cumulative_distribution(np.linspace(data.min(), data.max(), data.shape[0]), nbins=256)
    cdf = (cdf + cdf_u) / 2
    '''
    Re-map a colormap according to a cumulative distribution. This is used to 
    perform histogram equalization of an image by changing the colormap 
    instead of the image. *This is not strickly speaking the equalization of the 
    colormap itself*.
    The cdf and bins should be calculated from an input image, as if carrying out
    the histogram equalization of that image. In effect, the cdf becomes integrated  
    to the colormap as a mapping function by redistributing the indices of the
    input colormap.

    Parameters
    ----------
    cmap : string or colormap object
        Input colormap to remap.
    bins : array
        Centers of bins.
    cdf : array
        Values of cumulative distribution function.
    '''

    # first retrieve the color table (lists of RGB values) behind the input colormap
    if cmap in mpl.cm.cmap_d:  # matplotlib colormaps + plus the new ones (viridis, inferno, etc.)
        cmList = cmap_to_array(plt.cm.cmap_d[cmap])
    else:
        try:
            # in case cmap is a colormap object
            cmList = cmap_to_array(cmap)
        except:
            raise ValueError('Colormap {} has not been recognised'.format(cmap))

    # normalize the input bins to interval (0,1)
    bins_norm = (bins - bins.min()) / np.float(bins.max() - bins.min())

    # calculate new indices by applying the cdf as a function on the old indices
    # which are initially regularly spaced.
    old_indices = np.linspace(0, 1, len(cmList))
    new_indices = np.interp(old_indices, cdf, bins_norm)

    # make sure indices start with 0 and end with 1
    new_indices[0] = 0.0
    new_indices[-1] = 1.0

    return new_indices, cmList


def equalize_colormap_plotly(cmap, data):
    new_indices, cmList = equalize_colormap_base(cmap, data)

    carr = []
    for i, n in enumerate(new_indices):
        r, g, b = (cmList[i] * 256).astype(int)
        rgb_str = f'rgb({r}, {g}, {b})'
        carr.append([n, rgb_str])

    return carr


def equalize_colormap(cmap, data, name='EqualizedMap'):
    new_indices, cmList = equalize_colormap_base(cmap, data)
    # remap the color table
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, n in enumerate(new_indices):
        r1, g1, b1 = cmList[i]
        cdict['red'].append([n, r1, r1])
        cdict['green'].append([n, g1, g1])
        cdict['blue'].append([n, b1, b1])

    return mpl.colors.LinearSegmentedColormap(name, cdict)


if __name__ == '__main__':
    data = np.array([
        5, 24, 41, 6, 206, 874, 10, 1, 2707, 381, 44, 778, 2, 7, 301, 747, 117, 69, 87, 151, 8, 12, 41, 6513, 5, 35, 13,
        14, 1, 4752, 245, 525, 264, 4, 37, 10, 1, 324, 3, 106, 17, 3, 36, 429, 2948, 1, 3, 608, 56, 86, 59, 237, 1713,
        317, 1, 1179, 6, 2522, 11, 12, 5459, 119, 16, 6, 4, 1, 660, 4, 11, 53, 3, 21, 453, 37, 862, 2265, 5, 1003, 352,
        101, 72, 65, 508, 1562, 55, 11, 52, 1132, 79, 40, 3, 8, 1, 1, 134, 119, 12, 38, 48, 29, 3, 4, 46, 10, 648, 37,
        314, 113, 2, 56, 4, 15, 892, 1, 34, 5, 59, 48, 18, 59, 5, 1, 1, 36, 3, 895, 2, 44, 13, 2571, 1207, 58, 574, 24,
        180, 106, 1, 174, 3136, 6, 6097, 5, 1945, 24, 15, 58, 1175, 3149, 1, 482, 20, 772, 1, 4, 29, 1, 2, 386, 1, 6,
        324, 138, 1681, 1, 9, 40, 1, 10, 270, 1, 4, 1, 56, 96, 963, 73, 14, 7, 582, 103, 23801, 8, 1, 2, 264, 2, 230, 1,
        1, 7, 326, 2, 8]).astype(np.float64)
    equalize_colormap(plt.cm.jet, data, name='EqualizedMap')
