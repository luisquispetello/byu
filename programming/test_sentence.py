from sentence import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner(determiner=None):
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]

    if determiner is None:
        # 1. Test the single determiners.
        for _ in range(4):
            determiner = get_determiner(1)
            assert determiner in single_determiners

        # 2. Test the plural determiners.
        for _ in range(4):
            determiner = get_determiner(2)
            assert determiner in plural_determiners
    else:
        for _ in range(4):
            assert determiner in single_determiners + plural_determiners



def test_get_noun(noun=None):
    single_nouns = ["bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"]
        
    if noun is None:
        # 1. Test the single noun.
        for _ in range(4):
            noun = get_noun(1)
            assert noun in single_nouns

        # 2. Test the plural noun.
        for _ in range(4):
            noun = get_noun(2)
            assert noun in plural_nouns
    else:
        for _ in range(4):
            assert noun in single_nouns + plural_nouns



def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"]
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"]
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"]
    
    # 1. Test the past verb.
    for _ in range(4):
        verb = get_verb(1, 'past')
        assert verb in past_verbs

    # 2. Test the single present verb.
    for _ in range(4):
        verb = get_verb(1, 'present')
        assert verb in single_present_verbs

    # 3. Test the plural present verb.
    for _ in range(4):
        verb = get_verb(2, 'present')
        assert verb in plural_present_verbs

    # 4. Test the future verb.
    for _ in range(4):
        verb = get_verb(1, 'future')
        assert verb in future_verbs



def test_get_preposition(preposition=None):
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    if preposition is None:
        for _ in range(4):
            preposition = get_preposition()
            assert preposition in prepositions
    else:
        for _ in range(4):
            assert preposition in prepositions



def test_get_prepositional_phrase():
    # 1. Test the singular prepositional phrase
    for _ in range(4):
        phrase = get_prepositional_phrase(1).split()

        preposition = phrase[0]
        determiner = phrase[1]
        noun = phrase[2]
        
        assert len(phrase) == 3

        test_get_preposition(preposition)
        test_get_determiner(determiner)
        test_get_noun(noun)

    # 2. Test the plural prepositional phrase
    for _ in range(4):
        phrase = get_prepositional_phrase(2).split()

        preposition = phrase[0]
        determiner = phrase[1]
        noun = phrase[2]

        assert len(phrase) == 3

        test_get_preposition(preposition)
        test_get_determiner(determiner)
        test_get_noun(noun)



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])