# Implementation in Python:


def permutations(s):
    """
    Generate all possible permutations of the input string.

    Args:
        s: The input string to generate permutations for.

    Returns:
        A list containing all possible permutations of the input string.
    """

    # Base case: if the string has only one character,
    # the only permutation is the string itself
    if len(s) == 1:
        return [s]

    # This will store all permutations we generate
    result = []

    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Create a new string without the current character
        # by combining the part before and after it
        remaining = s[:i] + s[i + 1 :]

        # Recursively generate all permutations of the remaining string
        for perm in permutations(remaining):
            # Combine the current character with each permutation
            # of the remaining characters and add to result
            result.append(char + perm)

    return result


# Test Case:

print(permutations("abc"))
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
