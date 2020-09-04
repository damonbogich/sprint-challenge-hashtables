def intersection(arrays):
    """
    YOUR CODE HERE
    """
    total_lists = len(arrays)
    #make empty list to return
    result = []
    #make dictionary to store the count of each number
    counter_dict = {}

    for i in arrays:
        for j in i:
            if j not in counter_dict:
                counter_dict[j] = 1
            else:
                counter_dict[j] += 1
    #now we must check dictionary for keys with value = length of arrays
    dict_items_list = list(counter_dict.items())

    for pair in dict_items_list:
        if pair[1] == total_lists:
            result.append(pair[0])


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
