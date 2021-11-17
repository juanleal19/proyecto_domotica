#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
#include <Servo.h>
Servo servo1;
int pinServo = 9;
String inString = "";

void setup() {
  Serial.begin(9600);
  dht.begin();
  servo1.attach(pinServo); 
  pinMode(LED_BUILTIN, OUTPUT);
}
 

int humedad()
{
  delay(1);
  float h = dht.readHumidity();
  if (isnan(h) ) {
    Serial.println("Error obteniendo los datos del sensor DHT22");
    return;
  } 
  return (h) ;
}
int temperatura()
{
  delay(1);  
  float t = dht.readTemperature();
 
  if ( isnan(t)) {
    Serial.println("Error obteniendo los datos del sensor DHT22");
    return;
  } 
  return (t) ;
}

int servo()
{
  int x = 0;
  Serial.print("listo");
  while (x < 3)
  {
  if(Serial.available() > 0){
    int inChar = Serial.read();
    
    if(inChar != '\n'){
      inString += (char)inChar; 
      
      }
    
    else{
      float angulo =inString.toFloat();
      Serial.println(angulo);
      servo1.write(angulo);
      inString = ""; 
      x = x + 1; 
        }
    
   }
  }
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
  else if (Dato == 's' )
  {
    Serial.println("servo");
   // servo();
  }

    else if (Dato == 'o' ) // dato para encender el led
  {
     digitalWrite(LED_BUILTIN, HIGH);   
     delay(10);   
  }
    else if (Dato == 'f' )  // dato para apagar el led
  {
     digitalWrite(LED_BUILTIN, LOW);   
     delay(10);     

  }
  
}
