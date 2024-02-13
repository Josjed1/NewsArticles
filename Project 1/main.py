import sys
import struct


instructions = [None ] * 500 
address =  [None ] * 500
imm = [None ] * 500
op = [None ] * 500
valid = [None ] * 500
def dissassemble():
    if len(sys.argv) != 2:
        print("Usage: python main.py <binary_file>")
        sys.exit(1)

    inFile = open(sys.argv[1], 'rb')
    
    print (sys.argv)

    addr = 96

    while True :
            bitsInStrForm = inFile.read(4)
            if len( bitsInStrForm) == 0 :
                print("End of file reached.")
                break

            address[addr] = addr 

            instructions[addr] =  struct.unpack('>I', bitsInStrForm)[0] 
            
            # go ahead and get the 16 bit IMM out form the binary
            # this is the easiest way to do it.
            imm[ addr ]   = struct.unpack('>h', bitsInStrForm[2:4])[0]

            # use I to hold the current instruction
            I = instructions[ addr ]
            # get IMMEDIATE bits

            # get the opcode bits
            op[addr] = I>>26

            binstr = bin(I)
            print (binstr, op[ addr])
            addr += 4
            
    inFile.close()
    # Dissassembly finished


### This is where it starts the Simulation and Prints 
def simulate():
    registers = [0] * 32
    memory = [0] * 1024
    addr = 96
    pc = 96
    i = 1

    while addr < len(instructions):
        instruction = instructions[addr]
        op_val = op[addr]

        print("====================")
        print("cycle: {}".format(i), "{} {}".format(addr, instruction))
        print("registers:")

        for reg in range(0, 32, 8):
            print("r{:02d}: {} {} {} {} {} {} {} {}".format(
                reg, *registers[reg:reg + 8]))

        print("data:")
        print("{}: {} {} {} {}".format(i, *memory[i:i + 4]))

        print("====================")

        if op_val == 0:  # R-type instruction
            funct = instruction & 0x3F
            if funct == 32:  # ADD instruction
                rs = (instruction >> 21) & 0x1F
                rt = (instruction >> 16) & 0x1F
                rd = (instruction >> 11) & 0x1F
                registers[rd] = registers[rs] + registers[rt]

        elif op_val == 8:  # I-type instruction (ADDI)
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            imm_val = imm[addr]
            registers[rt] = registers[rs] + imm_val

        elif op_val == 35:  # I-type instruction (LW)
            rs = (instruction >> 21) & 0x1F
            rt = (instruction >> 16) & 0x1F
            imm_val = imm[addr]
            address = registers[rs] + imm_val
            registers[rt] = memory[address]
        if addr > 152:
            return
        addr += 4
        i += 1
        

if __name__ == '__main__':
    dissassemble()
    simulate()

