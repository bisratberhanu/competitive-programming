def countSwaps(a):
    counter=0
    sort=False
    while not sort:
        sort=True
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                counter=counter+1
                sort=False
                (a[i],a[i+1])=(a[i+1],a[i])
    return counter
print("Array is sorted in", countSwaps(a), "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
