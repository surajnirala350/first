import cv2
import argparse
#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i/--image', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading the image with opencv
img = cv2.imread(img_path)


while(1):
    
    cv2.imshow("image",img)
    if cv2.waitKey(20) & 0xFF ==27:
        break
