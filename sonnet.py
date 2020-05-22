#https://www.youtube.com/watch?v=MmhNk-zRJcU
#https://stackoverflow.com/questions/25714531/find-rhyme-using-nltk-in-python?answertab=votes#tab-top
import pronouncing
import random

def getSyllables(w):
    l = lambda x: 1 if x in "aeiouy" else 0
    return sum(list(map(l,w)))

def getRandomRhyme(w):
    l = pronouncing.rhymes(w.lower())
    print("worked", len(l))
    if len(l) == 0:
        return "No Rhyme today"
    return random.choice(l)

word = input("Give me a word to rhyme baby: ")
print(getRandomRhyme(word))
