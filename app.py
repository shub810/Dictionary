import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
allWords = data.keys()

# def getClosestRatio(word1, word2):
#     return SequenceMatcher(None, word2, word1).ratio()

# def similarWords(w):
#     words = difflib.get_close_matches(w, allWords)
#     print(words)
#     ratio = 0
#     closestWord = ""
#     for i in words:
#         r = getClosestRatio(i, w)
#         if r > ratio:
#             closestWord = i
#             r = ratio
#     return closestWord

def printWord(word):
    ans = ""
    means = data[word]
    for i in means:
        ans += i + " "
    return ans

def translate(word):
    word = word.lower()
    if word in data:
        return printWord(word)
    elif word.title() in data:
        return printWord(word.title())
    elif word.upper() in data:
        return printWord(word.upper())
    elif len(get_close_matches(word, allWords)) > 0:
        yn = input("Did you mean %s instead? If yes enter Y else N\n" % get_close_matches(word, allWords)[0])
        if yn == "Y":
            return printWord(get_close_matches(word, allWords)[0])
        elif yn == "N":
            return "This word does not exist. Please check that word again."
        else:
            return "We didn't understand your entry."
    else :
        return "This word does not exist. Please check that word again."

word = input("Enter the word : ")
print(translate(word))
