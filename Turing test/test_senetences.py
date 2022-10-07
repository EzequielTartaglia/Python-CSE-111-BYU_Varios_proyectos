import pytest
from sentences import get_determiner,get_noun,get_verb, get_preposition, get_prepositional_phrase,get_prepositional_phrase

def test_get_determiner():
           
# 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]
    
    #Capitalize every element inside the list, because in the main change the value
    for i in range(len(single_determiners)):
        single_determiners[i] = single_determiners[i].capitalize()
    
    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)
        
        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["Some", "Many", "The"]
    
    #Capitalize every element inside the list, because in the main change the value
    for i in range(len(plural_determiners)):
        plural_determiners[i] = plural_determiners[i].capitalize()

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    
           
# 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural noun.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_noun list.
        assert word in plural_nouns

def test_get_verb():
    
    """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ "" #Past """ """ """ """ """ """ """ """ """  """ """ """ """ """ """ """ """ """
    # 1. Test the single determiners.

    past_verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1,"past")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in past_verbs, "The verb isn't inside the list"

    # 2. Test the plural determiners.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2,"past")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in past_verbs, "The verb isn't inside the list"

    """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ "" #Present """ """ """ """ """ """ """ """ """  """ """ """ """ """ """ """ """ """

    # 1. Test the single determiners.

    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1,"present")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_present_verbs, "The verb isn't inside the list"

    # 2. Test the plural determiners.

    plural_present_verbs = [ "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2,"present")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_present_verbs, "The verb isn't inside the list"
        
    """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ "" #Future """ """ """ """ """ """ """ """ """  """ """ """ """ """ """ """ """ """

    # 1. Test the single determiners.

    future_verbs = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_verb(1,"future")

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in future_verbs, "The verb isn't inside the list"

    # 2. Test the plural determiners.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_verb(2,"future")

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in future_verbs, "The verb isn't inside the list"

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]


    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        preposition = get_preposition()

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert preposition in prepositions

def test_get_prepositional_phrase():#working
    
    preposition_phrase_single_past = get_prepositional_phrase(1,"past")
    preposition_phrase_plural_past = get_prepositional_phrase(2,"past")
    preposition_phrase_single_present = get_prepositional_phrase(1,"present")
    preposition_phrase_plural_present = get_prepositional_phrase(2,"present")
    preposition_phrase_single_future = get_prepositional_phrase(1,"future")
    preposition_phrase_plural_future = get_prepositional_phrase(2,"future")
    
    prepositions_phrase = [preposition_phrase_single_past,preposition_phrase_plural_past,preposition_phrase_single_present,preposition_phrase_plural_present,preposition_phrase_single_future,preposition_phrase_plural_future]

    
    assert preposition_phrase_single_past in prepositions_phrase
    assert preposition_phrase_plural_past in prepositions_phrase
    assert preposition_phrase_single_present in prepositions_phrase
    assert preposition_phrase_plural_present in prepositions_phrase
    assert preposition_phrase_single_future in prepositions_phrase
    assert preposition_phrase_plural_future in prepositions_phrase

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])