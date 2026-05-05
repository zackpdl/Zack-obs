
## 📌 1. DATA TYPES

### ❖ Primitive Types

- `int`, `float`, `bool`, `char`, `string`
    
- Example: `let x : int = 5`
    

### ❖ Compound Types

- **Tuples**: `(int * string)` → Fixed-size, heterogeneous  
    Example: `let pair = (1, "hello")`
    
- **Lists**: `'a list` → Homogeneous, recursive  
    Example: `[1; 2; 3]`, `1 :: 2 :: []`
    

### ❖ Variant Types

User-defined types that can take multiple forms.

ocaml

CopyEdit

`type shape =   | Circle of float   | Rectangle of float * float`

---

## 📌 2. FUNCTIONAL SYNTAX & EXPRESSIONS

### ❖ let-binding

- `let x = 10 in x + 5`
    
- `let rec` for recursion
    

### ❖ Pattern Matching

ocaml

CopyEdit

`match x with | [] -> "empty" | h :: t -> "head is " ^ string_of_int h`

### ❖ Anonymous Functions (Lambdas)

ocaml

CopyEdit

`let f = fun x -> x + 1`

### ❖ Currying

- All functions in OCaml are curried by default
    

ocaml

CopyEdit

`let add a b = a + b (* same as *) let add = fun a -> fun b -> a + b`

---

## 📌 3. POLYMORPHISM

### ❖ Parametric Polymorphism

- General types: `'a`, `'b`, etc.
    

ocaml

CopyEdit

`let identity x = x     (* 'a -> 'a *)`

### ❖ Type Inference

- OCaml infers types using **Hindley-Milner** algorithm.
    
- Static typing, compile-time checking.
    

---

## 📌 4. HIGHER-ORDER FUNCTIONS

### ❖ Functions as Values

ocaml

CopyEdit

`let apply_twice f x = f (f x)`

### ❖ Common HOFs

ocaml

CopyEdit

`List.map (fun x -> x + 1) [1;2;3]       (* [2;3;4] *) List.filter (fun x -> x mod 2 = 0) lst  (* even numbers *) List.fold_left ( + ) 0 [1;2;3]          (* 6 *)`

---

## 📌 5. EVALUATION STRATEGIES

### ❖ Eager vs Lazy

- **Eager (Strict)**: Arguments evaluated before function call (OCaml)
    
- **Lazy (Non-strict)**: Only when needed (Haskell)
    

### ❖ Call by Value

- Evaluate arguments **before** applying function
    

### ❖ Call by Name

- Pass expression unevaluated; evaluate when used
    

---

## 📌 6. SCOPE & BINDINGS

### ❖ Lexical Scope

- Variable's scope determined by **code structure**
    
- Inner functions use outer function’s variables (closures)
    

### ❖ Shadowing

ocaml

CopyEdit

`let x = 5 in let x = 10 in x      (* x is 10 *)`

---

## 📌 7. IMMUTABILITY & PURE FUNCTIONS

### ❖ Immutable Data

- Variables cannot be reassigned (`let` is not mutable)
    

### ❖ Pure Functions

- No side effects, same output for same input
    

---

## 📌 8. TYPE SYSTEM

### ❖ Type Safety

- Type errors detected at compile time
    

### ❖ Type Errors

ocaml

CopyEdit

`3 + true     (* Error: expected int, got bool *)`

### ❖ Type Declarations

ocaml

CopyEdit

`let square (x: int) : int = x * x`

---

## 📌 9. RECURSION

### ❖ Base and Recursive Cases

ocaml

CopyEdit

`let rec fact n =   if n = 0 then 1 else n * fact (n - 1)`

### ❖ Tail Recursion

ocaml

CopyEdit

`let rec fact_tail n acc =   if n = 0 then acc else fact_tail (n-1) (n * acc)`

---

## 📌 10. EXAMPLES

### ❖ Fibonacci

ocaml

CopyEdit

`let rec fib n =   if n <= 1 then n else fib (n-1) + fib (n-2)`

### ❖ Sum List

ocaml

CopyEdit

`let rec sum lst =   match lst with   | [] -> 0   | h :: t -> h + sum t`

---

## 📌 11. MUTUAL RECURSION

ocaml

CopyEdit

`let rec even n =   if n = 0 then true else odd (n - 1) and odd n =   if n = 0 then false else even (n - 1)`

---

## 📌 12. COMMON MISTAKES

- Forgetting base case in recursion
    
- Using `=` vs `==`: use `=` for structural equality
    
- Mixing types in lists: `[1; "hi"]` is invalid
    
- Confusing `::` (cons) with `@` (append)
    

---

## 📌 13. SYNTAX QUICK REFERENCE

|Construct|Example|
|---|---|
|let binding|`let x = 5`|
|function|`let f x = x + 1`|
|pattern match|`match x with|
|tuple|`(3, "hi")`|
|list|`[1; 2; 3]`|
|recursion|`let rec f n = ...`|
|anonymous func|`fun x -> x + 1`|

---