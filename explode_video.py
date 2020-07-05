import sys

import cv2



"""
Break a video file into frame images
arg 1: input video path
arg 2: output folder path
"""

if __name__ == '__main__':
    input_video = sys.argv[1]
    output_folder = sys.argv[2]
    vidcap = cv2.VideoCapture(input_video)
    success, image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite(f"{output_folder}/frame%04d.jpg" % count, image)     # save frame as JPEG file
      success, image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
