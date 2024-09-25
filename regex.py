import re

text = "Î‘ÎœÎŸÎ¥ NOODLE LO MEIN 6104 9213513 42.83 128.49"

regex = r'^(.*?)\s+(.*?)\s+(\d{7})\s+([\d.]+)\s+([\d.]+)$'

match = re.match(regex, text, re.DOTALL)
brand = match.group(1)
print(brand)
print("\t")
description = match.group(2)
print(description)
print("\t")
category = ""
print(category)
print("\t")
productCode = match.group(3)
print(productCode)
print("\t")
price = match.group(5)
print(price)
print("\n")