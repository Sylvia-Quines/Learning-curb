foodStuff = {"Yam", "Plantain", "Cocoyam", "Cassava"}
for x in foodStuff:
    print(x)

for x in "banana":
    print(x)
    
foodStuff = {"Yam", "Plantain", "Cocoyam", "Cassava"}
for x in foodStuff:
    print(x)
    if x == "Plantain":
        break
    
foodStuff = {"Yam", "Plantain", "Cocoyam", "Cassava"}
for x in foodStuff:
    if x == "Plantain":
        break
    print(x)
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)