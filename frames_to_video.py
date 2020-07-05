import glob
import sys

from shutil import copyfile


"""
Collapse frames from a dir to a video
arg 1: input folder path
arg 2: output video folder
"""

if __name__ == '__main__':
    input_dir = sys.argv[1]
    output_folder = sys.argv[2]

    files = glob.glob(input_dir + "*.jpg")

    for f in files:
        file_number = ''.join(c for c in f if c.isdigit())
        new_file_name = 'output_frame-' + "{0:0=5d}".format(int(file_number)) + '.jpg'
        copyfile(f, output_folder + new_file_name)
