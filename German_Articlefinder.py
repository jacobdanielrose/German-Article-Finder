FeminineEndings = ["ung", "heit", "keit", "schaft", "ik", "ion"]
NeuterEndings = ["nis", "tum", "lein", "chen", "ment"]
MasculineEndings = ["ling", "ich", "ig"]

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

    wordInput = input()

    result = retrievewordGender(wordInput)

    print("The german noun {word} is {result}: {article} {word}".format(
        word=wordInput, result=result, article=Article[result]))


if __name__ == "__main__":
    main()
