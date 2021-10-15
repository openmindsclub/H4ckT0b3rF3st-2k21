
with open("p022_names.txt","r") as names:

  names = names.read().replace("\"","").split(",")


names.sort()

Sum = 0

length = len(names)

for position in range(length):
  
  alphavalue=0

  for j in names[position]:

    alphavalue += (ord(j)-64)

  Sum += (alphavalue * (position+1))

print(Sum)   