import pandas as pd
import re

def load_data():
    with open('data/doh_inspections.csv', 'r') as f:
        data = pd.read_csv(f, quotechar='"')
    data = data[~data['INSPECTION DATE'].isin(['01/01/1900'])]
    return data

def make_violation_dict(data):
    return dict(zip(data['VIOLATION CODE'], data['VIOLATION DESCRIPTION']))

def unique_firsts(l):
    le_list = [a[0] for a in set(l)]
    for x in set(le_list):
        le_list.remove(x)
    return set(le_list)

data = load_data()
violation_dict = make_violation_dict(data)
