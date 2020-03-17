import os

iterations = 30
content_image = 'examples/1-content.jpg'
dir = 'onto_self'

if __name__ == '__main__':
    stry = "python neural_style.py --content " + content_image + " --styles " + content_image + " --output " + dir + "/output-0.jpg"
    print("RUNNING")
    print(stry)
    os.system(stry)
    for i in range(1, iterations):
        stry = "python neural_style.py --content " + dir + "/output-" + str(i-1) + ".jpg --styles " + content_image + " --output " + dir + "/output-" + str(i) + ".jpg"
        print("RUNNING")
        print(stry)
        os.system(stry)
