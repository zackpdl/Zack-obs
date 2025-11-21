
### Puran Paodensakul (6611140)

# CSX3007 Home Assignment 1 

## 1. Number of different values with 16 bits

2¹⁶ = **65,536**



## 2. Largest unsigned 32-bit binary number

2³² − 1 = **4,294,967,295**



## 3. Largest 16-bit values

**3.1 Unsigned:** 65,535  
**3.2 Two’s complement:** +32,767  
**3.3 Sign/magnitude:** +32,767



## 4. Hexadecimal to decimal

A5₁₆ = 165  
3B₁₆ = 59  
FFFF₁₆ = 65,535  
ED3A₁₆ = 60,730

  

## 5. Hexadecimal to unsigned binary

A5 → 1010 0101  
3B → 0011 1011  
FFFF → 1111 1111 1111 1111  
ED3A → 1110 1101 0011 1010

  

## 6. Two’s complement to decimal

1010₂ = −6  
110110₂ = −10  
01110000₂ = 112  
10011111₂ = −97

  

## 7. Convert to 8-bit sign/magnitude

1010 → 10001010  
110110 → 10110110  
01110000 → 01110000  
10011111 → 11011111

  

## 8. 4-bit to 8-bit two’s complement

0101 → 0000 0101  
1010 → 1111 1010

  

## 9. Unsigned binary addition

10011001 + 01000100 = 11011101 (no overflow)  
11010010 + 10110110 = overflow

  

## 10. Two’s complement addition

First pair: no overflow  
Second pair: overflow

  

## 11. Decimal to 8-bit binary and addition

27 + 31 = 58 (no overflow)  
−4 + 19 = 15 (no overflow)  
3 + (−32) = −29 (no overflow)  
−16 + −9 = −25 (no overflow)

  

## 12. Unsigned hexadecimal addition (8-bit max = FF)

7 + 9 = 0A (no overflow)  
13 + 28 = 29 (no overflow)  
AB + 3E = E9 (no overflow)  
8F + AD = overflow

  

## 13. BCD

289 → 0010 1000 1001  
1001 0101 0001 (BCD) → 951  
0110 1001 (BCD) → 01101001₂  
92 + 25 → 117 BCD  
38 + 22 → 60 BCD  
78 + 32 → 110 BCD

  

## 14. Number of truth tables for N variables

2^(2^N)

  

## 15. NAND gate implementations

NOT: A NAND A  
AND: (A NAND B) NAND (A NAND B)  
OR: (A NAND A) NAND (B NAND B)  
NOR: OR output NAND with itself  
XOR: Standard NAND-only XOR structure  
XNOR: NOT(XOR)

  

## 16. Three-input XOR truth table

|A|B|C|XOR|
|  |  |  |  |
|0|0|0|0|
|0|0|1|1|
|0|1|0|1|
|0|1|1|0|
|1|0|0|1|
|1|0|1|0|
|1|1|0|0|
|1|1|1|1|

  

## 17. XOR as NOT and buffer

A XOR 1 = NOT A  
A XOR 0 = A
