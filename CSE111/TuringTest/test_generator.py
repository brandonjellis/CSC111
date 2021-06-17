from sentence_generator import get_determinate,get_noun,get_verb,get_preposition,get_prepositional_phrase
import pytest


def test_determinate():
    single_det = ["The","One","A"]
    plural_det = ["Some","Several","Many"]
    for _ in range(5):
        test = get_determinate(False)
        assert test in single_det

    for _ in range(5):
        test = get_determinate(True)
        assert test in plural_det

def test_nouns():
    single_nouns = ["cat","dog","man","woman","child","robot"]
    plural_nouns = ["cats","dogs","men","women","children","robots"]

    for _ in range(5):
        test = get_noun(False)
        assert test in single_nouns
    for _ in range(5):
        test = get_noun(True)
        assert test in plural_nouns

def test_verbs():
    past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    single_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    plural_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    p = False
    for _ in range(5):
        test_past = get_verb(p,1)
        test_present = get_verb(p,2)
        test_future = get_verb(p,3)

        assert test_past in past
        assert test_present in single_present
        assert test_future in future
    p = True
    for _ in range(5):
        test_past = get_verb(p,1)
        test_present = get_verb(p,2)
        test_future = get_verb(p,3)

        assert test_past in past
        assert test_present in plural_present
        assert test_future in future

def test_prepositions():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(5):
        test = get_preposition()
        assert test in prepositions

def test_p_phrase():
    single_det = ["the","one","a"]
    plural_det = ["some","several","many"]
    single_nouns = ["cat","dog","man","woman","child","robot"]
    plural_nouns = ["cats","dogs","men","women","children","robots"]
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    #test singular
    for _ in range(5):
        phrase = get_prepositional_phrase(False)
        phrase = phrase.split(" ")
        p = phrase[0]
        d = phrase[1]
        n = phrase[2]

        assert p in prepositions
        assert d in single_det
        assert n in single_nouns
    #test plural
    for _ in range(5):
        phrase = get_prepositional_phrase(True).split(" ")
        p = phrase[0]
        d = phrase[1]
        n = phrase[2]

        assert p in prepositions
        assert d in plural_det
        assert n in plural_nouns

test_p_phrase()
pytest.main(["-v","--tb=line","-rN","test_generator.py"])