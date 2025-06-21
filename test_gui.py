import cv2
import numpy as np

# Create a blank white image (300x300 pixels)
img = np.ones((300, 300, 3), dtype=np.uint8) * 255

# Show the image in a window
cv2.imshow("Test Window", img)

# Wait for a key press, then close
cv2.waitKey(0)
cv2.destroyAllWindows()
