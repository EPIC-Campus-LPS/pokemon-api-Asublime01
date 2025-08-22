import requests


    


class PokemonModel:
    def __init__(self):
        self.number = 0

    def increment(self):
        self.number += 1
        
        

    def decrement(self):
        self.number -= 1

    def get_value(self):
        return self.number
    
    def get_name(self):
        name_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.number}")

        name_response1 = name_response.json()

        pname = name_response1['forms'][0]['name']
        pname = pname.capitalize()
        picUrl = name_response1['sprites']['front_default']


        pokepic_response = requests.get(picUrl)

        with open(f"{pname}.png", "wb") as f:
            f.write(pokepic_response.content)

        return pname
        
