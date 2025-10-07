

## Quiz

_Answer the following questions in 2-3 sentences each, based on the provided source material._

1. In object-oriented programming, what is the fundamental difference between a "class" and an "object"?
2. How does Java's runtime memory management distinguish between the roles of the stack and the heap?
3. Explain the key difference between a Java class that `implements` an interface and one that `extends` another class, particularly concerning inheritance.
4. What are checked exceptions in Java, and how does the compiler enforce their handling?
5. Contrast the "pass by value" and "pass by reference" parameter passing mechanisms.
6. What is tail-call optimization, and how does it improve the performance of recursive functions?
7. Prolog is described as having "two faces." What are these two aspects of the language?
8. Describe the process of unification in Prolog and explain its role in processing a query.
9. What is "negation as failure" in Prolog, and how does the `not` predicate work?
10. In C, multidimensional arrays can be stored in row-major or column-major order. How does this layout affect the performance of code that iterates through the array?

--------------------------------------------------------------------------------

## Answer Key

1. A class is a definition that serves as a template for creating objects. An object is a specific instance of a class, described as a "little bundle of data that knows how to do things to itself." For example, multiple `Point` objects, each with its own coordinates and color, can be instances of the same `Point` class.
2. The stack is used for dynamically allocating activation records for method calls, which are pushed on call and popped on return. The heap is a pool of memory for objects and other data where allocations and deallocations can occur in any order, managed by mechanisms like "First Fit" or garbage collection.
3. A class that `implements` an interface only gains an obligation to provide definitions for the method prototypes in that interface. In contrast, a class that `extends` a base class inherits all of its methods and fields, gaining both its type and its implementation.
4. Checked exceptions are all throwable classes that do not descend from `Error` or `RuntimeException`. A method that can generate a checked exception is not permitted to ignore it; the compiler requires the method to either catch the exception within a `try` block or declare it in a `throws` clause.
5. In pass by value, the formal parameter is a local variable initialized with a copy of the actual parameter's value; changes to the formal do not affect the actual. In pass by reference, the formal parameter becomes an alias for the actual parameter, sharing the same memory location, so any changes to the formal directly affect the actual.
6. Tail-call optimization is a process where a language system reuses the current activation record for a tail call, as the calling function has no further computation to perform. This makes the call faster by avoiding the push/pop of a new frame and allows tail-recursive functions to use constant stack space, preventing overflow.
7. The two faces of Prolog are the declarative and the procedural. The declarative aspect views a program as a set of logical assertions or formulas, describing a problem without specifying how to solve it. The procedural aspect considers a program as a set of proof procedures, where the ordering of clauses and conditions dictates the execution flow and search for a solution.
8. Unification is a form of pattern-matching where two Prolog terms are compared to see if a substitution exists that can make them identical. Prolog finds the Most General Unifier (MGU), which does just enough substitution to unify. It is the core mechanism for parameter passing, variable binding, and data construction/selection when Prolog attempts to prove goals.
9. "Negation as failure" is the procedural interpretation of the `not(X)` predicate. To prove `not(X)`, Prolog first attempts to prove the goal `X`. The `not(X)` goal succeeds only if the attempt to prove `X` fails.
10. C uses row-major order, meaning array elements are stored in memory one complete row at a time. Code that accesses elements sequentially in this same order (e.g., iterating through columns in an inner loop) is faster because memory hardware is optimized for sequential access. Accessing elements in column-major order results in non-sequential memory access, which is less efficient.

--------------------------------------------------------------------------------

## Essay Questions

_Suggest an outline or key points for a comprehensive answer to the following questions. Do not provide a full essay._

1. Compare and contrast Java's approach to polymorphism using interfaces (`implements`) and class inheritance (`extends`). Discuss the concepts of inheriting type versus inheriting implementation, the role of the `Object` class, and how Java avoids the complexities of multiple inheritance found in languages like C++.
2. Describe the three primary approaches to automatic garbage collection discussed in the source material: Mark and Sweep, Copying Collection, and Reference Counting. For each, explain its fundamental mechanism, its ability to handle used vs. unused inclusion errors, and its major advantages and disadvantages, such as performance overhead and the ability to reclaim cyclical data structures.
3. Explain the difference between eager and lazy evaluation in the context of parameter passing. Detail how the "by-name" and "by-need" mechanisms work, contrasting them with the more common "by-value" technique. Use the concept of a short-circuiting logical operator to illustrate a scenario where lazy evaluation is beneficial.
4. Using the provided Prolog code for the "wolf, goat, and cabbage" riddle, explain how Prolog performs a problem-space search. Describe how the problem is represented using terms and lists, how `move` and `safe` predicates define the search space and its constraints, and how the recursive `solution` predicate uses backtracking to explore possible move sequences to find a valid path from the initial to the final state.
5. Discuss the concept of a "cost model" for a programming language, explaining why it is important for writing efficient code even though it is often not part of the formal language specification. Using examples from the source material, detail the cost models for (a) cons-cell list operations in ML/Prolog, (b) array layouts in C, and (c) tail-call optimization.

--------------------------------------------------------------------------------

## Glossary

