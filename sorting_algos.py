
def bubble_sort(lst): # O(n^2)
	swap_happened = True
	while swap_happened:
		# print("Status: ",str(lst))
		swap_happened = False
		for i in range(len(lst)-1):
			if lst[i] > lst[i+1]:
				swap_happened = True
				lst[i],lst[i+1] = lst[i+1],lst[i]

def selection_sort(lst):
	marker = 0
	while marker < len(lst):
		# print("Status: ",str(lst))
		for i in range(marker,len(lst)):
			if lst[marker] > lst[i]:
				lst[marker],lst[i] = lst[i],lst[marker]
		marker += 1
	return f"Sorted list: {lst}"


def insertion_sort(lst):
	for i in range(1,len(lst)):
		if lst[i] < lst[i-1]:
			j = i
			while j > 0 and lst[j] < lst[j-1]:
				lst[j],lst[j-1] = lst[j-1],lst[j]
				j -= 1


def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]

		# Recursively call the merge sort function
		merge_sort(left)
		merge_sort(right)
		# Counter for left and right list respectively
		i = 0
		j = 0
		# Counter for the main list
		k = 0

		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1

			else:
				arr[k] = right[j]
				j += 1
			k += 1
		# appending the remaining elements of left and right
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1



def quick_sort(lst):

	if len(lst) < 2:
		return lst[:]

	else:
		pivot = lst[-1]
		smaller = []
		equal = []
		greater = []

		for i in lst:
			if i < pivot:
				smaller.append(i)
			elif i == pivot:
				equal.append(i)
			else:
				greater.append(i)

		return quick_sort(smaller)+ equal + quick_sort(greater)

