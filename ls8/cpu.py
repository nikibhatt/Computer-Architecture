"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.registers = [0,0,0,0,0,0,0,0]
        self.ram = [0] * 256

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        halted = False
        pc = 0

        while not halted:
            instruction = self.ram[pc]

            if instruction == 0b10000010:
                reg_num = self.ram[pc + 1]
                value = self.ram[pc + 2]
                self.registers[reg_num] = value
                pc += 3
            elif instruction == 0b01000111:
                reg_num = self.ram[pc + 1]
                print(self.registers[reg_num])
                pc += 2
            # elif instruction == ADD:
            #     reg_num_a = ram[pc + 1]
            #     reg_num_b = ram[pc + 2]
            #     registers[reg_num_a] += registers[reg_num_b]
            #     pc += 3
            elif instruction == 0b00000001:
                halted = True
            else:
                print(f'unknown instruction {instruction} at address {pc}')
                sys.exit(1)
