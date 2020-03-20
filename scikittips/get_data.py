import pandas as pd


def get_all_data():

    column_headers = ['cp', 'im', 'pp', 'imU', 'om', 'omL', 'imL', 'imS']

    df = pd.read_csv(
        'https://raw.githubusercontent.com/jbrownlee/Datasets/master/ecoli.csv', names=column_headers)
    return df
