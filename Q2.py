# Q2: Student Marks Analysis (no loops or functions)

marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

# Display both collections and their types
print("List :", marks_list, type(marks_list))
print("Tuple:", marks_tuple, type(marks_tuple))

# Highest and lowest marks using built-in operations
print("Highest mark:", max(marks_list))
print("Lowest mark :", min(marks_list))

# Count marks >= 40 (True counts as 1, False as 0, so no loop is needed)
passed_count = ((marks_list[0] >= 40) + (marks_list[1] >= 40) +
                (marks_list[2] >= 40) + (marks_list[3] >= 40) +
                (marks_list[4] >= 40))
print("Students with at least 40 marks:", passed_count)

# All marks valid if the lowest is >= 0 and the highest is <= 100
all_valid = min(marks_list) >= 0 and max(marks_list) <= 100
print("All marks within 0-100:", all_valid)

# Changing one element in each collection
marks_list[1] = 50          # works
print("List after change:", marks_list)

# marks_tuple[1] = 50       # uncommenting this raises:
#                           # TypeError: 'tuple' object does not support item assignment
print("Tuple unchanged:", marks_tuple)

# Observation: A list is mutable, so its elements can be changed in place.
# A tuple is immutable, so assigning to an element raises a TypeError.
# Use tuples for data that should not change, lists for data that may change.
