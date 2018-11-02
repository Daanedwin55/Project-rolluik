/*
 * LedBoardTest.c
 *
 * Created: 31-10-2018 15:19:58
 * Author : CreepCoder
 */ 

#define F_CPU 16E6
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRD = 1;
	
	void rolluikOmlaag() {
		PORTD &= ~(1 << PIND3); //LOW
		for(int i=0; i<10; i++) {
			PORTD |= (1 << PIND4); //HIGH
			_delay_ms(500);
			PORTD &= ~(1 << PIND4); //LOW
			_delay_ms(500);
		}
		PORTD |= (1 << PIND5); //HIGH
		_delay_ms(5000);
	}
	
	void rolluikOmhoog() {
		PORTD &= ~(1 << PIND5); //LOW
		for(int i=0; i<10; i++) {
			PORTD |= (1 << PIND4); //HIGH
			_delay_ms(500);
			PORTD &= ~(1 << PIND4); //LOW
			_delay_ms(500);
		}
		PORTD |= (1 << PIND3); //HIGH
		_delay_ms(5000);		
	}
	
	while (1)
	{
		rolluikOmlaag();
		rolluikOmhoog();
	}
}



