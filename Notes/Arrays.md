# Arrays

## What is an Array?
- An array is a collection of elements stored in **contiguous memory locations**.
---

## Time Complexity
Time Complexity measures **how the running time of an algorithm grows as the input size (`n`) increases**.

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Traversal | O(n) |
| Search | O(n) |
| Insert (End) | O(1)* |
| Insert (Middle/Beginning) | O(n) |
| Delete (End) | O(1)* |
| Delete (Middle/Beginning) | O(n) |

> *Average case for dynamic arrays like Python lists.

---

## Access — O(1)
Directly access an element using its index.
---

## Traversal — O(n)
Visit every element once.
---

## Search — O(n)
Check each element until the target is found.
---

## Insert
- **End:** O(1) average (`append()`)
- **Middle/Beginning:** O(n) because elements must shift.
---

## Delete
- **End:** O(1) average (`pop()`)
- **Middle/Beginning:** O(n) because elements shift left.
---

## Space Complexity
Measures the **extra memory** an algorithm uses.

Example:
- Uses no extra array → **O(1)**
- Creates another array of size `n` → **O(n)**

---

## In-place vs Extra Space

### In-place (O(1) Extra Space)
Modifies the original array.

### Extra Space (O(n))
Creates a new array.

---

## Key Points
- Arrays allow **fast random access**.
- Searching an unsorted array takes **O(n)**.
- Inserting/deleting in the middle is expensive because elements shift.
- Prefer **in-place** solutions when possible to save memory.