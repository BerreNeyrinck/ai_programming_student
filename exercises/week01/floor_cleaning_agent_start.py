"""
Oefening 2: Floor Cleaning Agent (Model-based Reflex Agent)
=============================================================
Implementeer een model-based reflex agent voor een robotstofzuiger.
Volg het stappenplan in opgave_week1.md.
"""
import numpy as numpy
class FloorCleaningAgent:
    """
    Een model-based reflex agent die een kamer proper maakt.
    De kamer is een grid van `rows` × `cols` tegels.
    De robot start in de linkerbovenhoek (rij 0, kolom 0).
    """

    def __init__(self, rows=5, cols=10):
        """
        Initialiseer de robot met een lege kamer van `rows` × `cols`.

        Tip: gebruik een 2D-lijst om de status van elke tegel bij te houden.
        """

        self.rows = rows
        self.cols = cols
        self.cleanedTiles = []

        self.grid = numpy.random.choice([True, False], size=(rows, cols),).astype(object)
        self.grid[0][0] = "R"
        self.row = 0  # startrij (bovenaan)
        self.col = 0  # startkolom (links)

    # ---------- Basisbewegingen ----------

    def move_up(self):
        """Verplaats de robot één tegel omhoog (rij -1)."""
        if self.row > 0:
            self.row -= 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omhoog: rand bereikt")

    def move_down(self):
        """Verplaats de robot één tegel omlaag (rij +1)."""
        if self.row < self.rows-1:
            self.row += 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omlaag: rand bereikt")

    def move_left(self):
        """Verplaats de robot één tegel naar links (kolom -1)."""
        if self.col > 0:
            self.col -= 1
            print(f"Verplaats naar LINKS({self.row}, {self.col})")
        else:
            print("Kan niet naar links: rand bereikt")
        pass

    def move_right(self):
        """Verplaats de robot één tegel naar rechts (kolom +1)."""
        if self.col < self.cols -1:
            self.col += 1
            print(f"Verplaats naar RECHTS({self.row}, {self.col})")
        else:
            print("Kan niet naar rechts: rand bereikt")
        pass

    # ---------- Stofzuigen ----------

    def clean_tile(self):
        """Stofzuig de huidige tegel (maak hem proper)."""
        print("Position:", self.row, self.col)
        
        if self.grid[self.row][self.col] != True:
            self.grid[self.row][self.col] = True
            print(f"Tegel ({self.row}, {self.col}) is nu proper!")
        self.cleanedTiles.append((self.row, self.col))

    # ---------- Strategie ----------

    def clean_room(self):
        for r in range(self.rows):
            if r % 2 == 0:

                while self.col < self.cols - 1:
                    self.clean_tile()
                    self.move_right()

                self.clean_tile()

            else:

                while self.col > 0:
                    self.clean_tile()
                    self.move_left()

                self.clean_tile()

            if r < self.rows - 1:
                self.move_down()


    # ---------- Helper om naar een specifieke tegel te gaan ----------

    def move_to(self, target_row, target_col):
        """
        Verplaats de robot van huidige positie naar (target_row, target_col).
        Gebruik de basisbewegingen move_up/down/left/right.
        """


    # ---------- Weergave ----------

    def print_status(self):
        """Toon de huidige status van de kamer."""
        print("\nKamer status (false = vuil, true = proper, R = robot):")
        # for r in range(self.rows):
        #     rij_str = ""
        #     for c in range(self.cols):
        #         if r == self.row and c == self.col:
        #             rij_str += " R "
        #         else:
        #             # TODO: toon 'V' of 'P' op basis van interne grid
        #             rij_str += " ? "
        #     print(rij_str)

        self.grid[self.row][self.col] = "R"
        print(self.grid)
        print()


if __name__ == "__main__":
    # Test je agent
    robot = FloorCleaningAgent()
    # robot.clean_tile()

    print("Beginstatus:")
    robot.print_status()
    robot.clean_room()

    print("Eindstatus:")
    robot.print_status()