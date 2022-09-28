import pandas as pd
from Personality import Personality


def setMatchValue(personality1:Personality, personality2:Personality):
    diff = 0
    for i in range(personality1.get_number_of_traits()):
        if(abs(personality1.trait_values[i] - personality2.trait_values[i]) > 0.50):
            diff+= 1
    if(diff > 2):
        return 0
    
    return 1

def check():
    persona1 = Personality()
    persona2 = Personality()

    first = {}
    second = {}

    first = persona1
    first.set_sequence_number(1)
    second = persona2
    second.set_sequence_number(2)

    if(persona1.get_first_value() <= persona2.get_first_value()):
        first = persona2
        first.set_sequence_number(1)
        second = persona1
        second.set_sequence_number(2)
    
    match_value = setMatchValue(first, second)

    return {**first.to_dict(), **second.to_dict(), "match": match_value }


def writeToFile():

    output = []
    
    for i in range(1000):
        output.append(check())

    df = pd.DataFrame(output)

    df.to_csv("out.csv")
    
writeToFile()