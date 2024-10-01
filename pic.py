import cv2
import numpy as np


image = cv2.imread('./images.jpeg')

mask = np.zeros(image.shape[:2], np.uint8)


bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)


cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')


foreground = image * mask2[:, :, np.newaxis]

blurred = cv2.GaussianBlur(image, (21, 21), 0)


background = blurred * (1 - mask2[:, :, np.newaxis])
final_image = cv2.add(foreground, background)

cv2.imshow('Blurred Background with Sharp Subject', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('output_image.jpg', final_image)
