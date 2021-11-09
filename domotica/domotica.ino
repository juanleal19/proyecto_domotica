#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
 
}
 
int humedad()
{
  delay(500);
  float h = dht.readHumidity();
  if (isnan(h) ) {
    Serial.println("Error obteniendo los datos del sensor DHT22");
    return;
  } 
  return (h) ;
}
int temperatura()
{
  delay(500);  
  float t = dht.readTemperature();
 
  if ( isnan(t)) {
    Serial.println("Error obteniendo los datos del sensor DHT22");
    return;
  } 
  return (t) ;
}

void loop() {
  
char Dato = Serial.read();

  if(Dato == '1')
  {
    Serial.println(humedad());
  }
  else if (Dato == '2')
  {
    Serial.println(temperatura());
  }
  
  
}
