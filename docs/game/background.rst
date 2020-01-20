.. _background:

Background
==========

For the game, the background is space themed, just like the original arcade game(see home page link for example). To make the background show up for this game, we take the background image bank which is already created and take random images from the bank to paste it across the PyBadge screen. First, we set up our background image bank:

.. code-block:: python
  :linenos:
  
   # background image bank ready
    background_bank = stage.Bank.from_bmp16("background.bmp")
    
Then, we create a loop where we take a single image from the background bank and paste it on the screen. This loop occurs until the background fills up the whole PyBadge screen:

.. code-block:: python
  :linenos:
  
  background = stage.Grid(background_bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 15)
            background.tile(x_location, y_location, tile_picked)
            
The background now shows up on the screen!
