import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype=np.uint8)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# Note: Bitwise AND --> Intersection --> Returns Area Common in both Images --> (A⋂B)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Note: Bitwise OR --> Union --> Return All Area i.e., Common and Uncommon --> (A⋃B)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# Note: Bitwise XOR --> Return Full Area excluding the Common Area --> (A⋃B)-(A⋂B)
# It can also be said as (Bitwise OR - Bitwise AND)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# Note: Bitwise NOT --> Inverts the Colors
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT - Rectangle", bitwise_not)

cv.waitKey(0)