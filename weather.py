price = 1,000,000
credit = true
if credit:
  down = 0.1 * price
else:
  final = 0.2 * price
print(f"Down payment: ${down}")
