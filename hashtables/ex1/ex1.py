def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}

    for i in range(len(weights)):
        #takes care of test case 2
        if (weights[i] in weight_dict) and (weights[i] == weight_dict[weights[i]][1]):
            return (i, weight_dict[weights[i]][0])

        weight_dict[weights[i]] = [i, limit - weights[i]]

    
    for i in weights:
        difference = limit - i

        if difference in weight_dict:
            if difference > i:
                result = (weight_dict[difference][0], weight_dict[i][0])
                
                return result
            elif difference == 0:
                result = (weight_dict[difference][0], weight_dict[i][0])
                
                return result
            else:
                result = (weight_dict[i][0], weight_dict[difference][0])
                
                return result
    return None
