.. _game_over_scene:

Game Over Scene
===============

The game moves to the game over scene when the player loses all three of their lives. The game over scene displays score that they received when they died, as well as an option to go back to the menu scene by pressing any button. When the player presses a button, the game returns to the main menu scene, where they can play again.

.. code-block:: python
  :linenos:
  
  def game_over_scene(final_score):
    # this function is the game over scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(30, 66)
    text1.text("Your Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 20)
    text2.text("GAME OVER!!!")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(27, 110)
    text3.text("PRESS ANY BUTTON!")
    text.append(text3)

    text4 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text4.move(27, 120)
    text4.text("TO MAIN MENU")
    text.append(text4)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = text + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            keys = 0
            main_menu_scene()
        elif keys & ugame.K_START != 0:
            keys = 1
            main_menu_scene()
        elif keys & ugame.K_X != 0:
            keys = 2
            main_menu_scene()
        elif keys & ugame.K_O != 0:
            keys = 3
            main_menu_scene()
        elif keys & ugame.K_UP != 0:
            keys = 4
            main_menu_scene()
        elif keys & ugame.K_DOWN != 0:
            keys = 5
            main_menu_scene()
        elif keys & ugame.K_LEFT != 0:
            keys = 6
            main_menu_scene()
        elif keys & ugame.K_RIGHT != 0:
            keys = 7
            main_menu_scene()
        # redraw sprite list
        pass # just a placeholder until you write the code

