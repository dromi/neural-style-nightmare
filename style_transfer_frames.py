import glob
import os
import sys
from shutil import copyfile
from tile_image import tile_image

INPUT_DIR = 'data/'
OUTPUT_DIR = 'result/'


def transfer_onto_self(frame_dir, output_dir, sim_args):
    files = glob.glob(INPUT_DIR + "*.jpg")
    output_files = glob.glob(OUTPUT_DIR + "*.jpg")
    input_numbers = [''.join(c for c in f if c.isdigit()) for f in files]
    output_numbers = [''.join(c for c in f if c.isdigit()) for f in output_files]
    missing = list(set(input_numbers) - set(output_numbers))
    files = [INPUT_DIR + 'frame' + m + '.jpg' for m in missing]

    for f in files:
        file_number = ''.join(c for c in f if c.isdigit())
        stry = "python neural_style.py --content " + f + "--styles " + f + " --output " + OUTPUT_DIR + "output_frame-" + "%04d" % file_number + ".jpg" + sim_args
        print("RUNNING")
        print(stry)
        os.system(stry)


def transfer_with_same_style(frame_dir, style_path, output_dir, sim_args=''):
    files = sorted(glob.glob(frame_dir + "*.jpg"))

    # Do first image seperately
    f0 = files[0]

    stry = "python impl/neural_style.py --content " + f0 + " --styles " + style_path + " --output " + output_dir + \
           "output_frame-" + "%04d" % 0 + ".jpg " + sim_args
    print("RUNNING")
    print(stry)
    os.system(stry)

    for f in files[1:]:
        file_number = int(''.join(c for c in f if c.isdigit()))
        stry = "python impl/neural_style.py --content " + f + " --styles " + style_path + " --output " + output_dir + "output_frame-"\
               + "%04d" % file_number + ".jpg" + ' --initial ' + output_dir + "output_frame-" + "%04d" % int(file_number - 1) + ".jpg " + sim_args
        print("RUNNING")
        print(stry)
        os.system(stry)


def transfer_with_same_tiled_style(frame_dir, output_dir, tiling_shape, sim_args=''):
    files = sorted(glob.glob(frame_dir + "*.jpg"))
    width_tiles, height_tiles = tiling_shape
    tmp_dest = 'tiled_tmp.jpg'
    # Do first image seperately
    f0 = files[0]

    tile_image(f0, width_tiles, height_tiles, tmp_dest)

    stry = "python impl/neural_style.py --content " + f0 + " --styles " + tmp_dest + " --output " + output_dir + \
           "frame-" + "%04d" % 0 + ".jpg " + sim_args + " --network impl/imagenet-vgg-verydeep-19.mat"
    print("RUNNING")
    print(stry)
    os.system(stry)

    for f in files[1:]:
        file_number = int(''.join(c for c in f if c.isdigit()))
        tile_image(f, width_tiles, height_tiles, tmp_dest)
        stry = "python impl/neural_style.py --content " + f + " --styles " + tmp_dest + " --output " + output_dir + "frame-"\
               + "%04d" % file_number + ".jpg" + ' --initial ' + output_dir + "frame-" + "%04d" % int(file_number - 1) + ".jpg " + sim_args  + " --network impl/imagenet-vgg-verydeep-19.mat"
        print("RUNNING")
        print(stry)
        os.system(stry)
        
        

if __name__ == '__main__':
    # transfer_onto_self()
    # transfer_with_same_style('content/face/', 'examples/1-style.jpg', 'results/face_gogh_video/', '--iterations 500')
    transfer_with_same_tiled_style("content/face/", "results/tiles/face_tile_face/", (8,7), sim_args=str(' '.join(sys.argv[1:])))
