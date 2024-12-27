def RevArray(arr):
    left =0
    n=len(arr)
    right=n-1
    while left<=right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
if __name__=="__main__":
    arr=[1,2,3,4,5]
    RevArray(arr)
    for i in range (len(arr)):
        print(arr[i], end=" ")
        
                