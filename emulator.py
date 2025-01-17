import time
import sys
from Utils import set_proc_name, Pointer

set_proc_name("Casm Emulator")

rom = list(open(sys.argv[1],mode = "rb").read())
for i, byte in enumerate(rom):
    rom[i] = int(byte)
ram = [0]*(2**14) #16kibs
reg = [0,0,0,0] #reg ids are aabbccdd

def byte_to_reg_ids(byte):
    a = (byte >> 6) & 0b11
    b = (byte >> 4) & 0b11
    c = (byte >> 2) & 0b11
    d = byte & 0b11
    return [a,b,c,d]
def bytes_to_pointer(bytes):
    return int.from_bytes(bytes,'big')

pc = Pointer(0)
input_mode = 0 #pointers become constants, 0=pointers, 1=constants
while pc < (len(rom[0:2**14])+2**12): #max len of 16kib for rom + 16kib for ram
    print("\033[2J",end='')
    print("\033[0;0f",end='')
    
    data = rom[0:2**14+1] + ram
    match data[pc]:
        case 0:   #/x00  |  jump
            data[data[-256] * -5 + 0] = pc % 255
            data[data[-256] * -5 + 1] = int(pc / 64) % 255
            data[data[-256] * -5 + 2] = int(pc / 64**2) % 255
            data[data[-256] * -5 + 3] = int(pc / 64**3) % 255
            data[data[-256] * -5 + 4] = int(pc / 64**4) % 255
            data[-256] = (data[-256] + 1) % 64
            pc = bytes_to_pointer(data[pc + 1:pc + 6])
            print(f"Jumping to: {pc}")
        case 1:   #/x01  |  return
            data[-256] = (data[-256]-1) %64
            pc = bytes_to_pointer(reversed(data[data[-256] * -5:data[-256] * -5 + 4]))
            print(f"Returning to: {pc}")
            data[data[-256] * -5 + 0] = 0
            data[data[-256] * -5 + 1] = 0
            data[data[-256] * -5 + 2] = 0
            data[data[-256] * -5 + 3] = 0
            data[data[-256] * -5 + 4] = 0
        case 2:   #/x02  |  exit
            print("exiting")
            exit()
        case 3:   #/x03  |  read to reg
            if input_mode == 0:
                inp = data[bytes_to_pointer(data[pc+2:pc+8])]
                t = 8
            else:
                inp = data[pc+2]
                t = 3
            a,b,c,d = byte_to_reg_ids(data[pc+1])
            reg[a] = data[pc+1]
            print(f"{data[pc+1]} -> reg {a}")
            pc += t
        case 4:   #/x04  |  write from reg
            if input_mode == 0:
                a,b,c,d = byte_to_reg_ids(data[pc+1])
                inp = reg[a]
            else:
                inp = data[pc+1]
            p = bytes_to_pointer(data[pc+2:pc+8])
            data[p] = data[a]
            print(f"reg {a} -> {data[a]}")
            pc += 8
        case 5:   #/x05  |  is data[pc+1:pc+4] == data[pc+5]
            if input_mode == 0:
                inp = bytes_to_pointer(data[pc+7:pc+13])
                t = 13
            else:
                inp = data[pc+7]
                t = 8
            p1 = bytes_to_pointer(data[pc+1:pc+7])
            if data[p1] == inp:
                pc += t
                print(f"{p1} == {inp}")
            else:
                pc+=t+1
                print(f"{p1} != {inp}")
        case 6:   #/x06  |  is data[pc+1:pc+4] == 0
            p1 = bytes_to_pointer(data[pc+1:pc+7])
            if data[p1] == 0:
                pc += 7
                print(f"{p1} == 0")
            else:
                pc+=8
                print(f"{p1} != 0")
        case 7:   #/x07  |  is reg[a] == reg[b]
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
        case 8:   #/x08  |  is reg[a] == 0
            a,b,c,d = byte_to_reg_ids(data[pc])
            if reg[a] == 0:
                pc +=1
            else:
                pc +=2
        case 9:   #/x09  |  nop
            print("nop")
            pc+=1
        case 16:  #/x10  |  l bitshift
            p1 = bytes_to_pointer(data[pc+1:pc+7])
            a,b,c,d = byte_to_reg_ids(data[pc+7])
            reg[a] = int(data[p1]<<1)%256
            print(f"{data[p1]} << 1 -> reg {a}")
            pc += 8
        case 17:  #/x11  |  r bitshift
            p1 = bytes_to_pointer(data[pc+1:pc+7])
            a,b,c,d = byte_to_reg_ids(data[pc+7])
            reg[a] = int(data[p1]>>1)%256
            print(f"{data[p1]} >> 1 -> reg {a}")
            pc += 8
        case 18:  #/x12  |  add
            if input_mode == 0:
                inp = data[bytes_to_pointer(data[pc+8:pc+14])]
                t = 13
            else:
                inp = data[pc+8]
                t = 8
            p1 = bytes_to_pointer(data[pc+2:pc+8])
            a,b,c,d = byte_to_reg_ids(data[pc+1])
            reg[a] = int(data[p1]+inp)%255
            print(f"{data[p1]} + {inp} -> reg {a}")
            pc += t
        case 19:  #/x13  |  sub
            if input_mode == 0:
                inp = data[bytes_to_pointer(data[pc+8:pc+14])]
                t = 13
            else:
                inp = data[pc+8]
                t = 8
            p1 = bytes_to_pointer(data[pc+2:pc+8])
            a,b,c,d = byte_to_reg_ids(data[pc+1])
            reg[a] = int(data[p1]-inp)%255
            print(f"{data[p1]} - {inp} -> reg {a}")
            pc += t
        case 20:  #/x14  |  mult
            if input_mode == 0:
                inp = data[bytes_to_pointer(data[pc+8:pc+14])]
                t = 13
            else:
                inp = data[pc+8]
                t = 8
            p1 = bytes_to_pointer(data[pc+2:pc+8])
            a,b,c,d = byte_to_reg_ids(data[pc+1])
            reg[a] = int(data[p1]*inp)%255
            print(f"{data[p1]} * {inp} -> reg {a}")
            pc += t
        case 21:  #/x15  |  div
            if input_mode == 0:
                inp = data[bytes_to_pointer(data[pc+8:pc+14])]
                t = 13
            else:
                inp = data[pc+8]
                t = 8
            p1 = bytes_to_pointer(data[pc+2:pc+8])
            a,b,c,d = byte_to_reg_ids(data[pc+1])
            reg[a] = int(data[p1]/inp)%255
            print(f"{data[p1]} / {inp} -> reg {a}")
            pc += t
        case 22:  #/x16  |  add 1 to reg1
            reg[1] +=1
            print("reg1 += 1")
            pc+=1
        case 26:  #/x1A  |  L bit shift reg
            a,b,c,d = byte_to_reg_ids(data[pc])
            reg[b] = int(reg[a]<<1 % 256)
            print(f"reg {b} = reg {a} << 1")
            pc+=1
        case 27:  #/x1B  |  R bit shift reg
            a,b,c,d = byte_to_reg_ids(data[pc])
            reg[b] = int(reg[a]>>1 % 256)
            print(f"reg {b} = reg {a} >> 1")
            pc+=1
        case 28:  #/x1C  |  add reg
            a,b,c,d = byte_to_reg_ids(data[pc])
            reg[c] = int((reg[a]+reg[b]) % 256)
            print(f"reg {c} = reg {a} + reg {b}")
            pc+=1
        case 29:  #/x1D  |  sub reg
            a,b,c,d = byte_to_reg_ids(data[pc])
            reg[c] = int((reg[a]-reg[b]) % 256)
            print(f"reg {c} = reg {a} - reg {b}")
            pc+=1
        case 30:  #/x1E  |  mult reg
            a,b,c,d = byte_to_reg_ids(data[pc])
            reg[c] = int((reg[a]*reg[b]) % 256)
            print(f"reg {c} = reg {a} * reg {b}")
            pc+=1
        case 31:  #/x1F  |  div reg
            a,b,c,d = byte_to_reg_ids(data[pc])
            reg[c] = int((reg[a]/reg[b]) % 256)
            print(f"reg {c} = reg {a} / reg {b}")
            pc+=1
        case _: #err, unimplimented
            print(f"Unknown command: {data[pc]} at {pc}")
    ram = data[-(2**12):]
    rom = data[:-(2**12+1)]
    time.sleep(0.1)

# todo: Fully implimented!!!