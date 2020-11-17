import subprocess
import os
from pathlib import Path


parent_dir = str(Path(os.getcwd()).parent)
files_to_convert = os.listdir(parent_dir + '/convertedFiles/')  # Gets a list of all files in the specified directory

for file in files_to_convert:  # Loops through all files
    src_file = parent_dir + "/convertedFiles/" + file
    dst_file = parent_dir + "/smileOutput/" + os.path.splitext(file)[0] + ".arff"
    command = 'start SMILExtract_ReleasePortaudio.exe -C confs\emo_large.conf -I "' + src_file + '" -O "' + dst_file + '"'
    subprocess.Popen('cmd /k' + command)
