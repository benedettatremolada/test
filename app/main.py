import os
import numpy as np
import argparse
import json
import sys
import time
import datetime
import math
import matplotlib.pyplot as plt
# DAQ libraries
from hdf5libs import HDF5RawDataFile
import detdataformats
import fddetdataformats
from rawdatautils.unpack.wibeth import *
from rawdatautils.utilities.wibeth import *
import rawdatautils.utilities 
import detchannelmaps
sys.path.append('../python/') 
from plotter_libs import *


parser = argparse.ArgumentParser(description='Tranforms Trigger Primitives to images.')
parser.add_argument('--input_json', type=str, help='Input json file')
args = parser.parse_args()
input_json_file = args.input_json

# Read input json
with open(input_json_file) as f:
    input_json = json.load(f)

input_folder = input_json['input_folder']



# get the file path and record number
record_number = image_name.split("_")[-1].replace(".png", "")
record_number = int(record_number)
file_name = image_name.split("_")[:-1]
file_name = "_".join(file_name)
list_of_files = np.loadtxt(list_of_paths, dtype=str)

# create the output folder
output_folder = output_folder + str(record_number) + "/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# find the filename in the list of files
file_path = ""
for file in list_of_files:
    if file_name in file:
        file_path = file
        break
if file_path == "":
    print("File not found")
    sys.exit()

print("File path: ", file_path)

# do plots

plot_beam_status(   beam_status_file = beam_status_file, 
                    filename = file_path,
                    record_number = record_number,
                    det = det,
                    channel_map_name = channel_map_name,
                    outname = output_folder + f"beam_status_{record_number}")



print("Done")


