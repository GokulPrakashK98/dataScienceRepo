def assignment(new_list, i, old_list, j):
    """
    Assigns the value from old_list[j] to new_list[i].
    
    Parameters:
    new_list (list): The list to assign the value to.
    i (int): The index in the new_list where the value should be assigned.
    old_list (list): The list from which the value is taken.
    j (int): The index in the old_list from which the value is taken.
    
    Returns:
    None
    """
    new_list[i] = old_list[j]


def merge_sort(array):
    """
    Sorts an array using the merge sort algorithm.
    
    Parameters:
    array (list): The list to be sorted.
    
    Returns:
    None: The function sorts the list in place.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        l = r = i = 0

        while l < len(left_half) and r < len(right_half):
            if left_half[l] <= right_half[r]:
                assignment(new_list=array, i=i, old_list=left_half, j=l)
                l += 1
            else:
                assignment(new_list=array, i=i, old_list=right_half, j=r)
                r += 1
            i += 1

        while l < len(left_half):
            array[i] = left_half[l]
            l += 1
            i += 1

        while r < len(right_half):
            array[i] = right_half[r]
            r += 1
            i += 1


def plot_list(array, title):
    """
    Plots the elements of a list.
    
    Parameters:
    array (list): The list to be plotted.
    title (str): The title of the plot.
    
    Returns:
    None
    """
    import matplotlib.pyplot as plt
    x = range(len(array))
    plt.plot(x, array)
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    # Example usage
    sample_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Given array is:")
    plot_list(sample_list, 'Given Array')
    merge_sort(sample_list)
    print("Sorted array is:")
    plot_list(sample_list, 'Sorted Array')
