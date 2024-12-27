QUESTION : 

You are given an array of integers arr[]. Your task is to reverse the given array.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.

SOLUTION :

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
        
                
