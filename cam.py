import cv2
import os
import time
from smoke_detection.detector import SmokeDetector

# Verifica e cria a pasta de destino se ela não existir
output_folder = 'imagens_detectadas'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Inicializando a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Configurações iniciais
num_frames = 0
max_frames = 60
frame_interval = 1  # intervalo em segundos

# Inicializar o detector de fumaça
detector = SmokeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Verifica se há fumaça na imagem
    if detector.is_smoke(frame):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        img_name = f'imagem_{timestamp}.png'
        cv2.imwrite(os.path.join(output_folder, img_name), frame)

    num_frames += 1

    # Apaga a foto mais antiga após 60 fotos
    if num_frames > max_frames:
        files = sorted(os.listdir(output_folder))
        if files:
            os.remove(os.path.join(output_folder, files[0]))
        num_frames = 0

    time.sleep(frame_interval)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e destruir as janelas
cap.release()
cv2.destroyAllWindows()
