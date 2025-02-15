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
