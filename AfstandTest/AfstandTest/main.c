/*
 *   
 *      Program uses a ATMega328p MCU to query a HC-SR04 ultrasonic module. Then Calculates and displays the distance to a object in cm on the NewHaven display.
 *
 *      The ultrasonic module is triggered every 60 ms by setting pin PC4 (the trigger) high for 10 us. A change in state on pin PC5 (the echo)
 *      causes a interrupt. The interrupt checks if PC5 is high. If it is a timer is started that increments every micro second. Once PC5 triggers a
 *      interrupt again and is low the result is calculated and displayed in centimeters on the NewHaven display. Distance in cm is calculated
 *      by the amount of microseconds PC5 (the echo) is active high divided by 58.
 *
 *      Pin placement of ATMega328p:
 *      Pin PC4				HC-SR04 Trig
 *      Pin PC5				HC-SR04 Echo
 */
#define F_CPU 1000000UL
#define UBBRVAL 51 // baudrate op 19.200

#include <stdio.h>
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdlib.h>
/*******************************************INITALIZE PORTS, TIMER, AND INTURRUPTS*******************************************/
void init() {
	DDRC = 0xFF;							// Port C all output. PC0: RW		PC1: RS		PC2: E
	DDRC &= ~(1<<DDC5);						// Set Pin C5 as input to read Echo
	PORTC |= (1<<PORTC5);					// Enable pull up on C5
	PORTC &= ~(1<<PC4);						// Init C4 as low (trigger)

	PRR &= ~(1<<PRTIM1);					// To activate timer1 module
	TCNT1 = 0;								// Initial timer value
	TCCR1B |= (1<<CS10);					// Timer without prescaller. Since default clock for atmega328p is 1Mhz period is 1uS
	TCCR1B |= (1<<ICES1);					// First capture on rising edge

	PCICR = (1<<PCIE1);						// Enable PCINT[14:8] we use pin C5 which is PCINT13
	PCMSK1 = (1<<PCINT13);					// Enable C5 interrupt
	sei();									// Enable Global Interrupts
}


void uart_init()
{
	// set the baud rate | UBRR is het register
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter
	UCSR0B = _BV(RXEN0) | _BV(TXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}

void serialOut(char* Message){
	int i = 0;
	for(i=0; i < strlen(Message); i++){
		while ( !( UCSR0A & (1<<UDRE0)) );
		UDR0 = Message[i];
	}
	_delay_ms(1000);
}


/*******************************************INPUT HEX 0 - F AND RETURNS PROPER VALUE FOR DISPLAY*******************************************/
uint8_t HexToDisplayCode(uint8_t hex) {
	if (hex == 0x00) {return 0x30;}
	if (hex == 0x01) {return 0x31;}
	if (hex == 0x02) {return 0x32;}
	if (hex == 0x03) {return 0x33;}
	if (hex == 0x04) {return 0x34;}
	if (hex == 0x05) {return 0x35;}
	if (hex == 0x06) {return 0x36;}
	if (hex == 0x07) {return 0x37;}
	if (hex == 0x08) {return 0x38;}
	if (hex == 0x09) {return 0x39;}
	if (hex == 0x0A) {return 0x41;}
	if (hex == 0x0B) {return 0x42;}
	if (hex == 0x0C) {return 0x43;}
	if (hex == 0x0D) {return 0x44;}
	if (hex == 0x0E) {return 0x45;}
	if (hex == 0x0F) {return 0x46;}
	return 0x21;	// 0x21 is an !
}

/*******************************************MAIN PROGRAM*******************************************/
int main() {
	init();
	uart_init();
	while (1) {
		_delay_ms(60); 							// To allow sufficient time between queries (60ms min)

		PORTC |= (1<<PC4);						// Set trigger high
		_delay_us(10);							// for 10uS
		PORTC &= ~(1<<PC4);						// to trigger the ultrasonic module				
	}
}
/*******************************************INTURRUPT PCINT1 FOR PIN C5*******************************************/
ISR(PCINT1_vect) {
	if (bit_is_set(PINC,PC5)) {					// Checks if echo is high
		TCNT1 = 0;								// Reset Timer
		PORTC |= (1<<PC3);
	} else {
		uint16_t numuS = TCNT1;					// Save Timer value
		uint8_t oldSREG = SREG;
		cli();	

		uint16_t uitkomst = (numuS*0.034/2)/15;
		char temp[7];
		itoa(uitkomst, temp, 10);
		serialOut(temp);		

		SREG = oldSREG;							// Enable interrupts
	}
}