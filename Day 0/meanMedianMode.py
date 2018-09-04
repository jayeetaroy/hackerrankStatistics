def my_mean(length, values):
    totalSum=0
    mean=0
    for num in values:
        totalSum+=num
        
    mean=totalSum/length
    return mean


def my_median(length, values):
    values=sorted(values)
    median=0
    if(length%2==0):
        medianIndex=int(length/2)
        median=(values[medianIndex-1]+values[medianIndex])/2
    else:
        medianIndex=length//2+1
        median=values[medianIndex]
        
    return median
        
def my_mode(values):
    values=sorted(values)
    modeDict={}
    for num in values:
        if(num in modeDict.keys()):
            modeDict[num]+=1
        else:
            modeDict[num]=1
    
    maxOccurances=max(modeDict.values())
    maxOccurNumList=[]
    for k, v in modeDict.items():
        if(v==maxOccurances):
            maxOccurNumList.append(k)
    return min(maxOccurNumList)
            


        
    

size = int(input())
numbers = list(map(int, input().split()))
print(my_mean(size, numbers))
print(my_median(size, numbers))
print(my_mode(numbers))
