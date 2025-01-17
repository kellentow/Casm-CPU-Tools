import sys
from Utils import set_proc_name, Pointer

set_proc_name('Casm Compiler')

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

def assembly_to_bin(assembly_code,verbose=True):
    funcs = {}
    line_to_path=[]
    final = []
    
    # Helper function to convert a value into bytes
    def int_to_bytes(value, num_bytes=1):
        return [(value >> (8 * i)) & 0xFF for i in range(num_bytes)]
    
    bin_code = []
    if verbose:
        print("Reading code")
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
                    bin_code.extend(Pointer(funcs[parts[1]]))  # Jump to function
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
        for i in range(len(opcode_map[instruction][1:])):
            operand = operands[i]
            if operand.startswith(';'):
                break 
            elif any(element in operand for element in opcode_map[instruction][i+1].split(',')):
                if operand.startswith("r"):
                    instruction_bytes.extend(int_to_bytes(int(operand[1:]), 1))  # Register ID
                elif operand.startswith("pl"):
                    instruction_bytes.extend(Pointer(int(operand[2:])))
                    final.append([len(instruction_bytes)-5+len(bin_code),int(operand[2:]),"line pointer"])
                elif operand.startswith("pr"):
                    instruction_bytes.extend(Pointer(int(operand[2:])))
                    final.append([len(instruction_bytes)-5+len(bin_code),int(operand[2:]),"ram pointer"])
                elif operand.startswith("p"):
                    instruction_bytes.extend(Pointer(int(operand[1:])))  # Pointer
                elif operand.startswith("c"):
                    instruction_bytes.extend(Pointer(int(operand[1:])))
            else:
                print(f"Unrecognized operand: {operand}")
                exit(2)

        # Add this instruction to the binary code
        bin_code.extend(instruction_bytes)

    if verbose:
        print("Doing last look over")

    try:
        for byte, info, todo in final:
            if todo == "ram pointer":
                try:
                    bin_code[byte:byte+6]=bytes(Pointer(len(bin_code)+1+info))
                except Exception as _:
                    try:
                        print(f"Failed to create Ram pointer, near line {line_to_path.index(byte)}")
                        exit(7)
                    except ValueError:
                        print("Failed to create Ram pointer, Could not get line number")
                        exit(8)
            elif todo == "line pointer":
                try:
                    bin_code[byte:byte+5]=bytes(Pointer(line_to_path[info]))
                except KeyError():
                    print(f'Could not find line {info}')
                    exit(6)
    except Exception as e:
        import datetime
        filename = "error-"+str(datetime.date.today)
        print("An error occured please send file {filename} to https://github.com/kellentow/Casm-CPU-Tools/issues")
        try:
            with open(filename,'w') as f:
                f.write(str(e))
            exit(5)
        except Exception as r:
            print("another error occured while making error log, printing both errors")
            print(e)
            print(r)
            exit(9)

    if verbose:
        print("Binary Generated")

    return bin_code

def save_bin_to_file(bin_code, filename):
    with open(filename, "wb") as f:
        f.write(bytes(bin_code))
    print(f"Binary saved to {filename}")


if __file__ == "__main__":
    try:
        open(sys.argv[1], 'r').close()
    except Exception as _:
        print("Failed to read file, file may not exist or you don't have permission to read it")
        exit(10)

    # Convert the assembly code to binary and save to file
    bin_code = assembly_to_bin(open(sys.argv[1], 'r').read())
    save_bin_to_file(bin_code, "".join(sys.argv[1].split('.')[:-1]) + ".bin")
