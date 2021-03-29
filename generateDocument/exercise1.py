def generateDocument(characters, document):
    character_list = []
    for i in characters:
        character_list.append(i)
    for doc in document:
        if doc in character_list:
            character_list.remove(doc)
        else:
            return False

    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


generateDocument(characters, document)
