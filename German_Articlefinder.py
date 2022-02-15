FeminineEndings = ["ung", "heit", "keit", "schaft",
                   "ik", "ion", "e", "t", "ei", "in", "ur", "anz", "tät", "taet", "ade", "enz"]
NeuterEndings = ["um", "nis", "tum", "lein", "chen", "ment", "o"]
MasculineEndings = ["ling", "ich", "ig",
                    "or", "ist", "ismus", "er", "ent", "ast"]

Article = {"feminine": "Die", "masculine": "Der", "neuter": "Das"}


def retrievewordGender(word):
    for ending in FeminineEndings:
        if word.endswith(ending):
            return "feminine"
    for ending in NeuterEndings:
        if word.endswith(ending):
            return "neuter"
    for ending in MasculineEndings:
        if word.endswith(ending):
            return "masculine"
    else:
        return "Not Sure"


def getWord():
    wordInput = input().lower()
    if wordInput == "":
        print("Please enter a word:")
        return getWord()
    else:
        return wordInput


def printResult(word, result):
    if result == "Not Sure":
        print("Not able to tell the gender")
    else:
        print("The german noun {word} is {result}: {article} {word}".format(
            word=word, result=result, article=Article[result]))


def restartLoop():
    print("Would you like to try a nother word? y/n")
    again = input()
    if again == "n":
        loop = False


def main():

    loop = True
    while loop:

        try:
            print("Please enter a german noun:")

            word = getWord()

            result = retrievewordGender(word)

            word = word.capitalize()

            printResult(word, result)

            restartLoop()
        except KeyboardInterrupt:
            print("\nThanks for using my app!")
            loop = False


if __name__ == "__main__":
    main()
