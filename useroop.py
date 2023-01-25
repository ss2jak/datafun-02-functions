""""
Jakiel 
1/24/2023
"""

import datetime
from enum import Enum

class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4

class PyBuddy:
    """ PyBuddy class for creating a study buddy."""

    def __init__(self, name, species,num_legs,weight_lbs,is_available, skill_list):
        """ Built-in method to create a new instance."""

        self.weight_lbs = weight_lbs
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.weight_lbs = weight_lbs
        self.is_available = is_available
        self.skill_list = skill_list
        self.create_date = datetime.datetime.now()

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.species} with {self.num_legs} legs.\n"
        s2 = f"I weigh {self.weight_lbs:.2f} lbs.\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"

        if self.is_available:
            s4 = "I'm available for tutoring.\n"
        else:
            s4 = "I'm already helping others learn Python.\n"

        s5 = "I know:\n"

        s6 = ""
        for skill in self.skill_list:
            s6 = s6 + f"  - {skill}\n"

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s        

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())

        final_message = """

        You'll need curiousity, the ability to search the web,
        and the tenacity and resourcefulness
        to solve all kinds of challenges.

        Let's get started!

        """
        print(final_message)

#---------------------------------------------------------------------------#

if __name__== "__main__":
    #Create an instance of a PyBuddy
    Jakiel = PyBuddy(
        name="Jakiel",
        species=Species.CAT,
        num_legs= 4,
        weight_lbs= 8.123456,
        is_available=True,
        skill_list=["Tableau","GitHub","Python","R", "VS Code"]
    )
    Jakiel.display_welcome()

    #CAll the buddy's welscome() method
    Diana = PyBuddy(
        name="Diana",
        species=Species.DOG,
        num_legs=4,
        weight_lbs=10.437241,
        is_available=True,
        skill_list=["Git", "R", "Python", "Markdown", "VS Code"],
    )

    Diana.display_welcome()

    Brooklyn =PyBuddy(
        name= "Brooklyn",
        species=Species.ELF,
        num_legs=4,
        weight_lbs=8,
        is_available=False,
        skill_list=["Git", "GitHub", "SQL", "Markdown", "Excel"],
        
    )

    Brooklyn.display_welcome()

    


