
Author:

Type: 

Topics:

Link: [[CodingBat]] [[CSX3002 - OBJECT-ORIENTED CONCEPTS AND PROGRAMMING]] [[Java]]
___
Using arrays in Java involves several common operations such as declaration, initialization, accessing elements, and modifying elements. Here's a brief overview:

### Declaration and Initialization:

1. **Declaration:**
   ```java
   // Declare an array of integers
   int[] numbers;

   // Declare an array of strings
   String[] names;
   ```

2. **Initialization:**
   ```java
   // Initialize an array of integers with size 5
   numbers = new int[5];

   // Initialize an array of strings with specific values
   names = new String[]{"Alice", "Bob", "Charlie"};
   ```

   You can also combine declaration and initialization in one line:
   ```java
   int[] numbers = new int[]{1, 2, 3, 4, 5};
   ```

### Accessing Elements:

```java
int[] numbers = {10, 20, 30, 40, 50};

// Access the element at index 2
int valueAtIndex2 = numbers[2];
System.out.println("Value at index 2: " + valueAtIndex2);
```

### Modifying Elements:

```java
int[] numbers = {10, 20, 30, 40, 50};

// Modify the element at index 3
numbers[3] = 45;
```

### Iterating Through an Array:

1. **For Loop:**
   ```java
   int[] numbers = {1, 2, 3, 4, 5};

   for (int i = 0; i < numbers.length; i++) {
       System.out.println("Element at index " + i + ": " + numbers[i]);
   }
   ```

2. **Enhanced For Loop (for-each):**
   ```java
   int[] numbers = {1, 2, 3, 4, 5};

   for (int num : numbers) {
       System.out.println("Element: " + num);
   }
   ```

### Array Length:

The `length` property is used to determine the length of an array:

```java
int[] numbers = {1, 2, 3, 4, 5};
int length = numbers.length;
System.out.println("Array length: " + length);
```

