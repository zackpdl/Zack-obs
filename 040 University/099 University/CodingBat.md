Status: #

Class: [[CSX3002 - OBJECT-ORIENTED CONCEPTS AND PROGRAMMING]]

Subject/Topics: [[Java]] [[Strings]]

Date: 2023-11-25

Teacher:
___

Notes:
[[Array]]
### How to get a part of a string?
#substring
``` java
#1
String text;
text = "Hello World"
results = text.substring(6,10);
#2
text = "Hello World"
results = text.substring(6);
### Output
Worl
World

```

### How to get last few characters
#substring #length
``` java
String text;
text = "Hello World"
lasttwochar = text.substring(text.length() -2)

```
### How to put conditions
#if/else
```java
if (len >= 3) {

} else {

}
```

### How to find if integer is even?
```java
if (number % 2 == 0){

} else {
return null;
}
```
always need else if using if statement

### How to find middle letter?
```Java
int mid = str.length() / 2;
```

### How to use .equals
```Java
return str.substring(0, 3).equals(bad)
```


### How to use for loop
```java
for (int i = 1; i <= 5; i++) 
	{ System.out.println(i); }
	
```
in for loop 0,10 = position 1-9 it wont consider the last position 

### Middle can be any character
```java
int len = str.length();
for (int i = 0; i <= len - 3; i++) {
	// Check if the substring has the pattern "c*t" (where * can be any character)
	if (str.charAt(i) == 'c' && str.charAt(i + 2) == 't') {
	return true;
	}
}
return false;






```

### Counting yz

```java
public int countYZ(String str) {
    // Check if the input string is empty
    if (str.length() == 0)
        return 0;

    // Initialize the count variable to keep track of occurrences
    int count = 0;

    // Iterate through the string up to the second-to-last character
    for (int i = 0; i <= str.length() - 2; i++) {
        // Extract the current and next characters
        char currentChar = str.charAt(i);
        char nextChar = str.charAt(i + 1);

        // Check if the current character is 'y' or 'z' (case-insensitive) and if the next character is not a letter
        if ((currentChar == 'y' || currentChar == 'Y' || currentChar == 'z' || currentChar == 'Z') &&
            !Character.isLetter(nextChar))
            count++;
    }

    // Extract the last character
    char lastChar = str.charAt(str.length() - 1);

    // Check if the last character is 'y' or 'z' (case-insensitive)
    if (lastChar == 'y' || lastChar == 'Y' || lastChar == 'z' || lastChar == 'Z')
        count++;

    // Return the final count
    return count;
}
```


## new array copy

```java
public int[] front11(int[] a, int[] b) {
    int[] n;

    // Check if both arrays are empty, and if so, return an empty array
    if (a.length == 0 && b.length == 0) {
        return new int[0];
    }

    // Initialize result array with the correct size based on non-empty arrays
    n = new int[(a.length > 0 ? 1 : 0) + (b.length > 0 ? 1 : 0)];

    // Check if array a is non-empty and assign its first element to the result array
    if (a.length > 0) {
        n[0] = a[0];
    }

    // Check if array b is non-empty and assign its first element to the result array
    if (b.length > 0) {
        n[n.length - 1] = b[0];
    }

    return n;
}
```

### Remove 1 number and sum
```java
public int sum13(int[] nums) {
    int sum = 0;
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] == 13) {
            nums[i] = 0;
            if (i + 1 < nums.length) {
                nums[i + 1] = 0;
            }
        } else {
            sum += nums[i];
        }
    }

    return sum;
}

```

### Skip num in between

[[Skip explain]] 

```java
public int sum67(int[] nums) {
    int sum = 0;  // Initialize a variable to store the sum

    // Iterate through each element in the array
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] == 6) {  // Check if the current element is 6
            while (nums[i] != 7) {  // Enter a loop until the next element is 7
                i++;  // Increment the index to skip elements between 6 and 7
            }
        } else {
            sum += nums[i];  // Add the current element to the sum if it's not 6
        }
    }

    return sum;  // Return the final sum
}
```
