# Code Explanation: Hash Maps Implementation in Python

The provided code defines a simple implementation of a **hash map** (also known as a hash table) in Python. A hash map is a data structure that stores key-value pairs and allows for efficient insertion, retrieval, and deletion of these pairs. Below is a detailed explanation of how the code works:

---

## **`HashMap` Class**

```python
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
```

## **1. Class Definition: `HashMap`**

The `HashMap` class is the core of the implementation. It uses **chaining** to handle collisions, meaning that each bucket in the hash map can store multiple key-value pairs in a list.

---

### **2. Constructor: `__init__`**

```python
def __init__(self, size=10):
    self.size = size
    self.map = [[] for _ in range(size)]
```

- **Purpose**: Initializes the hash map with a given size (default is 10).
- **How it works**:
  - `self.size`: Stores the size of the hash map (number of buckets).
  - `self.map`: A list of lists (buckets) where each bucket is initially empty. For example, if `size = 10`, `self.map` will be a list of 10 empty lists.

---

### **3. Hash Function: `_get_hash`**

```python
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

```python
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

```python
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

```python
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

```python
def __str__(self):
    return "\n".join([f"{i}: {bucket}" for i, bucket in enumerate(self.map)])
```

- **Purpose**: Provides a string representation of the hash map for easy visualization.
- **How it works**:
  - Iterates through each bucket in `self.map` and formats it as `index: [key-value pairs]`.
  - Joins the formatted strings with newline characters for readability.

---

### **8. Example Usage**

```python
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
   - For example, if `key1` and `key4` both hash to index `3`, the bucket at index `3` will contain `[[key1, value1], [key4, value4]]`.

3. **Operations**:
   - **Insert/Update**: The hash map checks if the key already exists in the bucket. If it does, the value is updated. Otherwise, the new key-value pair is appended to the bucket.
   - **Retrieve**: The hash map searches the bucket for the key and returns the associated value if found.
   - **Delete**: The hash map searches the bucket for the key and removes the key-value pair if found.

---

### **Output Example**

For the provided example usage, the output might look like this:

```text
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
- Operations like `add`, `get`, and `delete` are efficient on average, with a time complexity of **O(1)** for a well-distributed hash function. However, in the worst case (e.g., all keys hash to the same index), the time complexity can degrade to **O(n)**.

This implementation is a basic demonstration of how hash maps work and can be extended with features like dynamic resizing or more sophisticated hash functions.

---

## **Big O Analysis:**

### Time and Space Complexity Analysis

#### **Time Complexity**

1. **`_get_hash(key)`**:
   - **Time Complexity**: O(k), where `k` is the length of the key (string).
   - **Explanation**: The hash function computes the sum of ASCII values of each character in the key. This requires iterating through each character of the key once.

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
   - **Explanation**: Similar to `add`, computing the hash is O(k), and searching the bucket is O(α) on average (or O(n) in the worst case).

4. **`delete(key)`**:
   - **Average Case**: O(1 + α).
   - **Worst Case**: O(n).
   - **Explanation**: Same as `get` and `add`, since deletion involves searching the bucket first.

#### **Space Complexity**

1. **Overall Space**:
   - **Space Complexity**: O(n + m), where `n` is the number of key-value pairs stored and `m` is the size of the internal bucket array (`self.size`).
   - **Explanation**:
     - The hash map stores `n` key-value pairs distributed across `m` buckets.
     - Each bucket is a list, and the overhead of the bucket array is O(m).
     - In practice, if the hash map is resized dynamically (not implemented here), `m` is proportional to `n`, making the space complexity O(n).

#### **Notes on Performance**

- The performance relies heavily on the hash function distributing keys uniformly across buckets. If many keys collide, the worst-case time complexity degrades to O(n).
- This implementation does not handle resizing (dynamic rehashing), so the load factor (`n/m`) can grow unbounded, leading to poor performance if many keys are added.
- The `_get_hash` function is simple but may not distribute keys uniformly for certain datasets (e.g., keys with the same characters in different orders will collide).

#### **Improvements**

