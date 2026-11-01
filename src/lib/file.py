import pandas as pd
from tabulate import tabulate

def create(name, price, volume, file_name):
    
    df = pd.DataFrame([{
        'Nama' : name,
        'Harga' : price,
        'Volume' : volume,
        'Total' : price*volume,
    }])

    df.to_csv(file_name, index=False, mode='a', header=False)

def read(file_name):
    df = pd.read_csv(file_name)
    print((tabulate(df, headers='keys', tablefmt='grid')))

def update(name, price, volume, file_name, name_update):
    df = pd.read_csv(file_name)
    temp = []

    for _, row in df.iterrows():
        if row['Nama'] == name_update:
            row['Nama'] = name
            row['Harga'] = price
            row['Volume'] = volume
            row['Total'] = price*volume
        temp.append(row.to_dict())

    df_new = pd.DataFrame(temp, columns=df.columns)
    df_new.to_csv(file_name, index=False)


def delete(file_name, name_delete):
    df = pd.read_csv(file_name)
    df = df[df['Nama'] != name_delete]
    df.to_csv(file_name, index=False)











    