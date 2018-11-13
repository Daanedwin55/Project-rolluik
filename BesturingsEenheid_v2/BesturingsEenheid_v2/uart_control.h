/*
*   UART settings
*/
#include <string.h>
#define UBBRVAL 51 // baudrate op 19.200

// output on USB = PD1 = board pin 1
// datasheet p.190; F_OSC = 16 MHz & baud rate = 19.200

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

/*
*   Ophalen van gegevens die worden ontvangen
*/
unsigned char uart_receive(void) {
	while(!(UCSR0A & (1<<RXC0)));
	return UDR0;
}

void serialOut(char* Message){
	int i = 0;
	for(i=0; i < strlen(Message); i++){
		while ( !( UCSR0A & (1<<UDRE0)) );
		UDR0 = Message[i];
	}
}