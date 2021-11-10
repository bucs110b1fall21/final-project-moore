
# #constants - something never change
# CONSTANT = 1
# # some utility function
#
# #free function and variables go in a utility.py

# requirements
# - Player is represented on screen by an image
# - Player has 3 health
# - Player can move using arrow keys
# - Player can shoot with space bar
# - 3 enemies that display on screen
# - enemies move vertically
# - when player shoots enemy enemy pauses
# - When player collides with the enemy, they fight
#   - either player or enemy loses
#   - player loses, lose 1 health
#   - enemy loses enemy dies

# what models
# - player
# - enemy
# projectile
# What goes in the controller:
# How many screens?
# What should enemies start?
# where should player start?
# view
# what are we going to use for the use - pygame

# import your controller
from src import Controller
from src import ControllerWithSubloops


def main():
    game = ControllerWithSubloops.Controller()
    game.mainloop()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
