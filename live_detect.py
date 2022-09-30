# importe a biblioteca opencv 
import cv2
from numpy import get_array_wrap

# Defina um objeto VideoCapture
vid = cv2.VideoCapture(0)
competissao = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
   
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = competissao.detectMultiScale(gray, 1.1, 4)
    for(x,y,elastico,helastico) in rostos:
        cv2.rectangle(frame, (x,y), (x+elastico, y+helastico), (255,0,0), 2)

    # Exiba o quadro resultante
    cv2.imshow("Web cam", frame)
      
    # Saia da tela ao pressionar a barra de espaço
    if cv2.waitKey(25) == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as telas
cv2.destroyAllWindows()