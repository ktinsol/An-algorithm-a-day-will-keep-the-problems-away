class MergeSort:

    @staticmethod
    def merge_sort_array(array):

        # Divide the array into subsets
        subsets = MergeSort.divide_array(array)

        # Conquer the subsets by merging them
        sorted_array = MergeSort.conquer_subsets(subsets)

        # Return the sorted array
        return sorted_array

    @staticmethod
    def divide_array(array):
        array_a = []
        array_b = []
        if len(array) <= 1:
            return array
        else:
            for i, element in enumerate(array):
                if i < (len(array) // 2):
                    array_a.append(element)
                else:
                    array_b.append(element)

        return MergeSort.divide_array(array_a), MergeSort.divide_array(array_b)

    @staticmethod
    def conquer_subsets(subsets):

        # Check if the subset has been conquered fully
        if len(subsets) == 1:
            return subsets

        # Find the smallest subsets
        subset_a_index = MergeSort.find_smallest_subset(subsets)
        subset_b_index = MergeSort.find_smallest_subset(subsets.pop(subset_a_index))
        subset_a = subsets[subset_a_index]
        subset_b = subsets[subset_b_index]

        # Combine the smallest subsets
        combined_subset = MergeSort.combine_subsets(subset_a, subset_b)

        return MergeSort.conquer_subsets(combined_subset)

    @staticmethod
    def find_smallest_subset(subsets):
        min_value = len(subsets[0])
        min_index = 0
        for i in range(len(subsets)):
            if len(subsets[i]) < min_value:
                min_value = len(subsets[i])
                min_index = i
        return min_index

    @staticmethod
    def combine_subsets(subset_a, subset_b):
        combined_subset = []
        limit = len(subset_a) if len(subset_a) > len(subset_b) else subset_b
        for i, j in range(limit):
            if subset_a[i] is None and subset_b[j] is None:
                return combined_subset
            elif subset_a[i] is None and subset_b[j] is not None:
                combined_subset.append((subset_b[j]))
                j += 1
            elif subset_b is None and subset_a[i] is not None:
                combined_subset.append(subset_a[i])
                i += 1
            elif subset_a[i] >= subset_b[j]:
                combined_subset.append(subset_a[i])
                i += 1
            else:
                combined_subset.append((subset_b[j]))
                j += 1



