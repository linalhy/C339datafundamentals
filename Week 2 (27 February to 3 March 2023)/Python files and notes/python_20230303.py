#%%

class Node:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None
     
    def printTree(self):
        if self.leftChild:
            self.leftChild.printTree()
        print(self.data)
        if self.rightChild:
                self.rightChild.printTree()

    def insert(self, data):
        """
        Insert function will insert a node into tree.
        """
        if data < self.data:  #if the inserted data is smaller than the data, attach to the inserted data to the left.
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        else: 
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def search(self, value):
        """
        Search function will search a node in tree.
        """
        if value == self.data:
            return str(value) + " is found in BST" # if value == value in node, return 'value' is found in BST.
        elif value < self.data:
            if self.leftChild:
                return self.leftChild.search(value) # if the inserted data(value) < value in node, search towards the left child
            else:
                return str(value) + " is not found in BST" # if value 
        else:
            if self.rightChild:
                return self.rightChild.search(value) # if value > node, search towards the right child.
            else:
                return str(value) + " is not found in BST" # if value is not found, print 'value' is not found in BST.

root = Node(27)

root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
print(root.search(10))
print(root.search(7))

root.printTree()

# %%
"""
Bubble Sort is the simplest sorting algorithm 
that works by repeatedly swapping the adjacent elements 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   if they are in the wrong order.
"""
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] == arr[j+1], arr[j] # if the array of j is greater than the array of j+1, swap the positions

bubble_sort([14, 27, 35, 10, 19])
# %%

def mergesort(arr):
    """
    if the array size is greater than one, there is nothing to do
    """
    if len(arr) == 1:
        return arr
    
    # Divide the array in two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = mergesort(left_half)
    right_sorted = mergesort(right_half)

    # Merge the halves
    i = j = 0
    result = []
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            result.append(left_sorted[i])
            i = i + 1
        else:
            result.append(right_sorted[j])
            j = j + 1
        result += left_sorted[i:]
        result += right_sorted[j:]
    return result

mergesort([14, 27, 35, 10, 19])
   
# %%

def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    # Choose the pivot element
    pivot = arr[0]

    # Partition the array in two sub arrays
    lesser = [i for i in arr[1:] if i <= pivot] 
    right = [i for i in arr[1:] if i > pivot]
    return quicksort(lesser) + [pivot] + quicksort(right)

quicksort([14, 27, 35, 10, 19])

# %%
"""
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place
in each iteration. 

"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # overwrites i with j
            j = j - 1
        arr[j + 1] = key
    return arr

print(insertion_sort([5, 4, 3, 2, 1]))

# %%
"""
Problem 1 Description
You are given a constant array A.

You are required to return another array which is the reversed form of the input array.
"""
"""
Example Inputs and Outputs

Input 1: A = [1,2,3,2,1]
Output 1: [1,2,3,2,1] 

Input 2: A = [1,1,10]
Output 2: [10,1,1]
"""

"""Problem Constraints
1 <= A.size() <= 10000
1 <= A[i] <= 10000

Input Format
First argument is a constant array A.

Output Format
Return an integer array."""

"""def reversed(arr):
    return arr[::-1]"""

# Solution 1:
def reversed(arr):
    res = [None] * len(arr)
    i = len(arr)
    j = 0
    while i > 0:
        res[j] = arr[i]
        j = j + 1
        i = i - 1
    return res
reversed([1, 2, 3, 4, 5])

# Solution 2
def reversed2(arr):
    result = []
    while len(arr) > 0:
        result.append(arr.pop())
    return result

reversed2([1,2,3,4,5])

# %%
"""
Problem 2 Description:
Given an integer array A of size N and an integer B, 
you have to return the same array after rotating it B times towards the right.
"""
"""
Example Output
Output 1:

[3, 4, 1, 2]
Output 2:

[6, 2, 5]

Example Explanation
Explanation 1: Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]

Explanation 2: Rotate towards the right 1 time - [2, 5, 6] => [6, 2, 5]

Problem Constraints
1 <= N <= 105
1 <= A[i] <=109
1 <= B <= 109


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the array A after rotating it B times to the right


Example Input
Input 1:

A = [1, 2, 3, 4]
B = 2
Input 2:

A = [2, 5, 6]
B = 1
"""
# Solution 1:
def rotate1(arr, times):
    for i in range(times):
        arr.insert(0, arr.pop())
    return arr

rotate1([1,2,3,4,5], 2)

# Solution 2: Identical to solution 2, but using list comprehension

def rotate2(arr, times):
    [arr.insert(0, arr.pop()) for i in range(times)]
    return arr

rotate2([1,2,3,4,5], 2)

# %%
"""
Problem 3 Description:
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 109

Input Format
The first argument is an integer array A.

Output Format
Return the second largest element. If no such element exist then return -1.

Example Input
Input 1:
A = [2, 1, 2] 
Output 1:
 1 

Input 2:
 A = [2]
Output 2:
 -1 

Example Explanation
Explanation 1:
First largest element = 2
Second largest element = 1

Explanation 2:
There is no second largest element in the array.
"""

# Solution 1:
def secondLargest1(arr):
    if len(arr) < 2:
        return "-1"
    else:
        arr.sort(reverse=True)
        for i in range(len(arr)):
            if arr[i] != arr[i+1]:
                return arr[i+1]

secondLargest1([1,8,5,10,10,10, 7])
secondLargest1([3])

# Solution 2:
def secondLargest2(arr):
    if len(arr) < 2:
        return "-1"
    else:
        no_rep_array = list(set(arr))
        no_rep_array.remove(max(no_rep_array))
        return max(no_rep_array)

secondLargest2([1,8,5,10,10,7])


