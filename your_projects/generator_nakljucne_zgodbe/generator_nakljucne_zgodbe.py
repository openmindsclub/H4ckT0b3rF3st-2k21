# Import the random module
import random
  
# Define a list of sentences to build the random story
intro = ['Okrog leta 1920', 'Kakšnih 1000 let nazaj', 'Pred skoraj 2000 leti', 'Bilo je nekoč, ko', 'Davno tega', 'Leta nazaj']
hero = [' je živel mož z imenom Pavle.', ' je živel veliki kralj.',' je živel neki kmet.',' je živel mož po imenu Kekec.', ' je živel neki pek.']
time = [' Neke noči', ' Nekega dne', ' Nekega večera', ' Na nek sončen dan', ' Ob neki polni luni']
plot = [' se je odločil, da gre na', ' je želel obiskati', ' se je sprehodil na',' je šel na piknik na']
place = [' goro', ' botanični vrt']
character = [' in videl moža,', ' in videl črnega psa,',]
age = [' ki je izgledal, kot da je star 20 let', ' ki je izgledal zelo star']
work = [' in je nekaj iskal.', ' in je kopal luknjo na sredi ceste.', ' in je pobiral rože ob poti.', ' ter je hodil zelo počasi.']
  
# Select an item from each list and concatenate them
print(random.choice(intro)+random.choice(hero)+
      random.choice(time)+random.choice(plot)+
      random.choice(place)+random.choice(character)+
      random.choice(age)+random.choice(work))