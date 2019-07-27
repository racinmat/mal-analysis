import os
import os.path as osp
import pandas as pd
from pandas.io.common import _NA_VALUES


def get_users_for_episode_count_ban(animelists: pd.DataFrame) -> pd.Series:
    users_for_ban = animelists[animelists['my_watched_episodes'] == 65535]['username'].unique()
    return users_for_ban


def get_users_for_episode_count_ban_cached():
    cache_name = 'cache_users-to-ban.csv'
    if osp.isfile(cache_name):
        users_for_ban = pd.read_csv(cache_name, encoding='utf-8')
        return users_for_ban

    print('cache not found, loading and calculating, may take quite long')
    na_values = _NA_VALUES - {'NULL', 'null', 'nan', 'NaN'}
    animelists = pd.read_csv('animelists_filtered.csv', na_values=na_values, keep_default_na=False)
    users_for_ban = get_users_for_episode_count_ban(animelists)
    users_for_ban.to_csv(cache_name, index=False, sep=',', encoding='utf-8')
    return users_for_ban

