
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
<table style="table-layout: fixed; width: 140.25ex; border: 1; text-align: center;">
  <tr style="height: 8.25ex;">
    <th>x/XY</th>
    <th>0Y</th>
    <th>1Y</th>
    <th>2Y</th>
    <th>3Y</th>
    <th>4Y</th>
    <th>5Y</th>
    <th>6Y</th>
    <th>8Y</th>
    <th>9Y</th>
    <th>AY</th>
    <th>BY</th>
    <th>CY</th>
    <th>DY</th>
    <th>EY</th>
    <th>FY</th>
  </tr>
  <tr style="height: 8.25ex;">
    <th>X0</th>
    <td><a href="./instructions.md#jump">Jump</a></td>
    <td><a href="./instructions.md#return">Return</a></td>
    <td><a href="./instructions.md#exit">Exit</a></td>
    <td><a href="./instructions.md#read">Read</a></td>
    <td><a href="./instructions.md#write">Write</a></td>
    <td><a href="./instructions.md#compare">P==P?</a></td>
    <td><a href="./instructions.md#is_zero">P==0?</a></td>
    <td><a href="./instructions.md#reg_equals">R==R</a></td>
    <td><a href="./instructions.md#req_zero">P==0?</a></td>
    <td><a href="./instructions.md#nop">Nop</a></td>
    <td><a href="./instructions.md">None</a></td>
    <td><a href="./instructions.md">None</a></td>
    <td><a href="./instructions.md">None</a></td>
    <td><a href="./instructions.md">None</a></td>
    <td><a href="./instructions.md">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>X1</th>
    <td><a href="./instructions.md#shift_left">Left bitshft</a></td>
    <td><a href="./instructions.md#shift_right">Right bitshft</a></td>
    <td><a href="./instructions.md#add">Add</a></td>
    <td><a href="./instructions.md#sub">Sub</a></td>
    <td><a href="./instructions.md#mult">Mult</a></td>
    <td><a href="./instructions.md#div">Div</a></td>
    <td><a href="./instructions.md#add1">Reg1 += 1</a></td>
    <td><a href="./instructions.md">None</a></td>
    <td><a href="./instructions.md">None</a></td>
    <td><a href="./instructions.md#shift_left_reg">Reg left shft</a></td>
    <td><a href="./instructions.md#shift_right_reg">Reg right shft</a></td>
    <td><a href="./instructions.md#add_reg">Reg add</a></td>
    <td><a href="./instructions.md#sub_reg">Reg Sub</a></td>
    <td><a href="./instructions.md#mult_reg">Reg Mult</a></td>
    <td><a href="./instructions.md#div_reg">Reg Div</a></td>
  </tr>
  <!--<tr style="height: 8.25ex;">
    <th>X2</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
   <tr style="height: 8.25ex;">
    <th>X3</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>X4</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>X5</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
   <tr style="height: 8.25ex;">
    <th>X6</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>X7</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>X8</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
   <tr style="height: 8.25ex;">
    <th>X9</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>XA</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>XB</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
   <tr style="height: 8.25ex;">
    <th>XC</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>XD</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>XE</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr>
  <tr style="height: 8.25ex;">
    <th>XF</th>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
    <td><a href="./instructions.md#jump">None</a></td>
  </tr> -->
</table>

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
