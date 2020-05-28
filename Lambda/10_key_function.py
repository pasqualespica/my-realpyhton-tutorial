

# This function directly influences the algorithm driven by the key function itself. Here are some key functions:

# sort(): list method

# sorted(), min(), max(): built-in functions

# nlargest() and nsmallest(): in the Heap queue algorithm module heapq


ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))  # Lexicographic sort

sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Integer sort
print(sorted_ids)
