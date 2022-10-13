#the function returns a frequency array of each value of arr list
def countingSort(arr):
    result=[]
    for i in range(100):
        result.append(0)
    for values in arr:
        
        c=arr.count(values)
        result[values]=c
    return result
    
