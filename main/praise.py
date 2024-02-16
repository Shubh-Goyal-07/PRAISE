import argparse
import sys

from helpers import preprocessing

import cv2

def read_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Input Image Path")
    args = parser.parse_args()
    path = args.path

    if not path:
        print("Please provide a path to the image")
        sys.exit(1)

    return path

def pipeline():
    path = read_args()

    # Display the original image
    cv2.imshow("Original Image", cv2.imread(path))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)


if __name__ == "__main__":
    read_args()
    pipeline()