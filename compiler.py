import sys

def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = bytes(newname, "UTF-8")
    libc.prctl(15, byref(buff), 0, 0, 0)

set_proc_name('Casm Compiler')

def assembly_to_bin(assembly_code):
    # Define the opcode mapping for your assembly instructions.
    opcode_map = {
        "jump":             [0x00,'p'],
        "return":           [0x01],
        "exit":             [0x02],
        "read":             [0x03,'r','p,c'],
        "write":            [0x04,'r,c','p'],
        "compare":          [0x05,'r','p,c'],
        "is_zero":          [0x06,'p'],
        "reg_equals":       [0x07,'r','r,c'],
        "reg_zero":         [0x08,'r'],
        "nop":              [0x09],
        "shift_left":       [0x10,'p','r'],
        "shift_right":      [0x11,'p','r'],
        "add":              [0x12,'r','p','p,c'],
        "sub":              [0x13,'r','p','p,c'],
        "mul":              [0x14,'r','p','p,c'],
        "div":              [0x15,'r','p','p,c'],
        "add1":             [0x16],
        "shift_left_reg":   [0x1A,'r','r'],
        "shift_right_reg":  [0x1B,'r','r'],
        "add_reg":          [0x1C,'r','r','r'],
        "sub_reg":          [0x1D,'r','r','r'],
        "mul_reg":          [0x1E,'r','r','r'],
        "div_reg":          [0x1F,'r','r','r']
    }

    funcs = {}
    line_to_path=[]
    final = []
    
    # Helper function to convert a value into bytes
    def int_to_bytes(value, num_bytes=1):
        return [(value >> (8 * i)) & 0xFF for i in range(num_bytes)]
    
    # Helper function to convert a pointer to bytes
    def pointer_to_bytes(pointer:int, num_bytes=5):
        return pointer.to_bytes(5,'big')
    
    bin_code = []

    # Parse the assembly code and convert each instruction to machine code.
    for i, line in enumerate(assembly_code.splitlines()):
        line = line.strip()
        line_to_path.append(len(bin_code)-1)
        if not line or line.startswith(";"):  # Ignore comments and empty lines
            continue

        parts = line.split()
        instruction = parts[0]
        
        # Handle function definitions
        if instruction == 'def' and len(parts) >= 2:
            funcs[parts[1]] = len(bin_code)  # Store the function's location
            continue
        
        # Handle the run instruction (jump to a function)
        elif instruction == 'run':
            if len(parts) >= 2:
                if parts[1] in funcs:
                    bin_code.extend(int_to_bytes(opcode_map['jump'][0]))
                    bin_code.extend(pointer_to_bytes(funcs[parts[1]]))  # Jump to function
                    continue
                else:
                    print(f"Function {parts[1]} undefined.")
                    exit(3)
            else:
                print(f"Run is missing function, line {i}:\n{line}")
                exit(4)

        if instruction not in opcode_map:
            print(f"Unknown instruction: {instruction}")
            exit(1)
        
        # Handle regular instructions
        opcode = opcode_map[instruction][0]
        operands = parts[1:]

        # Start by adding the opcode
        instruction_bytes = int_to_bytes(opcode)

        # Handle operands (registers, pointers, immediate values)
        for i, operand in enumerate(operands):
            if operand.startswith(';'):
                break 
            elif any(element in operand for element in opcode_map[instruction][i+1].split(',')):
                if operand.startswith("r"):
                    instruction_bytes.extend(int_to_bytes(int(operand[1:]), 1))  # Register ID
                elif operand.startswith("pl"):
                    instruction_bytes.extend(pointer_to_bytes(int(operand[2:])))
                    final.append([len(instruction_bytes)-5+len(bin_code),int(operand[2:]),"line pointer"])
                elif operand.startswith("pr"):
                    instruction_bytes.extend(pointer_to_bytes(int(operand[2:])))
                    final.append([len(instruction_bytes)-5+len(bin_code),int(operand[2:]),"ram pointer"])
                elif operand.startswith("p"):
                    instruction_bytes.extend(pointer_to_bytes(int(operand[1:])))  # Pointer
                elif operand.startswith("c"):
                    instruction_bytes.extend(int_to_bytes(int(operand[1:])))
            else:
                print(f"Unrecognized operand: {operand}")
                exit(2)

        # Add this instruction to the binary code
        bin_code.extend(instruction_bytes)

    for byte, info, todo in final:
        if todo == "ram pointer":
            bin_code[byte:byte+6]=pointer_to_bytes(len(bin_code)+1+info)
        elif todo == "line pointer":
            print(info,line_to_path[info])
            bin_code[byte:byte+5]=pointer_to_bytes(line_to_path[info])

    return bin_code

def save_bin_to_file(bin_code, filename):
    with open(filename, "wb") as f:
        f.write(bytes(bin_code))
    print(f"Binary code saved to {filename}")

# Convert the assembly code to binary and save to file
bin_code = assembly_to_bin(open(sys.argv[1], 'r').read())
save_bin_to_file(bin_code, "".join(sys.argv[1].split('.')[:-1]) + ".bin")
