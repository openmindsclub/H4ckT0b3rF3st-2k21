import inflect
import re



def nbrLetters(x):

    inflector = inflect.engine()

    count = 0

    for i in range(1,x+1):

        S = inflector.number_to_words(i)

        S = re.sub("[^A-z]","",S)

        count += len(S)

    return count    


print(nbrLetters(1000))