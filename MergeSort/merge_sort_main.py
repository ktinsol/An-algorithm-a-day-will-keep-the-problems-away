from MergeSort.merge_sort import MergeSort
from MergeSort.utils.random_array_generator import RandomArrayGenerator

random_array = RandomArrayGenerator.generate_random_array()

print(random_array)

sorted_array = MergeSort.merge_sort_array(random_array)

print(sorted_array)