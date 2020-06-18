'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    length = len(arr)
    result = [1]*length
    l,r = 1,1
    for i in range(length):
        result[i] *= l
        result[length-1-i] *= r
        l *= arr[i]
        r *= arr[length-1-i]
        print(result, l, r)
    return result

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 5, 7, 1]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
