import CPU.memory

import subprocess

while CPU.memory.flag_break == 0:
    CPU.memory.register_pc += 1
    subprocess.run(['python', f'instruction_set\\{CPU.memory.Memory[CPU.memory.register_pc]}.py'], capture_output=False, text=True)
