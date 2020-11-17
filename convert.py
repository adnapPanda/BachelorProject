import os
import subprocess

# Created by: Robin Herlan
# Date: 14/11/2020
# Script to convert any file that is accepted by ffmpeg into .wav.
# Requires destination folder to be empty.
# Unaccepted file formats won't be converted, but won't stop the script.
# Setup: Download ffmpeg and add to PATH. Run script.


def convert_files():
    files_to_convert = os.listdir('filesToConvert/')  # Gets a list of all files in the specified directory

    for file in files_to_convert:  # Loops through all files and converts them to .wav
        src_file = "filesToConvert/" + file
        dst_file = "convertedFiles/" + os.path.splitext(file)[0] + ".wav"
        command = 'ffmpeg -i "' + src_file + '" "' + dst_file + '"'
        subprocess.Popen('cmd /k' + command)


convert_files()  # Converts all files in directory to .wav


