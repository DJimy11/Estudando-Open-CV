import cv2

carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
imagem = cv2.imread('imagens/img2.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaAlgoritmo.detectMultiScale(cinza, scaleFactor=1.8, minNeighbors=1)
print(faces)

for (x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)

cv2.imshow('Faces', imagem)
cv2.waitKey()
