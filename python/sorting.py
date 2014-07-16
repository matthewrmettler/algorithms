'''
A collection of sorting algorithms implemented in python.
Written by Matthew Mettler.
'''
from random import randint
'''
Insertion sort
Insertion sort is a simple sorting algorithm that builds the final sorted array
 (or list) one item at a time. It is much less efficient on large lists than 
 more advanced algorithms such as quicksort, heapsort, or merge sort. However, 
 insertion sort provides several advantages:

-Simple implementation
-Efficient for (quite) small data sets
-Adaptive (i.e., efficient) for data sets that are already substantially 
    sorted: the time complexity is O(n + d), where d is the number of 
    inversions
-More efficient in practice than most other simple quadratic (i.e., O(n2)) 
    algorithms such as selection sort or bubble sort; the best case 
    (nearly sorted input) is O(n)
-Stable; i.e., does not change the relative order of elements with equal keys
-In-place; i.e., only requires O(1) of additional memory space
-Online; i.e., can sort a list as it receives it

Worst-case performance: O(n^2) comparisons, swaps
Best case performance: O(n) comparisons, O(1) swaps
Average case performance: O(n^2) comparisons, swaps
Worst case space complexity: O(n) total, O(1) auxiliary
'''
def insertion_sort(array):
	for i in range(1, len(array)):
		x = array[i]
		j = i
		while j > 0 and array[j-1] > x:
			array[j] = array[j-1]
			j = j-1
		array[j] = x
	return array

'''
Selection sort is a sorting algorithm, specifically an in-place comparison 
sort.

The algorithm divides the input list into two parts: the sublist of items 
already sorted, which is built up from left to right at the front (left) of 
the list, and the sublist of items remaining to be sorted that occupy the rest 
of the list. Initially, the sorted sublist is empty and the unsorted sublist 
is the entire input list. The algorithm proceeds by finding the smallest 
(or largest, depending on sorting order) element in the unsorted sublist, 
exchanging it with the leftmost unsorted element (putting it in sorted order), 
and moving the sublist boundaries one element to the right.
'''
def selection_sort(array):
	for i in range(len(array)):
		min_i = min(array[i:])
		min_index = array[i:].index(min_i)
		array[i + min_index] = array[i]
		array[i] = min_i
	return array
'''
Bubble sort, sometimes referred to as sinking sort, is a simple sorting 
algorithm that works by repeatedly stepping through the list to be sorted, 
comparing each pair of adjacent items and swapping them if they are in the 
wrong order. 

Worst-case performance: O(n^2)
Best case performance: O(n)
Average case performance: O(n^2)
Worst case space complexity: O(1) auxiliary
'''
def bubble_sort(array):
	n = len(array)
	while n > 0:
		new_n = 0
		for i in range(1, n):
			if array[i-1] > array[i]:
				temp = array[i-1]
				array[i-1] = array[i]
				array[i] = temp
				new_n = i
		n = new_n
	return array

'''
Quicksort is a divide and conquer algorithm. Quicksort first divides a large 
array into two smaller sub-array: the low elements and the high elements. 
Quicksort can then recursively sort the sub-arrays.

The steps are:

-Pick an element, called a pivot, from the array.
-Reorder the array so that all elements with values less than the pivot come 
before the pivot, while all elements with values greater than the pivot come 
after it (equal values can go either way). After this partitioning, the pivot 
is in its final position. This is called the partition operation.
-Recursively apply the above steps to the sub-array of elements with smaller 
values and separately to the sub-array of elements with greater values.

Worst-case performance: O(n^2)
Best case performance: O(n)
Average case performance: O(n log n)
Worst case space complexity: O(n) auxiliary
'''
def quicksort(array):
	if array == [] or len(array) <= 1:
		return array
	else:
		pivot = array[0]
		lesser = quicksort([x for x in array[1:] if x < pivot])
		greater = quicksort([x for x in array[1:] if x >= pivot])
		return lesser + [pivot] + greater

def test_sorts(array):
	print("Original array: " + str(array))
	print("")
	print("Insertion sort: " + str(insertion_sort(list(array))))
	print("Selection sort: " + str(quicksort(list(array))))
	print("")
	print("Quicksort: " + str(quicksort(list(array))))
	print("Bubble sort: " + str(bubble_sort(list(array))))

def random_array(size):
	array = []
	for i in range(size):
		array.append(randint(0,100))
	return array
if __name__ == "__main__":
	test_list = random_array(20)
	test_sorts(test_list)
