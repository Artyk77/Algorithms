# !/usr/bin/python

# import argparse

# def find_max_profit(prices):
#   pass


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

def max_profit(max_array): 
  profit = 0
  for i in range(len(price_array)):
    buy = price_array[i]
    for j in range(i + 1, len(price_array)):
      sell = price_array[j]
      if profit < sell - buy:
        profit = sell - buy #update value of profit
  return profit 

arr = [10, 7, 5, 8, 11, 9]
print(max_profit(arr))