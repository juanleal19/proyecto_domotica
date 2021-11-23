#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
#include <Servo.h>
Servo servo1;

int sensor_luz = A0;
int pinServo = 9;
int pinLed = 12;
int valor_luz;

void setup() {
  Serial.begin(9600);
  dht.begin();
  servo1.attach(pinServo); 
  pinMode(sensor_luz,INPUT);
  pinMode(sensor_luz,OUTPUT);
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

int servo2()
{

while(true)
  {
    valor_luz =  analogRead(A0);
    char Dato = Serial.read();
    delay(1000);

    if (valor_luz > 400 )
    {
      servo1.write(180);
      valor_luz =  analogRead(A0);
      Serial.print(valor_luz);
      digitalWrite(pinLed, LOW); 
      char Dato = Serial.read();
      if (Dato == 'e')
      {
        break;
      }
    }
    else if (valor_luz < 300)
    {
      servo1.write(10);
      valor_luz =  analogRead(A0);
      Serial.print(valor_luz);
      digitalWrite(pinLed, HIGH); 
      char Dato = Serial.read();
      if (Dato == 'e')
      {
      break;
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
    servo2();
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
