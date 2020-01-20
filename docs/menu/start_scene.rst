.. _start_scene:

Menu Scene
===========

The main menu scene includes the title of the game(Asteroids), the background(which is talked about in this documentation), and an option to play easy mode or hard mard by pressing a or b respectively. Here is the code for the main menu scene:

.. code-block:: python
  :linenos:
  
  def main_menu_scene():
    # this function is the menu scene
    # this code is only temporary so that I can work on game scene

    # an image bank for CircuitPython
    image_bank_0 = stage.Bank.from_bmp16("background.bmp")
    image_bank_1 = stage.Bank.from_bmp16("meteor.bmp")

    # difficulty multipliers that will be passed over to the game scene
    easy_mode = 1
    hard_mode = 3


    # sets the background
    background = stage.Grid(image_bank_0, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 15)
            background.tile(x_location, y_location, tile_picked)
    sprites = []
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(10, 20)
    text1.text("Asteroid Breaker")
    text.append(text1)
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(5, 100)
    text2.text("A = Easy  B = Hard")
    text.append(text2)

    title_meteor = stage.Sprite(image_bank_1, 0, 80, 64)
    sprites.append(title_meteor)


    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order

    game.layers = sprites + text + [background]
    # render the background and inital location of sprite list

    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        keys = ugame.buttons.get_pressed()
        # get user input
        if keys & ugame.K_X != 0:
            game_scene(easy_mode)
        if keys & ugame.K_O != 0:
            game_scene(hard_mode)


        # update game logic
        # redraw sprite list
        pass # just a placeholder until you write the code

The main menu scene leads into the main game.
