# Implementation in Python:


class HashMap:
    def __init__(self, size=10):
        """
        Initialize the hash map with a given size (default is 10).
        Uses a list of lists (buckets) to handle collisions via chaining.
        """
        self.size = size
        self.map = [[] for _ in range(size)]  # Create empty buckets

    def _get_hash(self, key):
        """
        Compute a hash value for a given key using the sum of ASCII values of its characters
        modulo the size of the hash map.
        """
        return sum(ord(char) for char in str(key)) % self.size

    def add(self, key, value):
        """
        Insert or update a key-value pair in the hash map.
        If the key already exists, update its value.
        """
        key_hash = self._get_hash(key)  # Compute the hash index
        key_value = [key, value]

        # Check if the key already exists in the bucket
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return True

        # If key doesn't exist, add the new key-value pair to the bucket
        self.map[key_hash].append(key_value)
        return True

    def get(self, key):
        """
        Retrieve the value associated with a given key.
        Returns None if the key is not found.
        """
        key_hash = self._get_hash(key)  # Compute hash index
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]  # Return the associated value
        return None  # Key not found

    def delete(self, key):
        """
        Remove a key-value pair from the hash map.
        Returns True if the deletion was successful, otherwise False.
        """
        key_hash = self._get_hash(key)  # Compute hash index
        for i, pair in enumerate(self.map[key_hash]):
            if pair[0] == key:
                self.map[key_hash].pop(i)  # Remove the key-value pair
                return True
        return False  # Key not found

    def __str__(self):
        """
        String representation of the hash map showing the contents of each bucket.
        """
        return "\n".join([f"{i}: {bucket}" for i, bucket in enumerate(self.map)])


# Example usage
if __name__ == "__main__":
    h = HashMap()
    h.add("key1", "value1")
    h.add("key2", "value2")
    h.add("key3", "value3")

    print("Initial hash map:")
    print(h)  # Print the hash map

    print("\nRetrieving values:")
    print("Getting key1:", h.get("key1"))  # Get value for key1
    print("Getting key2:", h.get("key2"))  # Get value for key2

    h.delete("key2")  # Delete key2
    print("\nAfter deleting key2:")
    print(h)

    print("\nTrying to retrieve deleted key2:")
    print("Getting key2:", h.get("key2"))  # Should return None

# Output:

