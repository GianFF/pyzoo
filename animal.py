"""
Represents the animals on the ZooJS.
They receive a specie and an animalSound to be created.
"""

class Animal:
    def __init__(self, specie, animal_sound):
        self.specie = specie
        self.animal_sound = animal_sound

    """ 
    speak receives a phrase and returns it interspersed with the anial sound.
    @param {String} phrase the phrase to intersperse.
    @returns the interspersed phrase.
    """
    def speak(self, phrase):
        if phrase == "":
            return ""
        splitPhrase = phrase.split(' ') # i.e: ['Hello', 'world']
        mapPhrase = list(map(lambda word: f'{word} {self.animal_sound}', splitPhrase)) # i.e: ['Hello miau', 'world miau']
        finalPhrase = " ".join(mapPhrase) # i.e: 'Lions grrr' + ' ' + 'suck grrr'
        return finalPhrase
    

if __name__ == '__main__':
    animal = Animal()
