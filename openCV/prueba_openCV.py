import cv2
import mediapipe as mp

# Inicializar la detección de manos de Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a escala de grises
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar manos en la imagen
    results = hands.process(rgb)

    # Si se detectan manos, iterar sobre ellas
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Obtener la posición de la muñeca de la mano
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Convertir las coordenadas normalizadas a píxeles
            img_h, img_w, _ = frame.shape
            wrist_px = int(wrist.x * img_w), int(wrist.y * img_h)

            # Dibujar un círculo en la muñeca
            cv2.circle(frame, wrist_px, 10, (0, 255, 0), -1)

            # Determinar la mano levantada
            if wrist_px[1] < img_h // 2:  # Si la muñeca está por encima del centro de la imagen
                position_text = "Mano levantada"
            else:
                position_text = "Mano abajo"

            # Determinar si es mano izquierda o derecha
            if idx == 0:
                hand_text = "Mano izquierda"
            else:
                hand_text = "Mano derecha"

            # Mostrar el texto
            cv2.putText(frame, position_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, hand_text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar el fotograma resultante
    cv2.imshow('frame', frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
