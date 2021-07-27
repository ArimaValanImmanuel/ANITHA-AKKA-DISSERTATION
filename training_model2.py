import h5py
import numpy as np
import os, sys, shutil
from PIL import Image
from pathlib import Path
import h5py
from Imageprocessor import imgprcwithpath
import csv

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES']='0,1'



def train_file(path, categ):

    return(imgprcwithpath(path + ".jpg", categ))

def train_directory(path, r):

    categories = []*0
    
    DIR = path

    files = os.listdir(path)

    for fil in files:

        fullPath = os.path.join(path, fil)

        if os.path.isdir(fullPath):

            name = Path(fullPath).stem

            categories.append(name)
                
            for f in os.listdir(fullPath):

                ff = f.split('.')
                
                passPath = fullPath +"\\" + ff[0]

                s = train_file(passPath, name)

                #lab = ff[0].split("_")
                
                #listlab = os.listdir(fullPath)

                data_p = np.concatenate((s, np.broadcast_to(np.array([int(categories.index(name))]) [:, None, None], s.shape[:-1] + (1,))), axis = -1)
                                
                if name in (list(r.keys())):
                    
                    dataset_name = Path(passPath).stem

                    r[name].create_dataset(dataset_name, data = data_p)

def train_model():

    DIR = "D:\\AnithaAkkaDS\\archive\\"

    DIRS = ["Train\\", "Test\\"]

    for j in DIRS:

        Full_path = os.path.join(DIR,j)

        h5 = h5py.File('{}_data.h5'.format(Path(Full_path).stem), 'w')

        for i in os.listdir(Full_path):

            h5.create_group(i)

        train_directory(Full_path, h5)

        print("TRAINING AND TESTING DATASETS CREATED")

if __name__ == "__main__":

    sys.exit(0)
