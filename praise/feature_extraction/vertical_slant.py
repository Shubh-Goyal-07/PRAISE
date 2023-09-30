import cv2
import numpy as np
import math
def verticalslant(pathfile):
    image1 = cv2.imread(pathfile)
    image = cv2.cvtColor(image1 , cv2.COLOR_BGR2GRAY)
    height, width = image.shape
    third_height = height // 3
    concimg = np.zeros((height, width,3))
    aroy = np.zeros((3,2))
    for i in range(3):
        start_row = i * third_height
        end_row = (i + 1) * third_height
        threshold , thresh = cv2.threshold(image[start_row:end_row, :], 150, 255, cv2.THRESH_BINARY_INV)
        Moments = cv2.moments(thresh)
        x = int(Moments["m10"] / Moments["m00"])
        y = int(Moments["m01"] / Moments["m00"])
        aroy[i] = [x, y+i*third_height]
        centroid = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        cv2.circle(centroid, (x,y), radius=3, color=(0, 0, 255), thickness=-1)
        concimg[start_row:end_row, :] = centroid

    #cv2.imshow('IMAGE WITH CENTROIDS',concimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    for i in range(3):
        print(aroy[i])
    print("\n")
    x_values = aroy[:, 0]
    y_values = aroy[:, 1]

    coefficients = np.polyfit(x_values, y_values, 1)

    slope = coefficients[0]
    intercept = coefficients[1]

    print(f"Linear Regression: y = {slope:.2f}x + {intercept:.2f}")
    angle_radians = math.atan2(slope, 1)
    angle_degrees = (-1)*math.degrees(angle_radians)

    print(f"Angle made by slant:  {angle_degrees:.2f} degrees")

    x1 = int(min(x_values))
    x2 = int(max(x_values))
    y1 = int(slope * x1 + intercept)
    y2 = int(slope * x2 + intercept)

    cv2.line(concimg, (x1, y1), (x2, y2), (0, 255, 0), 2)
    text1 = f"Linear Regression: y = {slope:.2f}x + {intercept:.2f}"
    text2 = f"Angle made by slant:  {angle_degrees:.2f} degrees"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (255, 255, 255)  # White color in BGR
    font_thickness = 2
    position1 = (50, 50)  # (x, y) coordinates where you want to place the text
    position2 = (50,100)
    # Add the text to the image
    concimg = cv2.putText(concimg.copy(), text1, position1, font, font_scale, font_color, font_thickness)
    concimg = cv2.putText(concimg.copy(), text2, position2, font, font_scale, font_color, font_thickness)
   # cv2.imshow('SLANT LINE',concimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
