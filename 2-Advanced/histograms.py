import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# NOTE: Histograms help us visualize distribution of pixel intensities in the Image

# Getting the Image
img = cv.imread("F:\OpenCV\Learning\Resources\Images\cats.jpg")
cv.imshow("Cats Image", img)

# Getting the shape of the Image
width = img.shape[1]
height = img.shape[0]

# Creating a blank image for mask
blank = np.zeros((height, width), np.uint8)

def grayscale_histogram(img, mask=None):
    # Converting the image to gray scale
    gray = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale Image", gray)

    # If the mask is passed apply the mask and show masked image
    masked_image = cv.bitwise_and(gray, gray, mask=mask)
    cv.imshow("Masked Image", masked_image)

    # Getting the Histogram data for the masked image
    gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

    # Plotting the Pixel Intensity Distribution
    plt.style.use("seaborn-whitegrid")
    plt.figure(dpi=100, figsize=(10, 6))
    plt.title("Grayscale Histogram", fontdict={"fontsize":16, "fontweight":"bold"})
    plt.xticks(np.arange(0, 275, 25))
    plt.xlabel("Pixel Intensities")
    plt.ylabel("No of Pixels")
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()

# circle_mask = cv.circle(blank.copy(), (width//2, height//2), 100, 255, -1)
# grayscale_histogram(img, circle_mask)

def color_histogram(img, mask=None):
    # If the mask is passed apply the mask and show masked image
    masked_image = cv.bitwise_and(img, img, mask=mask)
    cv.imshow("Masked Image", masked_image)

    colors = ("b", "g", "r")

    plt.style.use("seaborn-whitegrid")
    plt.figure(dpi=100, figsize=(10, 6))
    plt.title("Color Histogram", fontdict={"fontsize":16, "fontweight":"bold"})
    plt.xticks(np.arange(0, 275, 25))
    plt.xlabel("Pixel Intensities")
    plt.ylabel("No of Pixels")
    plt.xlim([0, 256])

    for i, color in enumerate(colors):
        hist = cv.calcHist([img], [i], mask, [256], [0, 256])
        plt.plot(hist, color=color)

    plt.show()

rectangle_mask = cv.rectangle(blank.copy(), (width//2-150, height//2-100), (width//2+150, height//2+100), 255, -1)
color_histogram(img, mask=rectangle_mask)