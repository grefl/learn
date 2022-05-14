



#---------------------
#      OPCODES
#---------------------

OPCODE = None

#---------------------
#      MEMORY 
#---------------------

memory = bytearray(4096)


#---------------------
#      Registers 
#---------------------

reg = bytearray(16)

index = None
pc    = None 



#---------------------
#      GRAPHICS 
#---------------------



gfx = bytearray(64*32)





#---------------------
#       TIMERS 
#---------------------

delay_timer = None
sound_timer = None


stack = bytearray(16*2)
sp    = None
