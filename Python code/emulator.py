import time
import sys
from Utils import set_proc_name, Pointer, Ram, byte_to_reg_ids

set_proc_name("Casm_E")

global pc, data
rom = list(open(sys.argv[1],mode = "rb").read())
for i, byte in enumerate(rom):
    rom[i] = int(byte)
ram = Ram(16) #16kibs
reg = [0,0,0,0] #reg ids are aabbccdd, 2 bits for each
pc = Pointer(0)
input_mode = 0 #pointers become constants, 0=pointers, 1=constants

def jump():
    global pc, data
    data[data[-256] * -5 + 0] = pc % 255
    data[data[-256] * -5 + 1] = int(pc / 64) % 255
    data[data[-256] * -5 + 2] = int(pc / 64**2) % 255
    data[data[-256] * -5 + 3] = int(pc / 64**3) % 255
    data[data[-256] * -5 + 4] = int(pc / 64**4) % 255
    data[-256] = (data[-256] + 1) % 64
    pc = Pointer(data[pc + 1:pc + 6])
def _return():
    global pc, data
    data[-256] = (data[-256]-1) %64
    pc = Pointer(reversed(data[data[-256] * -5:data[-256] * -5 + 4]))
    data[data[-256] * -5 + 0] = 0
    data[data[-256] * -5 + 1] = 0
    data[data[-256] * -5 + 2] = 0
    data[data[-256] * -5 + 3] = 0
    data[data[-256] * -5 + 4] = 0
def read():
    global pc, data
    if input_mode == 0:
        inp = data[Pointer(data[pc+2:pc+8])]
        t = 8
    else:
        inp = data[pc+2]
        t = 3
    a,b,c,d = byte_to_reg_ids(data[pc+1])
    reg[a] = data[pc+1]
    print(f"{data[pc+1]} -> reg {a}")
    pc += t
def write():
    global pc, data
    if input_mode == 0:
        a,b,c,d = byte_to_reg_ids(data[pc+1])
        inp = reg[a]
    else:
        inp = data[pc+1]
    p = Pointer(data[pc+2:pc+8])
    data[p] = data[a]
    print(f"reg {a} -> {data[a]}")
    pc += 8
def compare():
    global pc, data
    if input_mode == 0:
        inp = Pointer(data[pc+7:pc+13])
        t = 13
    else:
        inp = data[pc+7]
        t = 8
    p1 = Pointer(data[pc+1:pc+7])
    if data[p1] == inp:
        pc += t
        print(f"{p1} == {inp}")
    else:
        pc+=t+1
        print(f"{p1} != {inp}")
def is_zero():
    global pc, data
    p1 = Pointer(data[pc+1:pc+7])
    if data[p1] == 0:
        pc += 7
        print(f"{p1} == 0")
    else:
        pc+=8
        print(f"{p1} != 0")
def reg_equals():
    global pc, data
    p1 = Pointer(data[pc+1:pc+7])
    if data[p1] == 0:
        pc += 7
        print(f"{p1} == 0")
    else:
        pc+=8
        print(f"{p1} != 0")
def reg_zero():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    if input_mode == 0:
        inp = reg[b]
        t = 13
    else:
        inp = data[pc+7]
        t = 8
    if reg[a] == inp:
        pc +=t+1
    else:
        pc +=t+2
def nop():
    pc+=1
def shift_left():
    global pc, data
    p1 = Pointer(data[pc+1:pc+7])
    a,b,c,d = byte_to_reg_ids(data[pc+7])
    reg[a] = int(data[p1]<<1)%256
    print(f"{data[p1]} << 1 -> reg {a}")
    pc += 8
def shift_right():
    global pc, data
    p1 = Pointer(data[pc+1:pc+7])
    a,b,c,d = byte_to_reg_ids(data[pc+7])
    reg[a] = int(data[p1]>>1)%256
    print(f"{data[p1]} >> 1 -> reg {a}")
    pc += 8
def add():
    global pc, data
    if input_mode == 0:
        inp = data[Pointer(data[pc+8:pc+14])]
        t = 13
    else:
        inp = data[pc+8]
        t = 8
    p1 = Pointer(data[pc+2:pc+8])
    a,b,c,d = byte_to_reg_ids(data[pc+1])
    reg[a] = int(data[p1]+inp)%255
    print(f"{data[p1]} + {inp} -> reg {a}")
    pc += t
