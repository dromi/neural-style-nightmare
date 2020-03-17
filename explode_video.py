import cv2

if __name__ == '__main__':
    vidcap = cv2.VideoCapture('movies/the_face/fixed/cropped/output_cropped.avi')
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite("movies/the_face/fixed/cropped/frame%04d.jpg" % count, image)     # save frame as JPEG file
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
