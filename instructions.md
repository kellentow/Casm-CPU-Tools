
## Control Flow Instructions

### **`jump`**  
-  **Opcode**: `0x00`  
-  **Description**: Jumps to the provided address, also adds current pointer to stack.  
-  **Operands**: Pointer (address to jump to).  
-  **Example**: `jump p72`, `jump lp6`.

### **`return`**  
-  **Opcode**: `0x01`  
-  **Description**: Goes to the pointer stack points to.  
-  **Operands**: None.  
-  **Example**: `return`.

### **`exit`**  
-  **Opcode**: `0x02`  
-  **Description**: Exits the program.  
-  **Operands**: None.  
-  **Example**: `exit`.

### **`nop`**
-  **Opcode**: `0x09`  
-  **Description**: Does literally nothing.  
-  **Operands**: None.  
-  **Example**: `nop`.

## Arithmetic Instructions

### **`add`**  
-  **Opcode**: `0x12`  
-  **Description**: Adds two values and stores the result in a register.  
-  **Operands**: pointer, pointer, register.  
-  **Example**: `add p90 p100 r1`.

### **`sub`**  
-  **Opcode**: `0x13`  
-  **Description**: Subtracts the second operand from the first and stores the result in a register.  
-  **Operands**: pointer, pointer, register.  
-  **Example**: `sub p9 p200 r1`.

### **`mul`**  
-  **Opcode**: `0x14`  
-  **Description**: Multiplies two operands and stores the result in a register.  
-  **Operands**: pointer, pointer, register.  
-  **Example**: `mul p7 p80 r1`.

### **`div`**  
-  **Opcode**: `0x15`  
-  **Description**: Divides the first operand by the second and stores the result in a register.  
-  **Operands**: pointer, pointer, register.  
-  **Example**: `div p1 p770 r1`.

### **`add_reg`**  
-  **Opcode**: `0x12`  
-  **Description**: Adds two values and stores the result in a register.  
-  **Operands**: register, register, register.  
-  **Example**: `add_reg r1 r2 r3`.

### **`sub_reg`**  
-  **Opcode**: `0x13`  
-  **Description**: Subtracts the second operand from the first and stores the result in a register.  
-  **Operands**: register, register, register.  
-  **Example**: `sub_reg r1 r2 r3`.

### **`mul_reg`**  
-  **Opcode**: `0x14`  
-  **Description**: Multiplies two operands and stores the result in a register.  
-  **Operands**: register, register, register.  
-  **Example**: `mul_reg r1 r2 r3`.

### **`div_reg`**  
-  **Opcode**: `0x15`  
-  **Description**: Divides the first operand by the second and stores the result in a register.  
-  **Operands**: register, register, register.  
-  **Example**: `div_reg r1 r2 r3`.

### **`add1`**  
-  **Opcode**: `0x16`  
-  **Description**: Adds 1 to reg 0, useful for writing with no set up registers  
-  **Operands**: None.  
-  **Example**: `add1`.

## Shift Instructions

### **`shift_left`**  
-  **Opcode**: `0x10`  
-  **Description**: Shifts the value of a register left by 1 bit.
-  **Operands**: pointer, Register.  
-  **Example**: `shift_left p100 r1`.

### **`shift_right`**  
-  **Opcode**: `0x11`  
-  **Description**: Shifts the value of a register right 1 bit.  
-  **Operands**: pointer, Register.  
-  **Example**: `shift_right p100 r1`.

### **`shift_left_reg`**  
-  **Opcode**: `0x1A`  
-  **Description**: Shifts the value of a register left by 1 bit.  
-  **Operands**: Register, Register.  
-  **Example**: `shift_left_reg r1 r1`.

### **`shift_right_reg`**  
-  **Opcode**: `0x1B`  
-  **Description**: Shifts the value of a register right by 1 bit.  
-  **Operands**: Register, Register.  
-  **Example**: `shift_right_reg r1 r1`.

## Comparison Instructions

### **`compare`**  
-  **Opcode**: `0x05`  
-  **Description**: Compares two values and if equal runs the next line, otherwise skips.  
-  **Operands**: pointer, pointer.  
-  **Example**: `read p100 p1`.

### **`is_zero`**  
-  **Opcode**: `0x06`  
-  **Description**: Checks if the value at a pointer is zero, if not skips the next line.  
-  **Operands**: pointer.  
-  **Example**: `is_zero r1`.

### **`reg_equals`**  
-  **Opcode**: `0x07`  
-  **Description**: checks if two reqs are equal and runs the next line, otherwise skips.  
-  **Operands**: Register, Register.  
-  **Example**: `reg_equals r1 r2`.

### **`reg_zero`**  
-  **Opcode**: `0x08`  
-  **Description**: Checks if a register is zero, if not skips the next line.  
-  **Operands**: Register.  
-  **Example**: `reg_zero r1`.

## Input/Output Instructions

### **`read`**  
-  **Opcode**: `0x03`  
-  **Description**: Reads data into a register.  
-  **Operands**: Pointer, Register.  
-  **Example**: `read p100 r1`.

### **`write`**  
-  **Opcode**: `0x04`  
-  **Description**: Writes data from a register to memory.  
-  **Operands**: Pointer, Register.  
-  **Example**: `write p100 r1`.