def sub():
    global pc, data
    if input_mode == 0:
        inp = data[Pointer(data[pc+8:pc+14])]
        t = 13
    else:
        inp = data[pc+8]
        t = 8
    p1 = Pointer(data[pc+2:pc+8])
    a,b,c,d = byte_to_reg_ids(data[pc+1])
    reg[a] = int(data[p1]-inp)%255
    print(f"{data[p1]} - {inp} -> reg {a}")
    pc += t
def mul():
    global pc, data
    if input_mode == 0:
        inp = data[Pointer(data[pc+8:pc+14])]
        t = 13
    else:
        inp = data[pc+8]
        t = 8
    p1 = Pointer(data[pc+2:pc+8])
    a,b,c,d = byte_to_reg_ids(data[pc+1])
    reg[a] = int(data[p1]*inp)%255
    print(f"{data[p1]} * {inp} -> reg {a}")
    pc += t
def div():
    global pc, data
    if input_mode == 0:
        inp = data[Pointer(data[pc+8:pc+14])]
        t = 13
    else:
        inp = data[pc+8]
        t = 8
    p1 = Pointer(data[pc+2:pc+8])
    a,b,c,d = byte_to_reg_ids(data[pc+1])
    reg[a] = int(data[p1]/inp)%255
    print(f"{data[p1]} / {inp} -> reg {a}")
    pc += t
def add1():
    global pc
    reg[1] +=1
    print("reg1 += 1")
    pc+=1
def shift_left_reg():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    reg[b] = int(reg[a]<<1 % 256)
    print(f"reg {b} = reg {a} << 1")
    pc+=1
def shift_right_reg():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    reg[b] = int(reg[a]>>1 % 256)
    print(f"reg {b} = reg {a} >> 1")
    pc+=1
def add_reg():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    reg[c] = int((reg[a]+reg[b]) % 256)
    print(f"reg {c} = reg {a} + reg {b}")
    pc+=1
def sub_reg():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    reg[c] = int((reg[a]-reg[b]) % 256)
    print(f"reg {c} = reg {a} - reg {b}")
    pc+=1
def mul_reg():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    reg[c] = int((reg[a]*reg[b]) % 256)
    print(f"reg {c} = reg {a} * reg {b}")
    pc+=1
def div_reg():
    global pc, data
    a,b,c,d = byte_to_reg_ids(data[pc])
    reg[c] = int((reg[a]/reg[b]) % 256)
    print(f"reg {c} = reg {a} / reg {b}")
    pc+=1

#(name,<function object>,cycles)
opcode_map = {
    0x00: ("jump",            jump,            1),
    0x01: ("return",          _return,         1),
    0x02: ("exit",            exit,            1),
    0x03: ("read",            read,            1),
    0x04: ("write",           write,           1),
    0x05: ("compare",         compare,         1),
    0x06: ("is_zero",         is_zero,         1),
    0x07: ("reg_equals",      reg_equals,      1),
    0x08: ("reg_zero",        reg_zero,        1),
    0x09: ("nop",             nop,             1),
    0x10: ("shift_left",      shift_left,      1),
    0x11: ("shift_right",     shift_right,     1),
    0x12: ("add",             add,             1),
    0x13: ("sub",             sub,             1),
    0x14: ("mul",             mul,             1),
    0x15: ("div",             div,             1),
    0x16: ("add1",            add1,            1),
    0x1A: ("shift_left_reg",  shift_left_reg,  1),
    0x1B: ("shift_right_reg", shift_right_reg, 1),
    0x1C: ("add_reg",         add_reg,         1),
    0x1D: ("sub_reg",         sub_reg,         1),
    0x1E: ("mul_reg",         mul_reg,         1),
    0x1F: ("div_reg",         div_reg,         1),
}

while pc < (len(rom[0:2**14])+2**14): #max len of 16kib for rom + 16kib for ram
    print("\033[2J",end='')
    print("\033[0;0f",end='')
    
    data = rom[0:2**14+1] + ram

    if data[pc] in opcode_map:
        name, func, cycles = opcode_map.get(data[pc])
        print(f"{pc}{" "*(5-len(str(pc)))}: {name}")
    else:
        print(f"Unknown command: {data[pc]} at {pc}")
        exit()

    ram = data[-(2**14):]
    rom = data[:-(2**14+1)]
    time.sleep(0.1)