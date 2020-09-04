
#should return (2,1)

# * What if we store each weight in the input list as keys? What would be
#   a useful thing to store as the value for each key? 

# * If we store each weight's list index as its value, we can then check
#   to see if the hash table contains an entry for `limit - weight`. If it
#   does, then we've found the two items whose weights sum up to the
#   `limit`!
weights = [2,4,6,7]
weight_limit = 8

#1. make dictionary out of the weights
    #keys = weights  #value = index
weight_dict = {}

for i in range(len(weights)):
    if weights[i] not in weight_dict:
        weight_dict[weights[i]] = [i, weight_limit - weights[i]]
print(weight_dict)

#keys are the weights, values = [index, difference between current weight and weight limit]
# Need to check the dictionary for a key that matches value[1]

#make list of dictionary keys
# loop through that list and calculate difference between current value and weight limit
#  pass in that calculation to the dictionary, if it's there return indices
dict_keys_list = list(weight_dict.keys())
print(dict_keys_list)
for i in dict_keys_list:
    difference = weight_limit - i
    #now we want to check the dictionary for that value
    if difference in weight_dict:
        if difference > i:
            result = (weight_dict[difference][0], weight_dict[i][0])
        else:
            result =(weight_dict[i][0], weight_dict[difference][0])
print(result)
            





