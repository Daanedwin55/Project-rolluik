/*
*   Associeer waarden 1 en 0 met omhoog en omlaag gaan van het rolluik
*/
#define OMHOOG 1
#define OMLAAG 0
uint8_t status = OMHOOG;

/*
*   Functie om gemakkelijker een poort aan te sturen
*/

void pind_high(uint8_t pin) {
	PORTD |= (1 << pin); //HIGH
}

void pind_low(uint8_t pin) {
	PORTD &= ~(1 << pin); //LOW
}

/*
*   Rolluik controls
*/

void midden() {
	for(int i=0; i<7; i++) {
		pind_high(PIND4);
		_delay_ms(500);
		pind_low(PIND4);
		_delay_ms(250);
	}
}

void omhoog() {
	if(status == OMLAAG) {
		pind_low(PIND5);
		midden();
		pind_high(PIND3);
		status = OMHOOG;
	}
}

void omlaag() {
	if(status == OMHOOG) {
		pind_low(PIND3);
		midden();
		pind_high(PIND5);
		status = OMLAAG;
	}
}