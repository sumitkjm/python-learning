from random import choice

class Coin:
    def __init__(self, rare = False, clean = True, **kwargs):

        for key, value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print ("Coin Spent!")

    def flip(self):
        heads_options = [True,False]
        choice_random = choice(heads_options)
        self.heads = choice_random



class PoundInherit(Coin):

    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_colour": "gold",
            "rusty_colour":"greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
        }
        super().__init__(**data)

class Pound:

    def __init__(self, rare = False):
        self.rare = rare
        if self.rare:
            self.diameter = 1.25
        self.value = 2.00

    value = 1.00
    colour = "gold"
    num_edges = 1
    diameter = 22.5  #mm
    thickness = 3.15  #mm
    heads = True

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"
    def flip(self):
        heads_options = [True,False]
        choice_random = choice(heads_options)
        self.heads = choice_random
    def __del__(self):
        print ("Coin Spent!")
coin1 = Pound(True)

coin2 = Pound()
coin2.rust()

coin_new = PoundInherit()

print (coin_new.colour)
#coin1.colour = "Yellow"
print (coin1.colour)
print (coin1.diameter)
print (coin2.colour)
coin2.clean()
print (coin2.colour)
print (coin2.heads)
coin2.flip()
print (coin2.heads)
