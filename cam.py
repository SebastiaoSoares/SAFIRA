import cv2
import os
import time

# Diretório onde as fotos serão armazenadas
output_directory = 'static/images/fire_analysis/'
smoke_directory = 'static/images/fire_analysis/fire_detected/'  # Pasta para armazenar imagens com detecção de fumaça

# Cria o diretório se ele não existir
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

if not os.path.exists(smoke_directory):
    os.makedirs(smoke_directory)

# Inicializa a câmera
cap = cv2.VideoCapture(1)

# Define a contagem de tempo
start_time = time.time()
capture_interval = 1  # Captura uma foto a cada segundo
max_photos = 60  # Mantém no máximo 60 fotos

while True:
    # Captura um frame da câmera
    ret, frame = cap.read()

    if ret:
        # Mostra a imagem na tela (opcional)
        cv2.imshow('Captured Image', frame)

        # Verifica se passou o intervalo de captura
        if time.time() - start_time >= capture_interval:
            # Salva a foto com o nome 'capture.jpg'
            file_name = f'{output_directory}capture.jpg'

            # Salva a foto mais recente
            cv2.imwrite(file_name, frame)

            # Converte a foto para escala de cinza
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Aplica um desfoque para reduzir ruídos
            blurred_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            # Detecta contornos na imagem
            _, thresholded = cv2.threshold(blurred_frame, 200, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Se houver contornos, pode ser fumaça
            if len(contours) > 0:
                print("Possível presença de fumaça!")
                # Salva a imagem com detecção de fumaça como 'smoke.jpg'
                smoke_file_name = f'{smoke_directory}smoke.jpg'
                cv2.imwrite(smoke_file_name, frame)

            start_time = time.time()

        # Verifica se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Fecha a câmera e a janela
cap.release()
cv2.destroyAllWindows()
