def moveZeroes(arr):
    
    
    count=0
    for i in range(len(arr)):
        if arr[i]!=0:
             arr[i],arr[count]=arr[count],arr[i]
             count+=1
             
if __name__=="__main__":
    arr=[13,0,4,5,8,2]
    moveZeroes(arr)
    for num in arr:
        print(num , end=" ")
             
            
       