# Given two sets:
'''python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
```
Find the union and intersection'''

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}


union_set = set_a.union(set_b)


intersection_set = set_a.intersection(set_b)

print("Union:", union_set)
print("Intersection:", intersection_set)
