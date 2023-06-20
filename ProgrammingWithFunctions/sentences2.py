import random

def generate_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()
    
    sentence = determiner + " " + noun + " " + verb + " " + prepositional_phrase + "."
    return sentence

def get_determiner():
    determiners = ["A", "An", "The", "One", "Some", "Many"]
    return random.choice(determiners)

def get_noun():
    nouns = ["girl", "bird", "child", "dogs", "children", "rabbits", "cats"]
    return random.choice(nouns)

def get_verb():
    verbs = ["talked", "drinks", "run", "drank", "laugh", "talk"]
    return random.choice(verbs)

def get_prepositional_phrase():
    prepositions = ["for", "off", "on", "above", "at", "about"]
    noun = get_noun()
    preposition = random.choice(prepositions)
    
    return preposition + " " + noun

if __name__ == "__main__":
    sentence = generate_sentence()
    print(sentence)
