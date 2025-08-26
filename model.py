import requests
import tkinter as tk
import os


    


class PokemonModel:
    def __init__(self):
        self.number = 0

    def increment(self):
        """
        Increases the number by 1
        """
        self.number += 1
        
        

    def decrement(self):
        """
        Decreases number by 1 if number is not <= 0
        """
        self.number -= 1
        if self.number <= 0:
            self.number = 1000

    def get_value(self):
        """
        Returns the value of the number variable when called
        """

        return self.number
    
    def get_name(self):
        """
        1. Makes a request to the PokeApi pokemon information endpoint with the current number
        2. Parses the json data into 2 variables pname and picUrl
        3. Makes a request to picUrl and writes it on the disk
        4. Returns pname

        Args:
            None

        Returns:
            pname (str) : The name of the pokemon
        """
        name_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.number}")

        name_response1 = name_response.json()

        global pname
        pname = name_response1['forms'][0]['name']
        pname = pname.capitalize()
        picUrl = name_response1['sprites']['front_default']


        pokepic_response = requests.get(picUrl)

        with open(f"{pname}.png", "wb") as f:
            f.write(pokepic_response.content)

        return pname
    
    def get_image_path(self):
        """
        Stores the image path of the current pokemon being displayed by using it's name and extension (.png)

        Args:
            None

        Returns:
            image_path (str): The path to the pokemon image stored in the working directory
        """
        image_path = f"{pname}.png"
        return image_path
    
    def takeout_the_trash(self):
        """
        1. Finds all files in the working directory with the extension of .png 
        2. Creates a list of the files
        3. Deletes all files mentioned in the list

        Args:
            None

        Returns:
            None
        """
        found_files = []
        for file in os.listdir():
            if file.endswith('.png'):
                pathf = file
                found_files.append(pathf)
                print(f"file found: {pathf}")
        
        for file in found_files:
            os.remove(str(file))


        
