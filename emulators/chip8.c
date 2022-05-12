

// These notes were taken after reading this -> https://multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/

// -------------------
//       OPCODES 
// -------------------

// CHIP 8 has 35 opcodes that are 2 bytes long
// So let's use short which is 16bits or 2 bytes
unsigned short opcode;

// -------------------
//       MEMORY 
// -------------------
// CHIP 8 has 4k in memory
// C can represent this like this
unsigned char memory[4096];

// -------------------
//     REGISTERS 
// -------------------

// There are 16 * 8bit registers
// 15 are general purpose
// 1 is for carrying

unsigned char reg[16];

// index register and a program counter (PC)

unsigned short index;
unsigned short pc;


// -------------------
//     GRAPHICS 
// -------------------

// 2048 pixels
// each one is turned on/off by XORing
unsigned char gfx[64 * 32];

// -------------------
//       TIMERS
// -------------------

// RING THE BELL WHEN REACHING ZERO! 
unsigned char delay_timer;
unsigned char sound_timer;


// -------------------
//      STACK 
// -------------------

// used for storing the current location when performing a jump/subroutine
unsigned short stack[16];
unsigned short sp;

// -------------------
//       KEYS 
// -------------------

// HEX based keypad 0x0-0xF
unsigned char key[16];

