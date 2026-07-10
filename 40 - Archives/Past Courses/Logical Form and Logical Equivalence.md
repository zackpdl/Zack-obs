"My shirt is grey but my shorts are not"
p = My shirt is grey 
q = my shorts are grey
~q = my shorts are not grey
$p \land \sim q$

> And $\land$ require both or all to be true to be true

Truth Table

| P | Q | P ∧ Q | P ∨ Q |
|---|---|-------|-------|
| T | T |   T   |   T   |
| T | F |   F   |   T   |
| F | T |   F   |   T   |
| F | F |   F   |   F   |

Not P or Not Q

| P | Q | ~P | ~Q | ~P ∨ ~Q |
|---|---|----|----|--------|
| T | T |  F |  F |    F   |
| T | F |  F |  T |    T   |
| F | T |  T |  F |    T   |
| F | F |  T |  T |    T   |

> Def: Two statements are logically equivalent if they have the same truth table
> 
> Def: A tautology t is a statement that is always true
> 
> Def: A contradiction c is a statement that is always false
> 
> When the hypothesis is false, the statement is vacuously true.

P then Q
 
|  p  |  q  | p → q |
| --- | --- | ----- |
|  T  |  T  |   T   |
|  T  |  F  |   F   |
|  F  |  T  |   T   |
|  F  |  F  |   T   |

## Laws

### not (p or q) = (not p) and (not q)?

| P | Q | ~P | ~Q | P ∨ Q | ~P ∨ ~Q | ~ (P ∨ Q) | (¬P) ∧ (¬Q) |
|---|---|----|----|-------|--------|----------|-------------|
| T | T |  F |  F |   T   |   F    |     F    |      F      |
| T | F |  F |  T |   T   |   T    |     F    |      F      |
| F | T |  T |  F |   T   |   T    |     F    |      F      |
| F | F |  T |  T |   F   |   T    |     T    |      T      |

> The statement ¬(p∨q)¬(p∨q) is indeed equivalent to (¬p)∧(¬q)based on De Morgan's Laws in propositional logic.






	The biconditional p » q means that both p → q and q → p 
	If I study hard, then I will pass 
	AND I pass, then I studied hard
	I will pass if and only if I study hard


