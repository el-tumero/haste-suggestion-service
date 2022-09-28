import numpy as np

traits = ["ambition", "confidence", "patience", "kindness", "creativity", "resposibility", "optimism", "courage", "modesty", "perseverance"]

class Personality:
    def __init__(self) -> None:
        self.trait_values = np.random.randint(0, 101, len(traits))
        self.trait_values = self.trait_values / 100

    def get_first_value(self) -> int:
        return self.trait_values[0]

    def get_number_of_traits(self):
        return len(self.trait_values)

    def set_sequence_number(self, number:int):
        self.sequence_number = number

    def to_dict(self):
        output = {}
        i = 0
        for trait in traits:
            output[trait + str(self.sequence_number)] = self.trait_values[i]
            i+=1
        return output


