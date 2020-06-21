import numpy as np
import cv2

b = np.ones([455,455],dtype = 'uint8')*250

n = int(57)
for i in range(n,455,n*2):
    for j in range(n,455,n*2):
        b[j-n:j,i-n:i] = 0
        b[j:j+n,i:i+n] = 0

cv2.imshow('CheckerBoard 8 * 8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
