# Create an array
array = [1, 2, 3, 4, 5]
print(array)  # Output: [1, 2, 3, 4, 5]

# Access an element in the array
array2 = [1, 2, 3, 4, 5]
print(array2[2])  # Output: 3

# Modify an element in the array
array3 = [1, 2, 3, 4, 5]
array3[2] = 10
print(array3)  # Output: [1, 2, 10, 4, 5]

# Add an element to the end of the array
array4 = [1, 2, 3, 4, 5]
array4.append(6)
print(array4)  # Output: [1, 2, 3, 4, 5, 6]

# Remove the last element from the array
array5 = [1, 2, 3, 4, 5]
array5.pop()
print(array5)  # Output: [1, 2, 3, 4]

# Remove an element at a specific index from the array
array6 = [1, 2, 3, 4, 5]
array6.pop(2)
print(array6)  # Output: [1, 2, 4, 5]

# Remove the first occurrence of a specific element from the array
array7 = [1, 2, 3, 4, 5]
array7.remove(3)
print(array7)  # Output: [1, 2, 4, 5]

# Insert an element at a specific index in the array
array8 = [1, 2, 3, 4, 5]
array8.insert(2, 10)
print(array8)  # Output: [1, 2, 10, 3, 4, 5]

# Clear all elements from the array
array9 = [1, 2, 3, 4, 5]
array9.clear()
print(array9)  # Output: []

# Reverse the order of elements in the array
array10 = [1, 2, 3, 4, 5]
array10.reverse()
print(array10)  # Output: [5, 4, 3, 2, 1]

# Sort the elements in the array in ascending order
array11 = [1, 2, 3, 4, 5]
array11.sort()
print(array11)  # Output: [1, 2, 3, 4, 5]

# Create a copy of the array
array12 = [1, 2, 3, 4, 5]
array13 = array12.copy()
print(array13)  # Output: [1, 2, 3, 4, 5]

# Assign the array to another variable
array14 = [1, 2, 3, 4, 5]
array15 = array14
print(array15)  # Output: [1, 2, 3, 4, 5]

# Extend the array with another iterable
array16 = [1, 2, 3, 4, 5]
array16.extend([6, 7, 8])
print(array16)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Extend the array with another array
array17 = [1, 2, 3, 4, 5]
array18 = [6, 7, 8]
array17.extend(array18)
print(array17)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Concatenate the array with another iterable
array19 = [1, 2, 3, 4, 5]
array20 = array19 + [6, 7, 8]
print(array20)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Get the length of the array
array21 = [1, 2, 3, 4, 5]
print(len(array21))  # Output: 5

# Get the index of the first occurrence of a specific element in the array
array22 = [1, 2, 3, 4, 5]
print(array22.index(3))  # Output: 2

# Count the number of occurrences of a specific element in the array
array23 = [1, 2, 3, 4, 5]
print(array23.count(3))  # Output: 1

# Check if an element is present in the array
array24 = [1, 2, 3, 4, 5]
print(3 in array24)  # Output: True

# Check if an element is not present in the array
array25 = [1, 2, 3, 4, 5]
print(3 not in array25)  # Output: False

# Check if an element is not present in the array
array26 = [1, 2, 3, 4, 5]
print(6 not in array26)  # Output: True

# Check if an element is present in the array
array27 = [1, 2, 3, 4, 5]
print(6 in array27)  # Output: False

# Get a slice of elements from the array
array28 = [1, 2, 3, 4, 5]
print(array28[1:3])  # Output: [2, 3]

# Get a slice of elements from the start to a specific index
array29 = [1, 2, 3, 4, 5]
print(array29[:3])  # Output: [1, 2, 3]

# Get a slice of elements from a specific index to the end
array30 = [1, 2, 3, 4, 5]
print(array30[1:])  # Output: [2, 3, 4, 5]

# Get a slice of elements from a specific start index to a specific end index
array31 = [1, 2, 3, 4, 5]
print(array31[1:4])  # Output: [2, 3, 4]

# Get a slice of elements with a specific step size
array32 = [1, 2, 3, 4, 5]
print(array32[::2])  # Output: [1, 3, 5]

# Get a reversed slice of elements
array33 = [1, 2, 3, 4, 5]
print(array33[::-1])  # Output: [5, 4, 3, 2, 1]

# Get a reversed slice of elements with a specific step size
array34 = [1, 2, 3, 4, 5]
print(array34[::-2])  # Output: [5, 3, 1]

# Get a slice of elements with a specific step size
array35 = [1, 2, 3, 4, 5]
print(array35[1:4:2])  # Output: [2, 4]

# Get an empty slice of elements
array36 = [1, 2, 3, 4, 5]
print(array36[1:4:-1])  # Output: []

# Get a reversed slice of elements
array37 = [1, 2, 3, 4, 5]
print(array37[4:1:-1])  # Output: [5, 4, 3]

# Get a reversed slice of elements with a specific step size
array38 = [1, 2, 3, 4, 5]
print(array38[4:1:-2])  # Output: [5, 3]

# Get an empty slice of elements with a specific step size
array39 = [1, 2, 3, 4, 5]
print(array39[1:4:-2])  # Output: []

# Get a slice of elements with a specific step size
array40 = [1, 2, 3, 4, 5]
print(array40[1:4:1])  # Output: [2, 3, 4]

# Get a slice of elements with a specific step size
array41 = [1, 2, 3, 4, 5]
print(array41[1:4:2])  # Output: [2, 4]
