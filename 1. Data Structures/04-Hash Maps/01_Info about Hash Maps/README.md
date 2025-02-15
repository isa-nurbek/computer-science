# Hash Maps Data Structure: Conceptual

## Hash Maps: A Detailed Explanation

A **hash map** (also known as a hash table) is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. Hash maps are widely used because they provide average **O(1)** time complexity for insertions, deletions, and lookups.

---

### Key Components of a Hash Map

1. **Key-Value Pairs**:
   - Each entry in a hash map consists of a **key** and a **value**.
   - The key is used to compute the index where the value will be stored.

![Hash Maps Key Value](../01_Info%20about%20Hash%20Maps/hash_maps_images/hash_map_key_value.png)

2. **Hash Function**:
   - A hash function takes a key as input and returns an integer (hash code).
   - The hash code is used to determine the index in the underlying array where the value will be stored.
   - A good hash function distributes keys uniformly across the array to minimize collisions.

![Hash Maps Hash Function](../01_Info%20about%20Hash%20Maps/hash_maps_images/hush_function.webp)

3. **Buckets (or Slots)**:
   - The underlying array where key-value pairs are stored.
   - Each index in the array is called a bucket or slot.

![Hash Maps Buckets](../01_Info%20about%20Hash%20Maps/hash_maps_images/hash-buckets.jpg)

4. **Collision Handling**:
   - A collision occurs when two different keys produce the same hash code (i.e., they map to the same bucket).
   - Common collision resolution techniques:
     - **Chaining**: Store multiple key-value pairs in the same bucket using a linked list or another data structure.
     - **Open Addressing**: Find another available bucket using techniques like linear probing, quadratic probing, or double hashing.

![Hash Maps Collision](../01_Info%20about%20Hash%20Maps/hash_maps_images/collision-in-hashing.jpg)

---

### How a Hash Map Works

#### Step 1: Insertion

1. The key is passed to the hash function to compute the hash code.
2. The hash code is mapped to an index in the array using modulo operation: `index = hash(key) % array_size`.
3. If the bucket at the computed index is empty, the key-value pair is stored there.
4. If the bucket is already occupied (collision), the collision resolution technique is applied.

#### Step 2: Lookup

1. The key is passed to the hash function to compute the hash code.
2. The hash code is mapped to an index in the array.
3. If the bucket at the computed index contains the key, the corresponding value is returned.
4. If the bucket contains multiple key-value pairs (due to chaining), the linked list is traversed to find the matching key.

#### Step 3: Deletion

1. The key is passed to the hash function to compute the hash code.
2. The hash code is mapped to an index in the array.
3. If the bucket at the computed index contains the key, the key-value pair is removed.
4. If the bucket contains multiple key-value pairs, the linked list is traversed to find and remove the matching key.

---

### Example of a Hash Map

Let’s say we have a hash map with the following key-value pairs:

- `("apple", 10)`
- `("banana", 20)`
- `("orange", 30)`

Assume the hash function is:

```text
hash(key) = sum of ASCII values of characters in key
```

And the array size is 5.

#### Step 1: Compute Hash Codes

- `hash("apple") = 97 + 112 + 112 + 108 + 101 = 530`
- `hash("banana") = 98 + 97 + 110 + 97 + 110 + 97 = 609`
- `hash("orange") = 111 + 114 + 97 + 110 + 103 + 101 = 636`

#### Step 2: Map Hash Codes to Indices

- `index = hash(key) % 5`
- `530 % 5 = 0` → "apple" goes to index 0.
- `609 % 5 = 4` → "banana" goes to index 4.
- `636 % 5 = 1` → "orange" goes to index 1.

#### Step 3: Store Key-Value Pairs

The hash map array looks like this:

| Index | Key-Value Pair(s)       |
|-------|-------------------------|
| 0     | ("apple", 10)           |
| 1     | ("orange", 30)          |
| 2     | -                       |
| 3     | -                       |
| 4     | ("banana", 20)          |

---

### Handling Collisions

#### Chaining Example

Suppose we add another key-value pair: `("grape", 40)`.

- `hash("grape") = 103 + 114 + 97 + 112 + 101 = 527`
- `527 % 5 = 2` → "grape" goes to index 2.

Now, the hash map array looks like this:

| Index | Key-Value Pair(s)       |
|-------|-------------------------|
| 0     | ("apple", 10)           |
| 1     | ("orange", 30)          |
| 2     | ("grape", 40)           |
| 3     | -                       |
| 4     | ("banana", 20)          |

If we add another key-value pair: `("lemon", 50)`.

- `hash("lemon") = 108 + 101 + 109 + 111 + 110 = 539`
- `539 % 5 = 4` → "lemon" goes to index 4.

Since index 4 is already occupied by `("banana", 20)`, we use chaining to store both key-value pairs in a linked list:

| Index | Key-Value Pair(s)                     |
|-------|---------------------------------------|
| 0     | ("apple", 10)                         |
| 1     | ("orange", 30)                        |
| 2     | ("grape", 40)                         |
| 3     | -                                     |
| 4     | [("banana", 20) → ("lemon", 50)]      |

---

### Visual Representation

Here’s a visual representation of the hash map after inserting all the key-value pairs:

```text
Index 0: ("apple", 10)
Index 1: ("orange", 30)
Index 2: ("grape", 40)
Index 3: -
Index 4: [("banana", 20) → ("lemon", 50)]
```

---

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | O(1)         | O(n)       |
| Lookup    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

- The worst case occurs when all keys hash to the same bucket, resulting in a linked list of size `n`.

