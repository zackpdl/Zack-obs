
Author:

Type: 

Topics:

Link: [[CSX3002 - OBJECT-ORIENTED CONCEPTS AND PROGRAMMING]] [[Java]]
___
In Java, operators are special symbols that perform operations on operands. Operands can be variables, constants, or expressions. Here's an overview of the different types of operators in Java:

1. **Arithmetic Operators:**
   - `+` (addition)
   - `-` (subtraction)
   - `*` (multiplication)
   - `/` (division)
   - `%` (modulus, returns the remainder of a division)

   ```java
   int a = 10, b = 3;
   int sum = a + b; // 13
   int difference = a - b; // 7
   int product = a * b; // 30
   int quotient = a / b; // 3
   int remainder = a % b; // 1
   ```

2. **Relational Operators:**
   - `==` (equal to)
   - `!=` (not equal to)
   - `>` (greater than)
   - `<` (less than)
   - `>=` (greater than or equal to)
   - `<=` (less than or equal to)
   - == (is equal to)

   ```java
   int x = 5, y = 10;
   boolean isEqual = (x == y); // false
   boolean isNotEqual = (x != y); // true
   boolean isGreaterThan = (x > y); // false
   boolean isLessThan = (x < y); // true
   ```

3. **Logical Operators:**
   - `&&` (logical AND)
   - `||` (logical OR)
   - `!` (logical NOT)

   ```java
   boolean condition1 = true, condition2 = false;
   boolean resultAnd = (condition1 && condition2); // false
   boolean resultOr = (condition1 || condition2); // true
   boolean resultNot = !condition1; // false
   ```

4. **Assignment Operators:**
   - `=` (assignment)
   - `+=` (addition assignment)
   - `-=` (subtraction assignment)
   - `*=` (multiplication assignment)
   - `/=` (division assignment)
   - `%=` (modulus assignment)

   ```java
   int num = 10;
   num += 5; // num is now 15
   num -= 3; // num is now 12
   num *= 2; // num is now 24
   num /= 4; // num is now 6
   ```

5. **Increment and Decrement Operators:**
   - `++` (increment by 1)
   - `--` (decrement by 1)

   ```java
   int count = 5;
   count++; // count is now 6
   count--; // count is now 5 again
   ```

6. **Bitwise Operators:**
   - `&` (bitwise AND)
   - `|` (bitwise OR)
   - `^` (bitwise XOR)
   - `~` (bitwise NOT)
   - `<<` (left shift)
   - `>>` (right shift)
   - `>>>` (unsigned right shift)

   ```java
   int a = 5, b = 3;
   int bitwiseAnd = a & b; // 1
   int bitwiseOr = a | b; // 7
   int bitwiseXor = a ^ b; // 6
   int bitwiseNot = ~a; // -6
   int leftShift = a << 1; // 10
   int rightShift = a >> 1; // 2
   ```

These are the basic operators in Java. They are used to manipulate variables and perform various operations in Java programs.