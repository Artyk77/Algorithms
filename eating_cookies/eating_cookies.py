#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  cache = cache or [0 for i in range(n+1)]
  if n > 0: #base cases
    cache[0], cache[1] = 1, 1
  else:
    cache[0] = 1

  if cache[n] == 0:
    for i in range(1, min(n+1,4)):   

      cache[n] += eating_cookies(n - i, cache)

  return cache[n]

if __name__ == "__main__":
    if len(sys.argv) > 1:
      num_cookies = int(sys.argv[1])
      print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
else:
    print('Usage: eating_cookies.py [num_cookies]')