"""
Initial hash map:
0: [['key3', 'value3']]
1: []
2: []
3: []
4: []
5: []
6: []
7: []
8: [['key1', 'value1']]
9: [['key2', 'value2']]

Retrieving values:
Getting key1: value1
Getting key2: value2

After deleting key2:
0: [['key3', 'value3']]
1: []
2: []
3: []
4: []
5: []
6: []
7: []
8: [['key1', 'value1']]
9: []

Trying to retrieve deleted key2:
Getting key2: None

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity**

1. **`_get_hash(key)`**:
   - **Time Complexity**: O(k), where `k` is the length of the key (string).
   
   - **Explanation**: The hash function computes the sum of ASCII values of each character in the key. 
   This requires iterating through each character of the key once.

2. **`add(key, value)`**:
   - **Average Case**: O(1 + α), where α is the load factor (average number of elements per bucket).
   - **Worst Case**: O(n), where `n` is the number of elements in the hash map (if all keys collide into the same bucket).
   
   - **Explanation**:
     - Computing the hash is O(k) (as above).
     - Searching the bucket for the key is O(α) on average (due to chaining).
     - Insertion or update is O(1).
     - In the worst case (all keys collide), the bucket becomes a list of size `n`, making insertion/search O(n).

3. **`get(key)`**:
   - **Average Case**: O(1 + α).
   - **Worst Case**: O(n).
   
   - **Explanation**: Similar to `add`, computing the hash is O(k), and searching the bucket is O(α) on average
   (or O(n) in the worst case).

4. **`delete(key)`**:
   - **Average Case**: O(1 + α).
   - **Worst Case**: O(n).
   
   - **Explanation**: Same as `get` and `add`, since deletion involves searching the bucket first.

---

### **Space Complexity**

1. **Overall Space**:
   - **Space Complexity**: O(n + m), where `n` is the number of key-value pairs stored and `m` is the size of the
   internal bucket array (`self.size`).
   
   - **Explanation**:
     - The hash map stores `n` key-value pairs distributed across `m` buckets.
     - Each bucket is a list, and the overhead of the bucket array is O(m).
     - In practice, if the hash map is resized dynamically (not implemented here), `m` is proportional to `n`,
     making the space complexity O(n).

---

### **Notes on Performance**

- The performance relies heavily on the hash function distributing keys uniformly across buckets. If many keys collide,
the worst-case time complexity degrades to O(n).

- This implementation does not handle resizing (dynamic rehashing), so the load factor (`n/m`) can grow unbounded,
leading to poor performance if many keys are added.

- The `_get_hash` function is simple but may not distribute keys uniformly for certain datasets (e.g., keys with the
same characters in different orders will collide).

---

### **Improvements**

1. **Dynamic Resizing**: Double the size of the bucket array and rehash all elements when the load factor exceeds
a threshold (e.g., 0.7). This keeps α bounded and maintains average O(1) operations.

2. **Better Hash Function**: Use a more sophisticated hash function (e.g., Python's built-in `hash()` or a
cryptographic hash) to reduce collisions.

3. **Open Addressing**: Alternative to chaining, where collisions are resolved by probing (linear/quadratic/double hashing).
This can be more cache-friendly but requires careful handling of deletions.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The provided code defines a simple implementation of a **hash map** (also known as a hash table) in Python.
A hash map is a data structure that stores key-value pairs and allows for efficient insertion, retrieval,
and deletion of these pairs. Below is a detailed explanation of how the code works:

---

### **1. Class Definition: `HashMap`**
The `HashMap` class is the core of the implementation. It uses **chaining** to handle collisions, meaning
that each bucket in the hash map can store multiple key-value pairs in a list.

---

### **2. Constructor: `__init__`**
```
def __init__(self, size=10):
    self.size = size
    self.map = [[] for _ in range(size)]
```
- **Purpose**: Initializes the hash map with a given size (default is 10).
- **How it works**:
  - `self.size`: Stores the size of the hash map (number of buckets).
  - `self.map`: A list of lists (buckets) where each bucket is initially empty. For example, if `size = 10`,
  `self.map` will be a list of 10 empty lists.

---

### **3. Hash Function: `_get_hash`**
```
def _get_hash(self, key):
    return sum(ord(char) for char in str(key)) % self.size
```
- **Purpose**: Computes a hash value for a given key.
- **How it works**:
  - Converts the key to a string and sums the ASCII values of its characters.
  - Uses the modulo operator (`%`) to ensure the hash value fits within the range of the hash map's size.
  - This ensures that the hash value is an index within the bounds of `self.map`.

---

### **4. Insert/Update: `add`**
```
def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    for pair in self.map[key_hash]:
        if pair[0] == key:
            pair[1] = value  # Update value if key exists
            return True

    self.map[key_hash].append(key_value)  # Add new key-value pair
    return True
```
- **Purpose**: Inserts or updates a key-value pair in the hash map.

- **How it works**:
  1. Computes the hash index for the key using `_get_hash`.
  2. Checks if the key already exists in the bucket at the computed index:
     - If the key exists, updates its value.
     - If the key does not exist, appends the new key-value pair to the bucket.

---

### **5. Retrieve: `get`**
```
def get(self, key):
    key_hash = self._get_hash(key)
    for pair in self.map[key_hash]:
        if pair[0] == key:
            return pair[1]  # Return the value if key is found
    return None  # Key not found
```
- **Purpose**: Retrieves the value associated with a given key.

- **How it works**:
  1. Computes the hash index for the key.
  2. Iterates through the bucket at the computed index to find the key.
  3. If the key is found, returns the associated value.
  4. If the key is not found, returns `None`.

---

### **6. Delete: `delete`**
```
def delete(self, key):
    key_hash = self._get_hash(key)
    for i, pair in enumerate(self.map[key_hash]):
        if pair[0] == key:
            self.map[key_hash].pop(i)  # Remove the key-value pair
            return True
    return False  # Key not found
```
- **Purpose**: Removes a key-value pair from the hash map.
- **How it works**:
  1. Computes the hash index for the key.
  2. Iterates through the bucket at the computed index to find the key.
  3. If the key is found, removes the key-value pair from the bucket using `pop(i)`.
  4. If the key is not found, returns `False`.

---

### **7. String Representation: `__str__`**
```
def __str__(self):
    return "\n".join([f"{i}: {bucket}" for i, bucket in enumerate(self.map)])
```
- **Purpose**: Provides a string representation of the hash map for easy visualization.
- **How it works**:
  - Iterates through each bucket in `self.map` and formats it as `index: [key-value pairs]`.
  - Joins the formatted strings with newline characters for readability.

---

### **8. Example Usage**
```
if __name__ == "__main__":
    h = HashMap()
    h.add("key1", "value1")
    h.add("key2", "value2")
    h.add("key3", "value3")

    print("Initial hash map:")
    print(h)

    print("\nRetrieving values:")
    print("Getting key1:", h.get("key1"))
    print("Getting key2:", h.get("key2"))

    h.delete("key2")
    print("\nAfter deleting key2:")
    print(h)

    print("\nTrying to retrieve deleted key2:")
    print("Getting key2:", h.get("key2"))
```
- **What happens**:
  1. A `HashMap` object `h` is created.
  2. Three key-value pairs are added to the hash map.
  3. The hash map is printed to show its contents.
  4. Values for `key1` and `key2` are retrieved and printed.
  5. `key2` is deleted from the hash map.
  6. The hash map is printed again to show the updated state.
  7. An attempt to retrieve `key2` after deletion returns `None`.

---

### **How It Works in Detail**
1. **Hashing**:
   - The hash function converts a key into an index within the range of the hash map's size.
   - For example, `key1` might hash to index `3`, so it is stored in the bucket at index `3`.

2. **Collision Handling**:
   - If two keys hash to the same index (collision), they are stored in the same bucket as a list of key-value pairs.
   - For example, if `key1` and `key4` both hash to index `3`, the bucket at index `3` will contain `[[key1, value1],
   [key4, value4]]`.

3. **Operations**:
   - **Insert/Update**: The hash map checks if the key already exists in the bucket. If it does, the value is updated.
   Otherwise, the new key-value pair is appended to the bucket.
   - **Retrieve**: The hash map searches the bucket for the key and returns the associated value if found.
   - **Delete**: The hash map searches the bucket for the key and removes the key-value pair if found.

---

### **Output Example**
For the provided example usage, the output might look like this:
```
Initial hash map:
0: []
1: []
2: []
3: [['key1', 'value1']]
4: [['key2', 'value2']]
5: [['key3', 'value3']]
6: []
7: []
8: []
9: []

Retrieving values:
Getting key1: value1
Getting key2: value2

After deleting key2:
0: []
1: []
2: []
3: [['key1', 'value1']]
4: []
5: [['key3', 'value3']]
6: []
7: []
8: []
9: []

Trying to retrieve deleted key2:
Getting key2: None
```

---

### **Key Points**
- The hash map uses **chaining** to handle collisions.
- The hash function is simple and based on the sum of ASCII values of the key's characters.
- Operations like `add`, `get`, and `delete` are efficient on average, with a time complexity of **O(1)** for
a well-distributed hash function. However, in the worst case (e.g., all keys hash to the same index),
the time complexity can degrade to **O(n)**.

This implementation is a basic demonstration of how hash maps work and can be extended with features
like dynamic resizing or more sophisticated hash functions.

"""

