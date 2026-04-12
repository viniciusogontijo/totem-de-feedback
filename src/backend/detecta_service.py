import cv2
import mediapipe as mp


def detectar_presenca(caminho_teste=None):
    mp_face_detection = mp.solutions.face_detection
    presenca = False

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        if caminho_teste:
            img = cv2.imread(caminho_teste)
            if img is None:
                print(f"Erro: imagem não localizada no caminho passado {caminho_teste}")
                return False
        else:
            webcam = cv2.VideoCapture(0)
            sucesso, img = webcam.read()
            webcam.release()
            if not sucesso: return False
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resultado = face_detection.process(img_rgb)

        if resultado.detections:
            presenca = True

    return presenca
