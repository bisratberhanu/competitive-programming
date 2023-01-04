def countingValleys(steps, path):
    # Write your code here
    counter1=0
    counter2=0
    for i in path:
        if i=='U':
            counter2+=1
            if counter2==0:
                counter1+=1
            
            
        elif i=='D':
            counter2-=1
    return counter1