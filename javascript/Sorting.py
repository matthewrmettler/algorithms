'''
A collection of sorting algorithms implemented in python.
Written by Matthew Mettler.
'''

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
'''
def insertion_sort(array):
	for i in range(1, len(array)):
		x = array[i]
		j = i
		while j > 0 and array[j-1] > x:
			array[j] = array[j-1]
			j = j-1
		array[j] = x



test_list = [x for x in range(50, 10, -3)]
print(test_list)
insertion_sort(test_list)
print(test_list)