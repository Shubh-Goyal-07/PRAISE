def find_hslant(path):
    import cv2
    import numpy as np
    from sklearn import linear_model
    #path = input("Enter the Path of image: ")

    # Reading an image in default mode
    image = cv2.imread(path)

    # Window name in which image is displayed
    window_name = 'image'

    # Using cv2.imshow() method
    # Displaying the image
    # print("regular")
    # cv2.imshow("dispimg", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print("Grayscale:")
    # cv2.imshow("grayimg", gray)

    # Binarization using simple thresholding
    threshold, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    # print("Thresholded:")
    # cv2.imshow("thresh", thresh)

    # Vertically spliting the image into n pieces
    points = 50
    lis = np.array_split(thresh, points, axis=1)
    # finding the x and y centroids of each splitted image
    x = np.zeros(points)
    y = np.zeros(points)
    centroid_i = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    sum = 0
    for i in range(points):
        if i != 0:
            sum += lis[i - 1].shape[1]
        if cv2.moments(lis[i])["m00"] == 0:
            continue
        x[i] = int(cv2.moments(lis[i])["m10"] / cv2.moments(lis[i])["m00"]) + sum
        y[i] = int(cv2.moments(lis[i])["m01"] / cv2.moments(lis[i])["m00"])
        cv2.circle(centroid_i, (int(x[i]), int(y[i])), 3, (0, 0, 255), -1)
        # print(i)
        # Centroids of each spitted image with respect to original image
    # print("Centroids:")
    # cv2.imshow("kk", centroid_i)

    x_train = []
    y_train = []
    for i in range(points):
        if (y[i] != 0):
            # print(x[i,],y[i])
            x_train.append(x[i])
            y_train.append(y[i])

    x_tra = np.array(x_train)
    y_tra = np.array(y_train)

    model = linear_model.LinearRegression()

    model.fit(x_tra.reshape(-1, 1), y_tra)
    slope = -model.coef_[0]
    intercept = thresh.shape[0] - model.intercept_
    #print(f"Slope of the line: {slope}")
    #print(f"Intersept of the line: {intercept}")

    degrees = np.degrees(np.arctan(slope))
    #print(f"Angle the word makes with base line(in degrees): {degrees}")
    return round(degrees, 4)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


