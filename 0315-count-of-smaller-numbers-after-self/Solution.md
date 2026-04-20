# Binary Search +  Maintaining Sorting || Beats 90.23%

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The intuition of this problem is not that hard.

> How many numbers are smaller than to the right of each number? 


but given the constraints brute force approach would definitely TLE.

### Instead, we do the following,

Instead of looking **right every time**, flip the direction:

> Process from **right → left**

Now:

* when you’re at a number, everything you’ve already seen = its “right side”.



### Notice

You don’t just store the right side — you store it **sorted**

Why?

Because:

> If it’s sorted, you can instantly count how many elements are smaller



# 🔹 Approach 

### 1. Go from right to left

```python id="px8qpd"
for n in reversed(nums):
```



### 2. Maintain a sorted structure

```python id="o4y4nq"
sorted_list = SortedList()
```

This always contains:

> all elements to the right, in sorted order



### 3. Count smaller elements using binary search

```python id="9mzn3s"
sorted_list.bisect_left(n)
```

 This gives:

> number of elements strictly smaller than `n`

Because:

* it returns the first position where `n` can go
* everything before that is `< n`



### 4. Insert the current number

```python id="sb3vkp"
sorted_list.add(n)
```

So future elements can use it



### 5. Reverse the result

Because we processed backwards




# 🔹 Complexity

* insert → O(log n)
* search → O(log n)
* total → **O(n log n)**


# Code
```python3 []
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        sorted_list = SortedList()
        ans = []
        for n in reversed(nums):
            ans.append(sorted_list.bisect_left(n))
            sorted_list.add(n)
        ans.reverse()
        return ans
```