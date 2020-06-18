'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #pointers?
    #left = 0 and right is len of arr
    left,right = 0,len(arr)-1
    while left < right:
        if arr[left] == 0:
            if arr[right] != 0:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
            right -= 1
        else:
            if arr[right] == 0:
                right -= 1
            left += 1
    return arr

    # for i in range(len(arr)):
    #     x = arr[i]

    #     if x != 0:
    #         arr = [x] + arr[:i] + arr[i +1:]
    
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")