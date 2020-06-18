'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for each in arr:
        #
        if arr.count(each) == 1:
            return each
    
    return -1

    # no_nups = []
    # for num in narr: #0(n)
    #     if num not in no_nups:
    #         no_nups.append(num)
    #     else:
    #         no_nups.remove(num)
    # return no_nups[0]

#     counts = {}

#     for num in arr:
#         if num in counts:
#             num += 1
#         else:
#             num = 1
# #returns interable of tuples?
#     for k, v in counts.items()
#         if v ==1:
#             return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")