---

### Applications of Hash Maps

1. **Database Indexing**: Hash maps are used to index data for fast retrieval.
2. **Caching**: Hash maps are used in caching systems like Redis.
3. **Counting Frequencies**: Hash maps can count occurrences of elements in a dataset.
4. **Symbol Tables**: Used in compilers to store variables and their attributes.

---

### Summary

- A hash map is a data structure that stores key-value pairs.
- It uses a hash function to compute an index for each key.
- Collisions are handled using techniques like chaining or open addressing.
- Hash maps provide average O(1) time complexity for insertions, deletions, and lookups.

---

### Scenario: Inserting Key-Value Pairs into a Hash Map

Let’s create a **visual example** of a hash map to help you understand how it works step by step. We’ll use a simple scenario with collisions and demonstrate how they are handled using **chaining**.

**Keys and Values**:

- `("apple", 10)`
- `("banana", 20)`
- `("orange", 30)`
- `("grape", 40)`
- `("lemon", 50)`

**Hash Function**:

- Sum of ASCII values of the characters in the key.

**Array Size**: 5

---

### Step 1: Compute Hash Codes and Indices

| Key     | Hash Code Calculation                     | Hash Code | Index (Hash Code % 5) |
|---------|-------------------------------------------|-----------|-----------------------|
| "apple" | 97 + 112 + 112 + 108 + 101 = 530          | 530       | 530 % 5 = 0           |
| "banana"| 98 + 97 + 110 + 97 + 110 + 97 = 609        | 609       | 609 % 5 = 4           |
| "orange"| 111 + 114 + 97 + 110 + 103 + 101 = 636     | 636       | 636 % 5 = 1           |
| "grape" | 103 + 114 + 97 + 112 + 101 = 527           | 527       | 527 % 5 = 2           |
| "lemon" | 108 + 101 + 109 + 111 + 110 = 539          | 539       | 539 % 5 = 4           |

---

### Step 2: Insert Key-Value Pairs into the Hash Map

#### Initial Hash Map (Empty)

```text
Index 0: -
Index 1: -
Index 2: -
Index 3: -
Index 4: -
```

#### Insert `("apple", 10)`

- Index = 0

```text
Index 0: ("apple", 10)
Index 1: -
Index 2: -
Index 3: -
Index 4: -
```

#### Insert `("banana", 20)`

- Index = 4

```text
Index 0: ("apple", 10)
Index 1: -
Index 2: -
Index 3: -
Index 4: ("banana", 20)
```

#### Insert `("orange", 30)`

- Index = 1

```text
Index 0: ("apple", 10)
Index 1: ("orange", 30)
Index 2: -
Index 3: -
Index 4: ("banana", 20)
```

#### Insert `("grape", 40)`

- Index = 2

```text
Index 0: ("apple", 10)
Index 1: ("orange", 30)
Index 2: ("grape", 40)
Index 3: -
Index 4: ("banana", 20)
```

#### Insert `("lemon", 50)`

- Index = 4 (Collision with `("banana", 20)`)
- Use **chaining** to handle the collision.

```text
Index 0: ("apple", 10)
Index 1: ("orange", 30)
Index 2: ("grape", 40)
Index 3: -
Index 4: [("banana", 20) → ("lemon", 50)]
```

---

### Final Hash Map Visualization

Here’s the final state of the hash map after all insertions:

```text
Index 0: ("apple", 10)
Index 1: ("orange", 30)
Index 2: ("grape", 40)
Index 3: -
Index 4: [("banana", 20) → ("lemon", 50)]
```

---

### Visual Representation

Let’s represent the hash map as a table with linked lists for chaining:

| Index | Key-Value Pair(s)                     |
|-------|---------------------------------------|
| 0     | ("apple", 10)                         |
| 1     | ("orange", 30)                        |
| 2     | ("grape", 40)                         |
| 3     | -                                     |
| 4     | [("banana", 20) → ("lemon", 50)]      |

---

### How It Works Visually

1. **Index 0**: Contains only `("apple", 10)`.
2. **Index 1**: Contains only `("orange", 30)`.
3. **Index 2**: Contains only `("grape", 40)`.
4. **Index 3**: Empty.
5. **Index 4**: Contains a linked list with two key-value pairs:
   - `("banana", 20)` is the first node.
   - `("lemon", 50)` is the second node, linked to the first.

---

### Lookup Example

#### Lookup `("lemon")`

1. Compute hash code: `hash("lemon") = 539`.
2. Compute index: `539 % 5 = 4`.
3. Go to index 4.
4. Traverse the linked list:
   - First node: `("banana", 20)` → Key does not match.
   - Second node: `("lemon", 50)` → Key matches! Return value `50`.

---

### Deletion Example

#### Delete `("banana")`

1. Compute hash code: `hash("banana") = 609`.
2. Compute index: `609 % 5 = 4`.
3. Go to index 4.
4. Traverse the linked list:
   - First node: `("banana", 20)` → Key matches! Remove this node.
5. Update the linked list at index 4:
   - New linked list: `("lemon", 50)`.

Updated hash map:

```text
Index 0: ("apple", 10)
Index 1: ("orange", 30)
Index 2: ("grape", 40)
Index 3: -
Index 4: ("lemon", 50)
```

---

### Summary of Visual Example

- The hash map uses a hash function to map keys to indices.
- Collisions are handled using **chaining** (linked lists).
- Lookup, insertion, and deletion are efficient when collisions are minimal.

Let me know if you’d like to explore more visual examples or dive deeper into specific scenarios!
