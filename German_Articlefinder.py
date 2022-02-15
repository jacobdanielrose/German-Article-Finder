FeminineEndings = ["ung", "heit", "keit", "schaft",
                   "ik", "ion", "e", "t", "ei", "in", "ur", "anz", "tät", "taet", "ade", "enz"]
NeuterEndings = ["um", "nis", "tum", "lein", "chen", "ment", "o"]
MasculineEndings = ["ling", "ich", "ig", "or", "ist", "ismus", "er"]

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


def main():
    print("Please enter a german noun:")

    wordInput = input().lower()

    result = retrievewordGender(wordInput)

    wordInput = wordInput.capitalize()

    print("The german noun {word} is {result}: {article} {word}".format(
        word=wordInput, result=result, article=Article[result]))


if __name__ == "__main__":
    main()
