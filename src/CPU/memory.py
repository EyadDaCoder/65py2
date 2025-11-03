Memory = bytearray(65536)
# 0x0000 - 0x00FF = Zero Page
# 0x0100 - 0x01FF = Stack
# 0x0200 - 0x03FF = Video
# 0x0400 - 0xFFFF = Program

register_pc = 0x0400
register_sp = 0xFF
register_a = 0x00
register_x = 0x00
register_y = 0x00

flag_break = 0
flag_carry = 0
flag_negative = 0
flag_zero = 0

Memory[0x0401] = 0x00

emu_flag_hold_cycle = False
emu_flag_hold_instruction_fetch = False