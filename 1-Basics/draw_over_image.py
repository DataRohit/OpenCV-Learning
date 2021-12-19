import cv2 as cv
import numpy as np

# Load the image from the given location
def ReadImage(path):
    return cv.imread(path)

# Create a Blank Image
# Datatype uit8 is the datatype of the Images
def BlankImage(shape=(500, 500, 3)):
    return np.zeros(shape, dtype="uint8")

# Display the given image with the given title
def ShowImage(image, title="Image"):
    cv.imshow(title, image)
    cv.waitKey(0)

blank = BlankImage(shape=(500, 500, 3))   

# NOTE 1: Paint the Image a certain color
# blank[:] = 0,255,255

# NOTE 2: Paint the specific region of the Image
# blank[200:300, 300:400] = 0,0,255

# NOTE 3: Draw a Rectangle on the Image
def DrawRectangle(image, start, end, color, thickness=2):
    cv.rectangle(image, start, end, color, thickness)

# # Outlined Rectangle
# DrawRectangle(image=blank, start=(0, 0), end=(300, 150), color=(0, 255, 0), thickness=2)

# # Filled Rectangle -> thickness = cv.FILLED or -1
# DrawRectangle(image=blank, start=(0, 0), end=(300, 150), color=(0, 255, 0), thickness=-1)

# # Use the Image dimension to create the rectangle
# DrawRectangle(image=blank, start=(0, 0), end=(blank.shape[1]//2, blank.shape[0]//2),
#               color=(0, 255, 0), thickness=-1)

# NOTE 3: Draw a Circle on the Image
def DrawCircle(image, center, radius, color, thickness=3):
    cv.circle(image, center, radius, color, thickness)

# # Outlined Circle
# DrawCircle(image=blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=40, 
#            color=(0, 0, 255), thickness=3)

# # Filled Circle
# DrawCircle(image=blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=100, 
#            color=(0, 255, 255), thickness=-1)

# NOTE 4: Draw a Line on the Image
def DrawLine(image, start, end, color, thickness=3):
    cv.line(image, start, end, color, thickness)

# # Draws the Line between the given points
# DrawLine(image=blank, start=(0, 0), end=(blank.shape[1]//2, blank.shape[0]//2), color=(255, 255, 255))
# DrawLine(image=blank, start=(100, 250), end=(300, 400), color=(255, 255, 255))

# NOTE 5: Write Text on the Image
def WriteText(image, text, start, fontface, fontscale, color, thickness=2):
    cv.putText(image, text, start, fontface, fontscale, color, thickness)

WriteText(blank, "Hello, My Name is Rohit!!!", (0, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

ShowImage(image=blank)