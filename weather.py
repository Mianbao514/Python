price = 1,000,000
credit = true
if credit:
  final = 0.2 * price
  total = price - down
  
else:
  down = 0.1 * price
  total = price - down
print("Final price" + total)

