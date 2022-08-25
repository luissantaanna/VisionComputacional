import cv2
imagen1=cv2.imread('wha.jpg',cv2.IMREAD_COLOR)
print('Color', imagen1)
cv2.imshow('Imagen1', imagen1)
cv2.waitKey(0)

imagen2=cv2.imread('wha.jpg',cv2.IMREAD_GRAYSCALE)
print('Escala de grises', imagen2)
cv2.imshow('Imagen', imagen2)
cv2.waitKey(0)

