
# Casm Assembly Language Documentation

**Casm** is a low-level assembly language designed for programming a custom CPU architecture. The language features basic operations, conditional jumps, function definitions, and custom operations like arithmetic and bitwise shifts.

## Table of Contents
1. [Introduction](#introduction)
2. [Instructions](#instructions)
   - [Control Flow Instructions](#control-flow-instructions)
   - [Arithmetic Instructions](#arithmetic-instructions)
   - [Shift Instructions](#shift-instructions)
   - [Comparison Instructions](#comparison-instructions)
   - [Input/Output Instructions](#input-output-instructions)
   - [Function Definitions](#function-definitions)
3. [Operands](#operands)
4. [Creating Binaries](#creating-binaries)
5. [Examples](#examples)

---

## Introduction

Casm is designed to provide a simple yet powerful assembly language for custom CPU implementations. The language allows direct manipulation of registers, memory, and control flow to achieve a variety of tasks, such as computation, input/output operations, and conditional execution.

---

## Instructions

### Control Flow Instructions

- **`jump`**  
  **Opcode**: `0x00`  
  **Description**: Jumps to the provided address.  
  **Operands**: Pointer (address to jump to).  
  **Example**: `jump p72`, `jump lp6`.

- **`return`**  
  **Opcode**: `0x01`  
  **Description**: Returns from the current function (if inside a function).  
  **Operands**: None.  
  **Example**: `return`.

- **`exit`**  
  **Opcode**: `0x02`  
  **Description**: Exits the program.  
  **Operands**: None.  
  **Example**: `exit`.

### Arithmetic Instructions

- **`add`**  
  **Opcode**: `0x12`  
  **Description**: Adds two values and stores the result in a register.  
  **Operands**: pointer, pointer, register.  
  **Example**: `add p90 p100 r1`.

- **`sub`**  
  **Opcode**: `0x13`  
  **Description**: Subtracts the second operand from the first and stores the result in a register.  
  **Operands**: pointer, pointer, register.  
  **Example**: `sub p9 p200 r1`.

- **`mul`**  
  **Opcode**: `0x14`  
  **Description**: Multiplies two operands and stores the result in a register.  
  **Operands**: pointer, pointer, register.  
  **Example**: `mul p7 p80 r1`.

- **`div`**  
  **Opcode**: `0x15`  
  **Description**: Divides the first operand by the second and stores the result in a register.  
  **Operands**: pointer, pointer, register.  
  **Example**: `div p1 p770 r1`.

- **`add_reg`**  
  **Opcode**: `0x12`  
  **Description**: Adds two values and stores the result in a register.  
  **Operands**: register, register, register.  
  **Example**: `add_reg r1 r2 r3`.

- **`sub_reg`**  
  **Opcode**: `0x13`  
  **Description**: Subtracts the second operand from the first and stores the result in a register.  
  **Operands**: register, register, register.  
  **Example**: `sub_reg r1 r2 r3`.

- **`mul_reg`**  
  **Opcode**: `0x14`  
  **Description**: Multiplies two operands and stores the result in a register.  
  **Operands**: register, register, register.  
  **Example**: `mul_reg r1 r2 r3`.

- **`div_reg`**  
  **Opcode**: `0x15`  
  **Description**: Divides the first operand by the second and stores the result in a register.  
  **Operands**: register, register, register.  
  **Example**: `div_reg r1 r2 r3`.

- **`add1`**  
  **Opcode**: `0x16`  
  **Description**: Adds 1 to reg 0, useful for writing with no set up registers  
  **Operands**: None.  
  **Example**: `add1`.

### Shift Instructions

- **`shift_left`**  
  **Opcode**: `0x10`  
  **Description**: Shifts the value of a register left by 1 bit.
  **Operands**: pointer, Register.  
  **Example**: `shift_left p100 r1`.

- **`shift_right`**  
  **Opcode**: `0x11`  
  **Description**: Shifts the value of a register right 1 bit.  
  **Operands**: pointer, Register.  
  **Example**: `shift_right p100 r1`.

- **`shift_left_reg`**  
  **Opcode**: `0x1A`  
  **Description**: Shifts the value of a register left by 1 bit.  
  **Operands**: Register, Register.  
  **Example**: `shift_left_reg r1 r1`.

- **`shift_right_reg`**  
  **Opcode**: `0x1B`  
  **Description**: Shifts the value of a register right by 1 bit.  
  **Operands**: Register, Register.  
  **Example**: `shift_right_reg r1 r1`.

### Comparison Instructions

- **`compare`**  
  **Opcode**: `0x05`  
  **Description**: Compares two values and if equal runs the next line, otherwise skips.  
  **Operands**: pointer, pointer.  
  **Example**: `read p100 p1`.

- **`is_zero`**  
  **Opcode**: `0x06`  
  **Description**: Checks if the value at a pointer is zero, if not skips the next line.  
  **Operands**: pointer.  
  **Example**: `is_zero r1`.

- **`reg_equals`**  
  **Opcode**: `0x07`  
  **Description**: checks if two reqs are equal and runs the next line, otherwise skips.  
  **Operands**: Register, Register.  
  **Example**: `reg_equals r1 r2`.

- **`reg_zero`**  
  **Opcode**: `0x08`  
  **Description**: Checks if a register is zero, if not skips the next line.  
  **Operands**: Register.  
  **Example**: `reg_zero r1`.

### Input/Output Instructions

- **`read`**  
  **Opcode**: `0x03`  
  **Description**: Reads data into a register.  
  **Operands**: Pointer, Register.  
  **Example**: `read p100 r1`.

- **`write`**  
  **Opcode**: `0x04`  
  **Description**: Writes data from a register to memory.  
  **Operands**: Pointer, Register.  
  **Example**: `write p100 r1`.

---

## Operands

Casm uses several types of operands:

- **Registers**: Denoted by `rX`, where `X` is the register number (e.g., `r0`, `r1`).
- **Pointers**: Denoted by `pX`, where `X` is the address (e.g., `p10`).
- **Line Pointers**: Denoted by `plX`, where `X`is the line number (e.g., `pl4`, `pl7`)
- **Ram Pointers**: Denoted by `prX`, where `X`is the address starting in ram (e.g., `pr70`, `pr8`)
- **Labels/Functions**: Functions are defined with the `def` keyword, and run instructions can target them.
  
Operands for instructions must be provided in the correct order as per the instruction format.

---

## Creating Binaries

To compile your Casm code into binary form, use the following Python script:

```bash
python3 compiler.py <filename>
```

This will take the Casm source code file, convert it to binary, and save it with a `.bin` extension.

---

## Examples

### Example 1: Simple Addition

```casm
add r0 r1 r2
```
This instruction adds the values in `r0` and `r1` and stores the result in `r2`.

### Example 2: Function Definition and Call

```casm
def my_function
    add r0 r1 r2
    return

run my_function
```

This code defines a function `my_function` that adds `r0` and `r1`, stores the result in `r2`, and then returns. The `run` instruction calls `my_function`.

---

For more information, consult the [Casm source code](./compiler.py).
