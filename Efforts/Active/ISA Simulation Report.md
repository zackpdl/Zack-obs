**Name:** Puran Paodensakul  
**ID:** 6611140  
**Section:** 542

---

## Introduction

An **Instruction Set Architecture (ISA)** defines the interface between software and hardware in a computer system. It specifies the set of instructions a processor can execute, such as arithmetic operations and data movement.

This report documents a simplified **32-bit ISA simulator implemented in Python**. The simulator:

- Reads instructions from user input
    
- Executes them sequentially
    
- Tracks register state
    
- Calculates total cycles, instruction count, and **CPI (Cycles Per Instruction)**
    

---

## System Architecture

The simulator models a minimal CPU with:

- Registers only (no memory)
    
- Fixed instruction set
    
- Sequential execution (no pipelining)
    

**Not included:**

- Memory subsystem
    
- Pipeline execution
    
- Hazard detection
    

---


## Registers

The simulator includes **8 general-purpose registers**:

```
r0, r1, r2, r3, r4, r5, r6, r7
```

- Each register stores a **32-bit integer**
    
- All registers are initialized to **0**
    
- **r7 special usage:**
    
    - Stores **high 32 bits** of multiplication
        
    - Stores **remainder** of division
        

### Example Instruction

```asm
mov r1 10
```

**Meaning:**

```
r1 = 10
```

---

## Instruction Set

|Instruction|Description|Clock Cycles|
|---|---|---|
|`mov`|Move value into register|1|
|`add`|Add value to register|2|
|`sub`|Subtract value from register|2|
|`mul`|Multiply (low → dest, high → r7)|4|
|`div`|Divide (quotient → dest, remainder → r7)|5|
|`end`|Terminate program|1|

---

## Example Program

```asm
mov r1 10
mov r2 5
add r1 r2
mul r1 2
end
```

### Execution Result

```
r1 = 10
r2 = 5
r1 = r1 + r2 → 15
r1 = r1 * 2 → 30
```

---

## Program Structure

The simulator is implemented using a **CPU class** in Python that handles:

- Register storage
    
- Instruction parsing
    
- Execution logic
    
- Cycle counting
    
- CPI calculation
    

---

## Instruction Representation

Each instruction is parsed into:

- **Opcode**
    
- **Destination register**
    
- **Operand** (register or immediate value)
    

---

## Execution Flow

```text
1. Read instruction from input
2. Parse opcode and operands
3. Resolve operand (register or immediate)
4. Execute instruction
5. Update registers
6. Update cycle count
7. Repeat until "end"
```

---

## Clock Cycle Calculation

Each instruction has a fixed cycle cost.

```text
Total Cycles = Sum of all instruction cycle costs
```

Includes the final `end` instruction.

---

## CPI Calculation

```text
CPI = Total Clock Cycles / Number of Instructions
```

---

## Limitations

This simulator does **not** include:

- Memory instructions (`lw`, `sw`)
    
- Pipeline execution
    
- Hazard detection
    
- Branching or control flow
    

---

## Conclusion

This project demonstrates a simple **ISA simulator in Python**.  
It supports:

- Basic arithmetic operations
    
- Register manipulation
    
- Cycle tracking
    
- CPI calculation
    

This provides a foundational understanding of how CPUs execute instructions at a low level.

---

## Reference

- Python Language  
    [https://www.python.org](https://www.python.org/)
    
