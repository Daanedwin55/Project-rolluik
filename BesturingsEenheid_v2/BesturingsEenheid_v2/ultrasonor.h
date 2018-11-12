/*
 *      Pin placement of ATMega328p:
 *      Pin PC4				HC-SR04 Trig
 *      Pin PC5				HC-SR04 Echo
 */
#include <avr/interrupt.h>

// Initialiseer de poorten voor de ultrasoonsensor en initialiseer de interrupt
void ultrasoon_init() {
	DDRC = 0b11111000;						// Port C all output. PC0: RW		PC1: RS		PC2: E
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

// Interrupt methode die wordt uitgevoerd wanneer er een echo plaatsvind op de sensor (die staat op PC5/A5)
ISR(PCINT1_vect) {
	if (bit_is_set(PINC,PC5)) {				// Checks if echo is high
		TCNT1 = 0;							// Reset Timer
		PORTC |= (1<<PC3);
		} 
		
	else {
		uint16_t numuS = TCNT1;				// Save Timer value
		uint8_t oldSREG = SREG;
		cli();

		uint16_t uitkomst = (numuS*0.034/2)/15;
		char temp[7];
		itoa(uitkomst, temp, 10);			// Zet de gevonden int waarde om in een ASCII waarde
		serialOut(temp);

		SREG = oldSREG;						// Enable interrupts
	}
}