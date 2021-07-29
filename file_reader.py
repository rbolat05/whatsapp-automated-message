from pandas import read_excel, read_csv

def reader(filetype):
    if filetype == 'csv':
        pass
    if filetype == 'excel':
        df = read_excel('phones_list.xlsx', header=None)
        df.columns = ['phones']
        phones_list = df['phones'].to_list()

    if filetype == 'txt':
        phones_list = [line.rstrip('\n') for line in open('phones_list.txt')]

    return phones_list