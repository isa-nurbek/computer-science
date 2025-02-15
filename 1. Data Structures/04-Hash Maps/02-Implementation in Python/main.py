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
