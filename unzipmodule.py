# mymodule.py 
import zipfile
import os
import h5py
from functools import reduce
import numpy as np
from scipy.io import loadmat
import pandas as pd #libreria pandas para hacer los dataframe

def unzip_1(paths, name):
    os.chdir(paths)
    with zipfile.ZipFile(name, 'r') as zip_ref:
        zip_ref.extractall(paths)

def zip_a(directory, output_file):
    h5_file = h5py.File(output_file, 'w')
    h5_file.close()

    for filename in os.listdir(directory):
        if filename.endswith('.mat'):
            file_path = os.path.join(directory, filename)
            key = os.path.splitext(filename)[0]
            annots = loadmat(file_path)

            indices_vibration = [0, 0, 1, 0, 0, 0]
            indices_started_time = [0, 0, 0, 0, 0, 0, 0, 0]
            indices_increment = [0, 0, 0, 0, 0, 1, 0, 0]
            indices_number_of_samples = [0, 0, 0, 0, 0, 2, 0, 0]

            vibration = reduce(lambda x, i: x[i], indices_vibration, annots['Signal'])
            started_time = reduce(lambda x, i: x[i], indices_started_time, annots['Signal'])
            increment_time = reduce(lambda x, i: x[i], indices_increment, annots['Signal'])
            number_of_samples = reduce(lambda x, i: x[i], indices_number_of_samples, annots['Signal'])
            final_value = started_time + (increment_time * (number_of_samples - 1))
            time = np.linspace(started_time, final_value, number_of_samples, endpoint=True)
            all_data = np.concatenate((vibration, time.reshape(vibration.shape[0], 1)), axis=1)

            with h5py.File(output_file, 'a') as h5_file:
                h5_file.create_dataset(key, data=all_data)

        elif filename.endswith('.csv') and 'vibration' in filename.lower():
            key = os.path.splitext(filename)[0]
            csv_path = os.path.join(directory, filename)
            df = pd.read_csv(csv_path)
            data = df.values

            with h5py.File(output_file, 'a') as h5_file:
                h5_file.create_dataset(key, data=data)
def delete_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)






    
    
    