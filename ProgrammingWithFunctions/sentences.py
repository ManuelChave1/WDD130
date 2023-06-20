import random

def generate_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    
    sentence = determiner + " " + noun + " " + verb + "."
    return sentence

def get_determiner():
    determiners = ["A", "An", "The", "One", "Some", "Many" ]
    return random.choice(determiners)

def get_noun():
    nouns = ["cat", "man", "woman", "girls", "dogs", "men"]
    return random.choice(nouns)

def get_verb():
    verbs = ["laughed", "eats", "will think", "thought", "run", "will write"]
    return random.choice(verbs)

if __name__ == "__main__":
    sentence = generate_sentence()
    print(sentence)
