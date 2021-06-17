import random



def get_determinate(plural):
    single_det = ["The","One","A"]
    plural_det = ["Some","Several","Many"]

    if not plural:
        return random.choice(single_det)
    elif plural:
        return random.choice(plural_det)
    else:
        return "ERROR"

def get_noun(plural):
    single_nouns = ["cat","dog","man","woman","child","robot"]
    plural_nouns = ["cats","dogs","men","women","children","robots"]

    if plural:
        word = random.choice(plural_nouns)
    else:
        word = random.choice(single_nouns)

    return word

def get_verb(plural,tense):
    """
    Returns a randomised word from internal list determined by the specified verb tense and plurality.
    Parameters:
    plural(BOOL) : pluraltiy of the sentence
    tense : verb tense 1 = past, 2 = present, 3 = future
    """
    past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    single_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    plural_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    if tense == 1:
        word = random.choice(past)
    elif tense == 2:
        if plural:
            word = random.choice(plural_present)
        else:
            word = random.choice(single_present)
    elif tense == 3:
        word = random.choice(future)
    else:
        return "ERROR"

    return word

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    return random.choice(prepositions)
    
def get_prepositional_phrase(plural):
    preposition = get_preposition()
    noun = get_noun(plural).lower()
    determiner = get_determinate(plural).lower()
    phrase = preposition + " " + determiner + " " + noun
    return phrase

def generate_sentence(tense,plural):
    determinant = get_determinate(plural)
    noun = get_noun(plural)
    verb = get_verb(plural, tense)
    sentence = determinant +" "+ noun +" "+ verb
    return sentence

def main():
    for i in range(3):
        i+=1
        print(generate_sentence(i,False)+".")
        print(generate_sentence(i,True)+".")
    for i in range(3):
        i+=1
        print(generate_sentence(i,False)+" "+get_prepositional_phrase(False)+".")
        print(generate_sentence(i,True)+" "+get_prepositional_phrase(True)+".")


main()