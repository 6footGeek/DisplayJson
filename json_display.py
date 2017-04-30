import json
import pandas as pd

def setup_terminal():
    pd.set_option('display.height', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.max_colwidth', 80)

def display_table():
    getJSON = pd.read_json('pwned.json', orient='index')
    table = pd.DataFrame(getJSON).T
    table = table[['Domain', 'BreachDate', 'PwnCount', 'Description']]
    table.set_index('Domain', inplace=True)
    print table

def main():
    setup_terminal()
    display_table()

main()
