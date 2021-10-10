# Import the random module
import random
  
# Define a liste of sentences to build the random story
  
first = [' In the 20 BC', ' About 1000 years ago', ' In the 10 BC', ' Once upon a time', ' On day', ' Many years ago']
char = [' there was a man named Paul.', ' there lived a king.',' there was a man named thomas.',' there lived a farmer.', ' There lived a baker']
time = [' One night', ' One day', ' One evening', ' In a sunny day', ' One full-moon night']
plot = [' he decided to go to', ' he wanted to visit', ' he was passing by',' he was going for a picnic to ']
place = [' the mountains', ' the garden']
secondary_char = [' he saw a man', ' he saw a young lady',]
age = [' who seemed to be in late 20s', ' who seemed very old']
work = [' searching for something.', ' digging a well on roadside.', ' picking flowers.', ' going phishing.']
  
# Select an item from each list and concatenating them
print(random.choice(first)+random.choice(char)+
      random.choice(time)+random.choice(plot) +
      random.choice(place)+random.choice(secondary_char)+
      random.choice(age)+random.choice(work))