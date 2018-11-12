#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>
#include <stdlib.h>
#include <inttypes.h>

#include "rolluik_controls.h"
#include "adc_controls.h"
#include "uart_control.h"
#include "ultrasonor.h"

uint8_t identifier = 101;

/*
*   Haal de waarde op en zet de waarde op het scherm via een seriële monitor
*/
void lichtintensiteit() {
	uint16_t licht = get_adc_value(A1);
	char temp[7];
	itoa(licht, temp, 10); // Zet de gevonden int waarde om in een ASCII waarde
	serialOut(temp);
}

void temperatuur() {
	uint8_t temperatuurv = get_adc_value(A0);
	char temp[7];
	itoa(temperatuurv, temp, 10); // Zet de gevonden int waarde om in een ASCII waarde
	serialOut(temp);
}

void stat() {
	char temp[7];
	itoa(status, temp, 10); // Zet de gevonden int waarde om in een ASCII waarde
	serialOut(temp);
}

void afstand() {
	PORTC |= (1<<PC4);		// Zet trigger hoog
	_delay_us(10);			// voor 10uS
	PORTC &= ~(1<<PC4);		// zodat je de ultrasoonsensor triggert
}

void ident() {
	char temp[7];
	itoa(identifier, temp, 10); // Zet de gevonden int waarde om in een ASCII waarde
	serialOut(temp);
}

/*
*   Luister naar welke commando er wordt verstuurd, vang deze op en geef de juiste data terug
*/
void get_command() {
	uint8_t command = uart_recive();
	switch(command) {

		case 0x74: //temp t
		temperatuur();
		break;
		
		case 0x73: //status s
		stat();
		break;
		
		case 0x6C: //light l
		lichtintensiteit();
		break;
		
		case 0x64: //distance d
		afstand();
		break;
		
		case 0x65: //identifier e
		ident();
		break;
		
		case 0x68: //up h
		omhoog();
		break;
		
		case 0x67: //down g
		omlaag();
		break;
	}
}

/*
*   Statuslampje voor de rolluiken
*/
void statuslamp() {
	if(get_adc_value(A1) >= 60 && status == OMHOOG) {
		omlaag();
		status = OMLAAG;	
	}
	else if(get_adc_value(A1) < 60 && status == OMLAAG) {
		omhoog();
		status = OMHOOG;
	}
}

int main(void)
{
	DDRD = 0b00111000; //Zet outputs goed (pin 4-6)
	uart_init(); // Initialiseer UART communicatie
	ultrasoon_init();

	while (1) {
		get_command();
	}
}