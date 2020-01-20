.. _space_ship:

Ship/Player
==========

As stated in the main game page, the player controls a ship using the d-pad. When a player presses a direction, the ship rotates to the direction in which the player is pressing(ex. player presses left, ship rotates and moves left). The player shoots lasers by pressing a, and the lasers also go in the direction that the ship is facing in. The controls for the game are very simple, thus a simple and fun game! Here is the code to get the ship showing up in the game:

.. code-block:: python
  :linenos:
  
  sprites = []
    ship = stage.Sprite(image_bank_1, 0, 80, 64)
    sprites.insert(0, ship)  # insert at the top of sprite list

The code for moving the ship is in the main game page.