# =========================================================================================================================== #

# Optimized Version:

"""
To optimize the `HashMap` implementation, we can focus on the following improvements:

1. **Better Hash Function**:
   - The current hash function (`sum(ord(char) for char in str(key)) % self.size`) is simple but prone to collisions
   for keys with similar character sums.
   - Use Python's built-in `hash()` function, which is more robust and efficient.

2. **Dynamic Resizing**:
   - The hash map has a fixed size, which can lead to performance degradation as the number of key-value pairs grows.
   - Implement dynamic resizing to double the size of the hash map when the load factor exceeds a threshold (e.g., 0.7).

3. **Load Factor Monitoring**:
   - Track the number of key-value pairs (`n`) and resize the hash map when the load factor (`n / size`) exceeds a threshold.

4. **Efficient Bucket Handling**:
   - Use a more efficient data structure for buckets (e.g., linked lists or balanced trees) to handle collisions. However,
   for simplicity, we'll stick with lists in this implementation.

5. **Code Cleanup**:
   - Improve readability and maintainability by refactoring the code.

---

### **Optimized Implementation**

Here’s the optimized version of the `HashMap`:

"""

# Implementation in Python:


class HashMap:
    def __init__(self, size=10):
        """
        Initialize the hash map with a given size (default is 10).
        Uses a list of lists (buckets) to handle collisions via chaining.
        """
        self.size = size
        self.map = [[] for _ in range(size)]  # Create empty buckets
        self.count = 0  # Track the number of key-value pairs

    def _get_hash(self, key):
        """
        Compute a hash value for a given key using Python's built-in hash function
        modulo the size of the hash map.
        """
        return hash(key) % self.size

    def _resize(self):
        """
        Resize the hash map when the load factor exceeds 0.7.
        Doubles the size of the hash map and rehashes all key-value pairs.
        """
        old_map = self.map
        self.size *= 2  # Double the size
        self.map = [[] for _ in range(self.size)]
        self.count = 0  # Reset count

        # Rehash all key-value pairs
        for bucket in old_map:
            for key, value in bucket:
                self.add(key, value)

    def add(self, key, value):
        """
        Insert or update a key-value pair in the hash map.
        If the key already exists, update its value.
        """
        if self.count / self.size > 0.7:  # Check load factor
            self._resize()  # Resize if load factor exceeds 0.7

        key_hash = self._get_hash(key)  # Compute the hash index
        bucket = self.map[key_hash]

        # Check if the key already exists in the bucket
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return True

        # If key doesn't exist, add the new key-value pair to the bucket
        bucket.append([key, value])
        self.count += 1  # Increment count
        return True

    def get(self, key):
        """
        Retrieve the value associated with a given key.
        Returns None if the key is not found.
        """
        key_hash = self._get_hash(key)  # Compute hash index
        bucket = self.map[key_hash]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]  # Return the associated value
        return None  # Key not found

    def delete(self, key):
        """
        Remove a key-value pair from the hash map.
        Returns True if the deletion was successful, otherwise False.
        """
        key_hash = self._get_hash(key)  # Compute hash index
        bucket = self.map[key_hash]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)  # Remove the key-value pair
                self.count -= 1  # Decrement count
                return True
        return False  # Key not found

    def __str__(self):
        """
        String representation of the hash map showing the contents of each bucket.
        """
        return "\n".join([f"{i}: {bucket}" for i, bucket in enumerate(self.map)])


