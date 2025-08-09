//Code specific for Arduino Mega 2560
// PORTE 4 is line 2
// PORTH 0 is line 17
// PORTJ ?? is line 15  
int line_period_us = 83/2;
int on_delay = 3;
int gatetime = line_period_us - 2 * on_delay;
float duty_cycle_off = 0.6;
int off_time = line_period_us * duty_cycle_off;
int a = (line_period_us - off_time) / 2;
int c = a * 2;

void setup() {
  // put your setup code here, to run once:
  DDRE = B11111100;  //Pin 1 of PORTE is an input, all others are outputs
  DDRH = B00000000;  
  DDRJ = B00000000;  

  DDRH = B00000000;
  PORTH = B11111111;
  PORTJ = B11111111;

  noInterrupts();
}

void loop() {
  // check pin 17 if it's hi or lo
  if ((PINJ & B00000001) == 1) { // check pin 15 for fast or slow
    if ((PINH & (B00000001)) == 1) {
      PORTE = (1 << PD4);           //Pin 2 of portd as now the logic value 1
      delayMicroseconds(a);         //16
      PORTE = (0 << PD4);           //Pin 2 of portd as now the logic value 0
      delayMicroseconds(off_time);  //34
      PORTE = (1 << PD4);           //Pin 2 of portd as now the logic value 1
      delayMicroseconds(c);         //32
      PORTE = (0 << PD4);           //Pin 2 of portd as now the logic value 0
      delayMicroseconds(off_time);  //34
      PORTE = (1 << PD4);           //Pin 2 of portd as now the logic value 1
    }
  } else if ((PINJ & B00000001) == 0) {
    if ((PINH & (B00000001)) == 0) {
      delayMicroseconds(on_delay);
      PORTE = (1 << PD4);
      delayMicroseconds(gatetime);
      PORTE = (0 << PD4);
      delayMicroseconds(2*on_delay);
    }
  }
}
