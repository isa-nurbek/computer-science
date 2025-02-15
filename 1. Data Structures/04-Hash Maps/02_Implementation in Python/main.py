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

"""
Output:

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

# Big O:

"""
## Time and Space Complexity Analysis:

The `HashMap` implementation provided uses **chaining** to handle collisions, where each bucket in the
hash map is a list of key-value pairs. Below is an analysis of the **time and space complexity**
for the operations in your implementation:

---

### **Time Complexity**

1. **`_get_hash(key)`**:
   - Computes the hash by summing the ASCII values of the characters in the key and taking modulo with the
   size of the hash map.
   - **Time Complexity**: `O(k)`, where `k` is the length of the key. This is because we iterate over each
   character in the key to compute the hash.

2. **`add(key, value)`**:
   - Computes the hash index using `_get_hash(key)`.
   - Iterates through the bucket (list) at the computed index to check if the key already exists.
     - If the key exists, it updates the value.
     - If the key doesn't exist, it appends the new key-value pair to the bucket.
   - **Time Complexity**:
     - Best case: `O(1)` (if there are no collisions and the bucket is empty).
     - Worst case: `O(n)` (if all keys hash to the same bucket, leading to a linear search through the bucket).

3. **`get(key)`**:
   - Computes the hash index using `_get_hash(key)`.
   - Iterates through the bucket at the computed index to find the key.
   - **Time Complexity**:
     - Best case: `O(1)` (if there are no collisions and the key is the first element in the bucket).
     - Worst case: `O(n)` (if all keys hash to the same bucket, leading to a linear search through the bucket).

4. **`delete(key)`**:
   - Computes the hash index using `_get_hash(key)`.
   - Iterates through the bucket at the computed index to find and remove the key-value pair.
   - **Time Complexity**:
     - Best case: `O(1)` (if there are no collisions and the key is the first element in the bucket).
     - Worst case: `O(n)` (if all keys hash to the same bucket, leading to a linear search through the bucket).

---

### **Space Complexity**

1. **Overall Space Complexity**:
   - The space used by the hash map is proportional to the number of buckets (`size`) and the number of key-value pairs stored.
   - **Space Complexity**: `O(size + n)`, where `size` is the number of buckets and `n` is the number of key-value pairs.

2. **Auxiliary Space for Operations**:
   - All operations (`add`, `get`, `delete`) use a constant amount of auxiliary space (`O(1)`) beyond the space required
   to store the hash map itself.

---

### **Example Analysis**

In our example usage:

1. **Adding keys**:
   - `h.add("key1", "value1")`: Computes hash for `"key1"` and adds it to the appropriate bucket.
   - `h.add("key2", "value2")`: Computes hash for `"key2"` and adds it to the appropriate bucket.
   - `h.add("key3", "value3")`: Computes hash for `"key3"` and adds it to the appropriate bucket.
   - **Time Complexity**: `O(1)` for each addition (assuming no collisions).

2. **Retrieving values**:
   - `h.get("key1")`: Computes hash for `"key1"` and retrieves the value from the bucket.
   - `h.get("key2")`: Computes hash for `"key2"` and retrieves the value from the bucket.
   - **Time Complexity**: `O(1)` for each retrieval (assuming no collisions).

3. **Deleting a key**:
   - `h.delete("key2")`: Computes hash for `"key2"` and removes it from the bucket.
   - **Time Complexity**: `O(1)` (assuming no collisions).

4. **Retrieving a deleted key**:
   - `h.get("key2")`: Computes hash for `"key2"` and finds no matching key in the bucket.
   - **Time Complexity**: `O(1)` (assuming no collisions).

---

### **Optimization Considerations**

1. **Hash Function**:
   - The current hash function (`sum(ord(char) for char in str(key)) % self.size`) is simple but
   may lead to collisions if keys have similar character sums.
   - Consider using a more robust hash function (e.g., Python's built-in `hash()` function or a cryptographic hash function).

2. **Dynamic Resizing**:
   - The hash map has a fixed size (`size=10`). If the number of key-value pairs grows significantly, the buckets
   will become longer, degrading performance.
   - Implement dynamic resizing (e.g., doubling the size of the hash map when the load factor exceeds a threshold).

3. **Load Factor**:
   - Monitor the load factor (`n / size`) and resize the hash map if it exceeds a certain threshold (e.g., 0.7).

"""

# ******************************************************************************************************************************* #

# Code Explanation:

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

# ****************************************************************************************************************************** #

"""
                                       *** Optimized Version ***

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
