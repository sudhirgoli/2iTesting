def counting_sum_pairs(new_array, x):
    """
    function for counting sum pairs
    """

    i=0
   
    while(i<len(new_array)):
        if (x-(new_array[i])) in  new_array[i+1:]
            new_array.pop(new_array.index(x-new_array[i]))
            i+=1
        else:
            new_array.pop(i)
            
    return len(new_array)


print(counting_sum_pairs([1,1,10,32,41], 42))
print(counting_sum_pairs([0,15,32,2000,15000], 15))

print(counting_sum_pairs([3,4,5,6], 1))
