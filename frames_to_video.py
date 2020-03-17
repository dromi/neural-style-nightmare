import glob
import os

from shutil import copyfile

INPUT_DIR = 'result/'
OUTPUT_DIR = 'result_spaced/'


if __name__ == '__main__':
    files = glob.glob(INPUT_DIR + "*.jpg")
    # output_files = glob.glob(OUTPUT_DIR + "*.jpg")

    for f in files:
        file_number = ''.join(c for c in f if c.isdigit())
        new_file_name = 'output_frame-' + "{0:0=5d}".format(int(file_number)) + '.jpg'
        copyfile(f, OUTPUT_DIR + new_file_name)
