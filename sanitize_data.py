import pandas as pd

def load_data():
    with open('data/doh_inspections.csv', 'r') as f:
        data = pd.read_csv(f, quotechar='"')
    return data