# Example usage
if __name__ == "__main__":
    h = HashMap()
    h.add("key1", "value1")
    h.add("key2", "value2")
    h.add("key3", "value3")

    print("Initial hash map:")
    print(h)  # Print the hash map

    print("\nRetrieving values:")
    print("Getting key1:", h.get("key1"))  # Get value for key1
    print("Getting key2:", h.get("key2"))  # Get value for key2

    h.delete("key2")  # Delete key2
    print("\nAfter deleting key2:")
    print(h)

    print("\nTrying to retrieve deleted key2:")
    print("Getting key2:", h.get("key2"))  # Should return None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### 1. **Time Complexity**

- **`_get_hash(key)`**:
  - **Time Complexity**: O(1)
  
  - **Explanation**: The hash function computes the hash value using Python's built-in `hash()` function and performs
  a modulo operation. Both operations are constant time.

- **`add(key, value)`**:
  - **Average Case**: O(1)
  - **Worst Case**: O(n)
  
  - **Explanation**:
    - **Average Case**: If the hash function distributes keys uniformly across the buckets, the average time to insert
    or update a key-value pair is O(1).
    
    - **Worst Case**: If all keys hash to the same bucket (due to poor hash function or high collisions), the time 
    complexity becomes O(n), where `n` is the number of key-value pairs in the bucket.
    
    - **Resizing**: When the load factor exceeds 0.7, the hash map resizes, which involves rehashing all existing key-value pairs.
    This operation is O(n), but it happens infrequently (amortized O(1) per insertion).

