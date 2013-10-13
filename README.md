GameTemplate
============

A basic object oriented game setup using pygame.

###Layout
This layout is loosely taken from the default Window's game template for XNA studio.  So far there are two classes: the program class and the game class.
####The Program Class
This class handles the game loop and basic initialization.  The includes the calling of the four major functions of the game class.
####The Game Class
This class has five parts, each of is called in the program class.
- Game Globals - Colors, constants, etc.
- Init - Initialization of game objects.  All init methods go here.
- Load - Content loaded here.
- Update - Game update methods here
- Draw - Draw methods go here.
