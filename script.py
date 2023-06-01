import pandas as pd
import numpy as np
import argparse
import os

def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description='data generator code')
    parser.add_argument('ppg_path', help='Path to the input ppg_directory.')
    parser.add_argument('path1', help='Path to the input path1 directory.')
    parser.add_argument('outputDirectory', help='Path to the output that contains generated data')
    return parser


def load_data(parsed_args):
    path1=parsed_args.path1
    ppg_path=parsed_args.ppg_path
    data1=pd.read_csv(path1)
    data1=data1.iloc[data1.iloc[:,1].isnull().sum():,:]
    data2=pd.read_csv(ppg_path)
    return data1, data2
 

def base_stamps(data2):
    indices=[]
    for row in range(1,data2.shape[0]):
        if data2.iat[row,0][:16]!=data2.iat[row-1,0][:16]:
            indices.append(row)
    return indices


def final_stamps(indices, data1, data2):
    final_index=[]
    glucose_values=[]
    for index in indices:
        for j in range(data1.shape[0]):
            if data2.iat[index,0][:16]==data1.iat[j,1][:16]:
                final_index.append(index)
                glucose_values.append(data1.iat[j,7])
    return final_index, glucose_values


def make_dataframe(final_index, data2, glucose_values):
    table=[]
    for index in final_index:
        table.append(data2.iloc[index-64*30:index+64*30,1])  
    table=np.array(table)
    df=pd.DataFrame(table)
    df['glucose_value']=glucose_values
    return df


def save_data(parsed_args,df):
    output=parsed_args.outputDirectory
    df.to_csv(output)


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args()
    if os.path.exists(parsed_args.ppg_path):
        print("Paths verified sucessfully!")
    #load data:
    data1, data2 = load_data(parsed_args)
    print("data loaded sucessfully")
    print("collecting base stamps")
    indices = base_stamps(data2)
    print("base stamps collected")
    print("collecting final stamps")
    final_index, glucose_values = final_stamps(indices, data1, data2)
    df=make_dataframe(final_index, data2, glucose_values)
    print(f'data points extracted successfully= {df.shape[0]}')
    save_data(parsed_args,df)
    print("Generated data was saved sucessfully at the location provided")