- **`get(key)`**:
  - **Average Case**: O(1)
  - **Worst Case**: O(n)
  
  - **Explanation**:
    - **Average Case**: If the hash function distributes keys uniformly, the average time to retrieve a value is O(1).
    - **Worst Case**: If all keys hash to the same bucket, the time complexity becomes O(n), where `n` is the number
    of key-value pairs in the bucket.

- **`delete(key)`**:
  - **Average Case**: O(1)
  - **Worst Case**: O(n)
  
  - **Explanation**:
    - **Average Case**: If the hash function distributes keys uniformly, the average time to delete a key-value pair is O(1).
    - **Worst Case**: If all keys hash to the same bucket, the time complexity becomes O(n), where `n` is the number of
    key-value pairs in the bucket.

- **`_resize()`**:
  - **Time Complexity**: O(n)
  
  - **Explanation**: Resizing involves creating a new hash map with double the size and rehashing all existing key-value pairs.
  This operation is O(n), where `n` is the number of key-value pairs in the hash map.

---

### 2. **Space Complexity**

- **Overall Space Complexity**: O(n)

  - **Explanation**: The space required by the hash map is proportional to the number of key-value pairs `n` and
  the size of the buckets. The buckets are implemented as a list of lists, and the total space used is O(n).

---

### 3. **Load Factor and Resizing**

- The load factor is defined as the ratio of the number of key-value pairs to the size of the hash map. When the load
factor exceeds 0.7, the hash map resizes by doubling its size. This ensures that the average time complexity of
operations remains O(1) in practice.

---

### 4. **Summary**

| Operation         | Average Case | Worst Case | Notes                            |
|-------------------|--------------|------------|----------------------------------|
| `_get_hash(key)`  |   O(1)       |     O(1)   | Constant time                    |
| `add(key, value)` |   O(1)       |     O(n)   | Resizing is amortized O(1)       |
| `get(key)`        |   O(1)       |     O(n)   | Depends on hash distribution     |
| `delete(key)`     |   O(1)       |     O(n)   | Depends on hash distribution     |
| `_resize()`       |   O(n)       |     O(n)   | Rehashing all key-value pairs    |

- **Space Complexity**: O(n)

This implementation provides efficient average-case performance for a hash map, with the worst-case scenario
occurring only under poor hash distribution.

"""

# =========================================================================================================================== #

# Key Improvements:

"""
### **Key Improvements**

1. **Better Hash Function**:
   - Replaced the custom hash function with Python's built-in `hash()` function, which is more efficient and
   less prone to collisions.

2. **Dynamic Resizing**:
   - Added a `_resize()` method to double the size of the hash map when the load factor exceeds 0.7.
   - Rehashes all key-value pairs after resizing.

3. **Load Factor Monitoring**:
   - Tracked the number of key-value pairs (`self.count`) and resized the hash map when the load factor 
   (`self.count / self.size`) exceeds 0.7.

4. **Efficient Bucket Handling**:
   - Used lists for buckets, but the dynamic resizing ensures that buckets remain short on average.

---

### **Time and Space Complexity After Optimization**

1. **Time Complexity**:
   - **`add`, `get`, `delete`**: Average case `O(1)` due to dynamic resizing and better hash function.
   - **`_resize`**: `O(n)` (occurs infrequently due to amortized analysis).

2. **Space Complexity**:
   - **Overall**: `O(n)` (proportional to the number of key-value pairs).
   - **Auxiliary Space**: `O(1)` for operations.

---

### **Example Output**

```
Initial hash map:
0: []
1: []
2: []
3: [['key1', 'value1']]
4: [['key2', 'value2']]
5: [['key3', 'value3']]
6: []
7: []
8: []
9: []

Retrieving values:
Getting key1: value1
Getting key2: value2

After deleting key2:
0: []
1: []
2: []
3: [['key1', 'value1']]
4: []
5: [['key3', 'value3']]
6: []
7: []
8: []
9: []

Trying to retrieve deleted key2:
Getting key2: None
```

This optimized implementation is more efficient and scalable, especially for larger datasets.

"""
