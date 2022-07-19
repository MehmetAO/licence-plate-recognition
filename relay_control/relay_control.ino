int data;

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(11,OUTPUT);
  digitalWrite (11, LOW); //initially set to low
}
 
void loop() 
{
while (Serial.available())
  {
    data = Serial.read();
  }

  if (data == '1')
  digitalWrite (11, HIGH);

  else if (data == '0')
  digitalWrite (11, LOW);

}
