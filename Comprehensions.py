#Task: For each comprehension type, create an example.
#Use Dictionary, Set, and List comprehensions —
#one with an if-else, one with an if condition, and one without any condition.



# Liefert alle Preise >= 102 (List-Comprehension mit if)

def getHighestPrices():
  stockPrices = [98.5, 102.3, 97.0, 105.6, 110.2, 99.9, 101.1]
  highestPrice = [price for price in stockPrices if price >= 102]
  return highestPrice



# Goldpreise (List-Comprehension mit if/else)

def getGoldStatus():
  goldPrices = [1890, 1912, 1925, 1888, 1950, 1899]
  goldStatus = ["low" if gold < 1900 else "okey" for gold in goldPrices]
  return goldStatus



# Rohstoffnamen  (Set-Comprehension mit if)
def getLongNames():
  commodities = ["gold", "oil", "silver", "gas", "silver", "copper", "oil"]
  longNames = {name for name in commodities if len(name) > 4}
  return longNames



# Erzeugt ein Dictionary mit Aktien und Preisen
# (Dictionary-Comprehension ohne Bedingung)

def getStockPrices():
  stocks = ["Apple", "Tesla", "Amazon"]
  prices = [176.4, 260.3, 134.9]
  stocksPrices = {stock: price for stock, price in zip(stocks, prices)}
  return stocksPrices


# Main

def main():
  print("\nAufgabe 1")
  print(getHighestPrices())

  print("\nAufgabe 2")
  print(getGoldStatus())

  print("\nAufgabe 3")
  print(getLongNames())

  print("\nAufgabe 4")
  print(getStockPrices())


# Einstiegspunkt
if __name__ == "__main__":
  main()
