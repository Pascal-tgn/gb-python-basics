from json import dump

firms = {}
profits = []

with open("files/task-07.txt") as f:
  for line in f:
    firm, bet, income, expenses = line.split()
    profit = int(income) - int(expenses)
    if profit > 0:
      profits.append(profit)
    firms[firm] = profit

with open("files/task-07.json", "w") as f:
  dump([firms, {"average_profit": sum(profits) / len(profits)}], f)