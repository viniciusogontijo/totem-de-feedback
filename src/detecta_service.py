import cv2

def detectar_presenca():
    ## usando o opencv para dectar rosto em frete ao totem.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    webcam = cv2.VideoCapture(0)

    print("Aguardando visitante...")
    presenca_detectada = False

    # tentativa de captura 
    for _ in range(5):
        check, img = webcam.read()
        if not check: break

        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(cinza, 1.1, 4)

        if len(faces) > 0:
            presenca_detectada = True
            break

    webcam.release()
    return presenca_detectada
