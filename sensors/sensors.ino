#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "PLUGNET-22355-2.4";
const char *password = "82ou8jt3";
const char *serverUrl = "http://192.168.0.112";

void setup() {
  Serial.begin(115200);

  // Conectar ao Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");

  delay(1000);
}

void loop() {
  // Ler dados dos sensores
  float dadoSensor1 = lerSensor1();
  float dadoSensor2 = lerSensor2();

  // Enviar dados para o servidor
  enviarDados(dadoSensor1, dadoSensor2);

  delay(5000);  // Aguardar 5 segundos antes de enviar novamente
}

float lerSensor1() {
  // Lógica para ler dados do Sensor 1
  return 25.5;  // Substitua pelo valor real lido pelo Sensor 1
}

float lerSensor2() {
  // Lógica para ler dados do Sensor 2
  return 30.0;  // Substitua pelo valor real lido pelo Sensor 2
}

void enviarDados(float sensor1, float sensor2) {
  HTTPClient http;

  // Construir a URL com os parâmetros
  String url = serverUrl + "?sensor1=" + String(sensor1) + "&sensor2=" + String(sensor2);

  Serial.print("Enviando dados para: ");
  Serial.println(url);

  // Enviar a requisição HTTP
  http.begin(url);
  int httpResponseCode = http.GET();

  // Verificar o código de resposta
  if (httpResponseCode > 0) {
    Serial.print("Resposta do servidor: ");
    Serial.println(httpResponseCode);
  } else {
    Serial.println("Falha na requisição HTTP.");
  }

  // Libera os recursos da requisição HTTP
  http.end();
}