1. **Dynamic Resizing**: Double the size of the bucket array and rehash all elements when the load factor exceeds a threshold (e.g., 0.7). This keeps α bounded and maintains average O(1) operations.
2. **Better Hash Function**: Use a more sophisticated hash function (e.g., Python's built-in `hash()` or a cryptographic hash) to reduce collisions.
3. **Open Addressing**: Alternative to chaining, where collisions are resolved by probing (linear/quadratic/double hashing). This can be more cache-friendly but requires careful handling of deletions.

---

### Optimized Version

To optimize the `HashMap` implementation, we can focus on the following improvements:

1. **Better Hash Function**:
   - The current hash function (`sum(ord(char) for char in str(key)) % self.size`) is simple but prone to collisions for keys with similar character sums.
   - Use Python's built-in `hash()` function, which is more robust and efficient.

2. **Dynamic Resizing**:
   - The hash map has a fixed size, which can lead to performance degradation as the number of key-value pairs grows.
   - Implement dynamic resizing to double the size of the hash map when the load factor exceeds a threshold (e.g., 0.7).

3. **Load Factor Monitoring**:
   - Track the number of key-value pairs (`n`) and resize the hash map when the load factor (`n / size`) exceeds a threshold.

4. **Efficient Bucket Handling**:
   - Use a more efficient data structure for buckets (e.g., linked lists or balanced trees) to handle collisions. However, for simplicity, we'll stick with lists in this implementation.

5. **Code Cleanup**:
   - Improve readability and maintainability by refactoring the code.

---

### **Optimized Implementation**

Here’s the optimized version of the `HashMap`:

```python
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
```

---

### **Example Output**

```plaintext
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

## **Big O Analysis:**

### Time and Space Complexity Analysis of Optimized Hash Maps Class

1. **`_get_hash(key)`**:
   - **Time Complexity**: O(1)
   - **Explanation**: This method computes the hash of the key and performs a modulo operation, both of which are constant-time operations.

2. **`add(key, value)`**:
   - **Average Case**: O(1)
   - **Worst Case**: O(n)
   - **Explanation**:
     - **Average Case**: Assuming a good hash function and a low load factor, the key-value pair is inserted into the bucket (a list) in constant time. Resizing (when the load factor exceeds 0.7) is amortized O(1) because it happens infrequently and the cost is spread out over many insertions.
     - **Worst Case**: If all keys hash to the same bucket, the bucket becomes a list of size `n`, and inserting a new key-value pair requires traversing the entire list to check for duplicates, resulting in O(n) time.

3. **`get(key)`**:
   - **Average Case**: O(1)
   - **Worst Case**: O(n)
   - **Explanation**:
     - **Average Case**: With a good hash function, the key is found in the bucket in constant time.
     - **Worst Case**: If all keys hash to the same bucket, the bucket is a list of size `n`, and searching for the key requires O(n) time.

4. **`delete(key)`**:
   - **Average Case**: O(1)
   - **Worst Case**: O(n)
   - **Explanation**: Similar to `get(key)`, deletion involves finding the key in the bucket and then removing it. In the worst case, this requires traversing the entire bucket.

5. **`_resize()`**:
   - **Time Complexity**: O(n)
   - **Explanation**: Resizing involves creating a new hash map of double the size and rehashing all existing `n` key-value pairs. Each insertion into the new hash map is O(1) on average, so the total time is O(n).

### Space Complexity Analysis

1. **Overall Space Complexity**:
   - **Space Complexity**: O(n)
   - **Explanation**: The space used by the hash map is proportional to the number of key-value pairs (`n`) and the size of the underlying array (`size`). Since `size` is resized to maintain a load factor <= 0.7, the space used is O(n).

2. **`_resize()`**:
   - **Space Complexity**: O(n)
   - **Explanation**: During resizing, a new array of double the size is created, and all existing key-value pairs are rehashed into it. This temporarily uses O(2 * size) space, but since size is proportional to `n`, this is O(n).

### Summary Table

| Operation       | Average Case Time | Worst Case Time | Space Complexity |
|-----------------|-------------------|-----------------|------------------|
| `_get_hash`     | O(1)              | O(1)            | O(1)             |
| `add`           | O(1)              | O(n)            | O(n)             |
| `get`           | O(1)              | O(n)            | O(1)             |
| `delete`        | O(1)              | O(n)            | O(1)             |
| `_resize`       | O(n)              | O(n)            | O(n)             |
| **Overall**     | -                 | -               | O(n)             |

### Notes

- The **average case** assumes a good hash function that distributes keys uniformly across buckets, keeping the bucket sizes small.
- The **worst case** occurs when all keys collide in the same bucket, degrading the performance to that of a linked list (O(n) for search, insert, and delete).
- The **resizing operation** is triggered when the load factor exceeds 0.7, ensuring that the average case performance remains O(1) by keeping the load factor low. The amortized cost of resizing is O(1) per insertion.
- The **space complexity** is dominated by the storage of the key-value pairs and the underlying array, which grows linearly with the number of elements.

This optimized implementation is more efficient and scalable, especially for larger datasets.
