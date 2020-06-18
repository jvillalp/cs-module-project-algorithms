'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
       #check for negative values
    if n < 0:
        #getting to a negative number means we didnt find a way to eat cookies
        return 0
    #base case where there are no more cookies
    if n == 0:
        #geting to 0, we found a way to eat our cookies
        return 1

    #check if the cache exists 
    #check if n is in cache

    #create an isinstance condition with dict
    #The next reason not to use type() is the lack of support for inheritance.
    if cache is None or not isinstance(cache, dict):
        cache = {}
    #if cache is None (no cahche yet), create a cache
    if n in cache:
        return cache[n]

    #this represents our recursive case
    #3 possible decisions
    #eat 1 cookie, 2 cookies, 3 cookies
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
