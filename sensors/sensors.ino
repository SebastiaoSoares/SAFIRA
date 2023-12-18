#include <WiFi.h>

#define WIFI_SSID     "SAFIRA"
#define WIFI_PASSWORD "milkshake"
#define SERVER_IP     "192.168.100.96"
#define SERVER_PORT   80

const char *host = SERVER_IP;
const int port = SERVER_PORT;

const int smokePin = 13;  // Pino do sensor de fumaça MQ-2

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Iniciando...");

  // Conecta-se à rede Wi-Fi
  connectToWiFi();
}

void loop() {
  // Lê o valor do sensor de fumaça MQ-2
  float smokeValue = getSmokeValue();

  // Envia dados para o servidor Python
  sendDataToServer(smokeValue);

  delay(5000);  // Aguarda 5 segundos antes de enviar o próximo conjunto de dados
}

void connectToWiFi() {
  Serial.println("Conectando-se à rede Wi-Fi...");

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("Conectado à rede Wi-Fi");
  Serial.println("Endereço IP: " + WiFi.localIP().toString());
}

float getSmokeValue() {
  // Lê o valor analógico do sensor de fumaça MQ-2
  int sensorValue = analogRead(smokePin);

  // Converte para uma escala de 0 a 100 (ou ajuste conforme necessário)
  float smokePercentage = map(sensorValue, 0, 1023, 0, 100);

  Serial.print("Valor do sensor de fumaça: ");
  Serial.println(smokePercentage);

  return smokePercentage;
}

void sendDataToServer(float smokeValue) {
  Serial.print("Enviando dados para o servidor... ");

  WiFiClient client;

  if (client.connect(host, port)) {
    String data = "smoke=" + String(smokeValue);

    client.println("POST / HTTP/1.1");
    client.println("Host: " + String(host));
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println("Content-Length: " + String(data.length()));
    client.println();
    client.print(data);

    delay(10);

    while (client.available()) {
      Serial.write(client.read());
    }

    client.stop();
    Serial.println("Dados enviados com sucesso");
  } else {
    Serial.println("Falha na conexão com o servidor");
  }
}
