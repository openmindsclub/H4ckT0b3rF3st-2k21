import random
#variables
walls = "0             "
width = 12
length = 50
#top layer of the map
print("0" * length)
#walls and midle layer
for i in range(width - 2):
   print("0", ("".join(random.choice(walls) for i in range(length - 3))) + "0")
#buttom layer of the map
print("0" * length)
