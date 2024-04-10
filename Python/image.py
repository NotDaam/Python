import cv2

imagen = cv2.imread('Capturas/paisaje.jpg',1)
cv2.imshow('Paisaje',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows() 