|   |   |
|---|---|
|Term|Definition|
|**Abstract Class**|A class declared `abstract` that is used only as a base class. It cannot be instantiated to create objects and may contain methods without definitions.|
|**Actual Parameters**|The expressions or values provided in a method call.|
|**Aliasing**|A situation where two or more expressions have the same lvalue, meaning they refer to the same memory location. Occurs notably with pass-by-reference parameters.|
|**Anonymous Variable (**`**_**`**)**|In Prolog, a variable represented by an underscore. Each occurrence is bound independently, effectively matching any term without creating a new binding.|
|**API (Application Programming Interface)**|The vast collection of predefined classes and methods provided by a language system for tasks like I/O, GUI development, networking, etc.|
|**Atom**|A type of constant in Prolog. It can be a lowercase letter followed by letters/digits/underscores (e.g., `fred`), a sequence of non-alphanumeric characters (e.g., `*`), or a quoted string of characters.|
|**Backtracking**|The process in Prolog where, upon failing to prove a goal, the system goes back to a previous choice point and tries an alternative path, such as a different clause or a different unification.|
|**Boxing**|An automatic coercion in Java (added in 2004) that converts a primitive type value (like `int`) into an object of its corresponding wrapper class (like `Integer`).|
|**Capture**|A phenomenon in macro expansion where free variables in an actual parameter become bound by definitions within the macro body, or vice-versa, leading to unexpected behavior.|
|**Checked Exception**|In Java, a throwable class that is not a descendant of `Error` or `RuntimeException`. The compiler requires that methods which might throw a checked exception must either catch it or declare it in a `throws` clause.|
|**Class**|In object-oriented languages, a template or definition for creating objects. It groups together field and method definitions.|
|**Clause**|The fundamental unit of a Prolog program. A clause can be either a fact (a single term ending in a period) or a rule (a head and a body separated by `:-`).|
|**Coalescing**|In heap management, the process of merging adjacent free blocks of memory into a single larger free block to combat fragmentation.|
|**Compound Term**|A structured data type in Prolog, consisting of an atom (the functor) followed by a parenthesized, comma-separated list of one or more terms.|
|**Constructor**|A special method in a class that is called when a new object (instance) of that class is created, typically to initialize its fields.|
|**Copying Collection**|A garbage collection technique that divides memory into two halves. It copies live objects from the active half to the other half, compacting them in the process, and then switches halves.|
|**Current Heap Link**|A memory location (outside or inside the heap) that stores a value which the running program will use as a heap address.|
|**Cut (**`**!**`**)**|A special goal in Prolog that always succeeds but commits the system to all choices made so far in proving the current goal. It prunes the search tree by eliminating backtracking opportunities.|
|**Declarative Language**|A language where programs correspond to simple mathematical abstractions (e.g., logic formulas in Prolog, functions in ML), describing _what_ a program should compute rather than _how_.|
|**Delegation**|A dynamic technique used in prototype-based languages as an alternative to inheritance, where an object forwards messages it cannot handle to a designated prototype object.|
|**Dynamic Dispatch**|The runtime mechanism in OO languages for selecting the correct method implementation to call based on the actual class of an object, not the static type of its reference.|
|**Dynamic Memory Allocation**|The allocation of memory at runtime for entities like activation records, objects, strings, and arrays.|
|**Encapsulation**|The practice of bundling data and the methods that operate on that data within an object, hiding the internal state and controlling access through a public interface.|
|**Evaluable Predicate**|In Prolog, a predicate that can be evaluated as a numeric expression when used with operators like `is` or numeric comparisons. Examples include `+`, `-`, `*`, `/`, and `sqrt`.|
|**Exception**|An object, inheriting from the `Throwable` class in Java, that represents an error or exceptional condition occurring during program execution.|
|**Fact**|A type of clause in Prolog that consists of a single term followed by a period. It asserts a piece of information as being unconditionally true.|
|**Field**|A piece of data contained within an object. For example, a `Point` object has fields for its x-coordinate, y-coordinate, and color.|
|**First Fit**|A heap allocation strategy that searches the list of free memory blocks and allocates memory from the first block it finds that is large enough to satisfy the request.|
|**Formal Parameters**|The variable names listed in a method's definition.|
|**Fragmentation**|A condition in heap memory where free memory is broken into many small, non-contiguous blocks, preventing the allocation of a large block even if the total free space is sufficient.|
|**Garbage Collection**|The automatic process of reclaiming memory occupied by objects that are no longer in use by the program.|
|**Generational Collector**|A garbage collection refinement that divides heap objects into generations based on their age. It collects garbage more frequently in younger generations, where objects are more likely to become unreachable quickly.|
|**Generics**|A feature in languages like Java (since 2004) that allows classes, interfaces, and methods to be parameterized by type. This enables the creation of general-purpose data structures (e.g., `Stack<T>`) that are type-safe.|
|**Heap**|A pool of memory blocks used for dynamic memory allocation where allocations and deallocations can occur in any order.|
|**Inheritance**|A mechanism in object-oriented programming where a new class (the derived class) acquires the properties (methods and fields) of an existing class (the base class).|
|**Inlining**|An optimization technique where a compiler replaces a function call with the actual body of the called function, saving the overhead of the call.|
|**Instance**|Another term for an object. An object is an instance of a particular class.|
|**Interface**|In Java, a collection of method prototypes (names and types, without bodies). A class can `implement` an interface, obligating it to provide definitions for those methods.|
|`**is**` **Predicate**|A predefined Prolog operator that evaluates a numeric expression on its right side and unifies the result with the term on its left.|
|**Lvalue**|An attribute of an expression that refers to a memory location. Expressions that can appear on the left side of an assignment must have an lvalue.|
|**Mark and Sweep**|A garbage collection technique that first traverses all live heap links from a root set to mark all reachable objects, and then sweeps through the entire heap, reclaiming all unmarked blocks.|
|**Method**|A procedure or function associated with a class that an object of that class "knows how to do." For example, a `Point` object has a `move` method.|
|**Most General Unifier (MGU)**|In Prolog unification, a unifier that makes two terms identical with the minimum necessary substitutions, without making the result more specific than required.|
|**Multiple Inheritance**|A feature in some OO languages (like C++) where a class can inherit from more than one base class. Java does not support this for classes but allows a class to implement multiple interfaces.|
|**Negation as Failure**|The procedural mechanism behind Prolog's `not` predicate. `not(X)` succeeds if the goal `X` fails, and fails if `X` succeeds.|
|**Object**|A fundamental concept in object-oriented programming; a self-contained entity consisting of data (fields) and procedures to manipulate that data (methods).|
|**Occurs Check**|A part of the theoretical unification algorithm that prevents unifying a variable `X` with a term `t` if `X` appears within `t`. Most Prolog systems omit this for efficiency.|
|**Override**|The action of a derived class providing a new definition for a method that it inherited from its base class.|
|**Pass by Name**|A parameter passing mechanism where the actual parameter is evaluated in the caller's context every time the corresponding formal parameter is used. It is like macro expansion but without variable capture.|
|**Pass by Need**|A lazy parameter passing mechanism where the actual parameter is evaluated in the caller's context only on its first use. The result is then cached for subsequent uses.|
|**Pass by Reference**|A parameter passing mechanism where the formal parameter becomes an alias for the actual parameter, sharing the same memory location.|
|**Pass by Result**|A parameter passing mechanism where the formal parameter is an uninitialized local variable. Its final value is copied back to the actual parameter when the method finishes.|
|**Pass by Value**|A parameter passing mechanism where the formal parameter is a local variable initialized with a copy of the actual parameter's value.|
|**Pass by Value-Result**|A parameter passing mechanism that combines pass by value and pass by result. The formal parameter is initialized with the actual's value, and the formal's final value is copied back to the actual upon return.|
|**Polymorphism**|The ability of an entity (like a variable or method call) to refer to objects of different classes at different times. Subtype polymorphism allows a reference of a base class type to refer to an object of a derived class.|
|**Proof Tree**|An abstract representation of a Prolog search. The root is the initial query, and nodes represent lists of goals, with children for each applicable program clause. Prolog explores this tree via a depth-first, left-to-right traversal.|
|**Prototype**|In prototype-based languages, an existing object that is cloned to create new, similar objects. This approach is used instead of class-based instantiation.|
|**Query**|In Prolog, a request to the system to prove a goal. It is a term or a conjunction of terms entered at the prompt.|
|**Reference Counting**|A garbage collection technique where each object maintains a count of the number of references pointing to it. When an object's count drops to zero, it is reclaimed.|
|**Reference Type**|In Java, a type whose values are references to objects. This includes all class, interface, and array types.|
|**Resolution**|The core inference step in Prolog's execution model. It takes a goal and a program clause, finds their Most General Unifier, and produces a new list of goals to be proved.|
|**Root Set**|In garbage collection, the set of memory locations outside the heap (e.g., in active activation records or static variables) that contain the initial links into the heap.|
|**Rule**|A type of clause in Prolog consisting of a head term and a body of one or more goal terms, separated by `:-`. It states that the head is true if all goals in the body can be proven.|
|**Rvalue**|An attribute of an expression that represents its value. Expressions on the right side of an assignment must have an rvalue.|
|**Side Effect**|An action of an operator or statement that changes something in the program environment, such as the value of a variable.|
|**Stack**|A region of memory used for managing activation records for method calls in a last-in, first-out (LIFO) manner.|
|**Substitution**|In Prolog, a function that maps variables to terms. Applying a substitution to a term produces an instance of that term.|
|**Tail Call**|A function call that is the very last action performed by a function before it returns. The calling function does no further computation with the result.|
|**Term**|The fundamental data structure in Prolog from which all programs and data are built. The three kinds of terms are constants, variables, and compound terms.|
|**Unboxing**|The reverse of boxing; an automatic coercion in Java that converts an object from a wrapper class (like `Integer`) back to its corresponding primitive type value (like `int`).|
|**Unification**|The process in Prolog of finding a substitution that makes two terms identical. It is the basis for pattern matching, parameter passing, and variable binding.|
|**Unifier**|A substitution that makes two terms identical.|