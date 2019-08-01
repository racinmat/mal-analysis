import json
import pandas as pd

if __name__ == '__main__':
    with open('anime-all-dump-json.txt', 'r') as data_file:
        json_data = data_file.readlines()

    data = []
    for anime_json in json_data:
        anime_row = json.loads(anime_json)
        data.append(anime_row)

    df = pd.DataFrame(data)
    print('done')
    df.to_csv('all_anime_new.csv', index=False, sep=',', encoding='utf-8')