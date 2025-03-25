#var
arr=[3,5,1,2,4,7]

#function to handle target sum and the given array
def nine_sum(arr,target_sum):
    #storing new set/pair of adding to sum numbers
    pair=set()
    visited=set()
    for i in arr:
        complement=target_sum-i #number that completes the target sum to each element
        #check complement availability in the arr and no element repetition
        if not (complement in pair and i in pair) and complement in arr and complement!=i:
            pair.add((complement,i))
            #ensure no redundant sets
            arr.remove(i)
        else:
            continue

    return pair

#call the function and input the var arr    
print(nine_sum(arr,4))