.. _game:

****
Game
****

The game scene starts out with the player/ship spawning in the middle of the screen. The player can move around using the d-pad and shoot lasers using the a button. Once the game starts, Asteroids will come down from the top of the screen, while two types of enemies come from the left side of the screen moving right. The aim of the game is to kill/avoid all enemies/asteroids before losing your three lives. On the main menu, there is an option to play on easy or hard mode (a for easy, b for hard(code shown in menu part of this documentation)). Destroying asteroids nets you five points on easy(fifteen points for hard), while enemies net you ten points on easy(thirty points for hard). The game gets progressively harder as you kill more enemies and asteroids. Once all three of your lives are gone, GAME OVER! 

Here is the code for the main game:

.. code-block:: python
  :linenos:
  
  def game_scene(diff_mul):
    # this function is the game scene
    # background image bank ready
    background_bank = stage.Bank.from_bmp16("background.bmp")
    image_bank_0 = stage.Bank.from_bmp16("meteor.bmp")
    image_bank_1 = stage.Bank.from_bmp16("ship-and-lasers.bmp")
    background = stage.Grid(background_bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 15)
            background.tile(x_location, y_location, tile_picked)
    a_button = constants.button_state["button_up"]
    shoot_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    sprites = []
    ship = stage.Sprite(image_bank_1, 0, 80, 64)
    sprites.insert(0, ship)  # insert at the top of sprite list

    score = 0
    scoretext = []
    score_text = stage.Text(width=29, height=14, font=None,
                            palette=constants.SCORE_PALETTE, buffer=None)
    score_text.cursor(0, 0)
    score_text.move(1, 118)
    score_text.text("Points: {0}".format(score))
    scoretext.append(score_text)

    lives = 3
    livestext = []
    lives_text = stage.Text(width=29, height=14, font=None,
                            palette=constants.LIVES_PALETTE, buffer=None)
    lives_text.cursor(0, 0)
    lives_text.move(1, 1)
    lives_text.text("Lives: {0}".format(lives))
    livestext.append(lives_text)

    asteroids = []
    for asteroids_number in range(constants.TOTAL_ASTEROIDS * diff_mul):
        single_asteroid = stage.Sprite(image_bank_0, 0, constants.OFF_TOP_SCREEN, constants.OFF_TOP_SCREEN)
        asteroids.append(single_asteroid)

    enemy_1 = []
    for enemy_number_1 in range(constants.TOTAL_ENEMY_1 * diff_mul):
        single_1 = stage.Sprite(image_bank_0, 1, constants.OFF_TOP_SCREEN, constants.OFF_TOP_SCREEN)
        enemy_1.append(single_1)

    enemy_2 = []
    for enemy_number_2 in range(constants.TOTAL_ENEMY_2 * diff_mul):
        single_2 = stage.Sprite(image_bank_0, 2, constants.OFF_TOP_SCREEN, constants.OFF_TOP_SCREEN)
        enemy_2.append(single_2)

    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        single_laser = stage.Sprite(image_bank_1, 8, constants.OFF_TOP_SCREEN, constants.OFF_TOP_SCREEN)
        lasers.append(single_laser)

    enemy_count = 1
    show_enemy(asteroids)
    show_enemy_2(enemy_1)
    show_enemy_3(enemy_2)
    death_mul = 1
    # set frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set layers, items show up in order
    game.layers = sprites + enemy_1 + enemy_2 + asteroids + lasers + scoretext + livestext + [background]
    # render background and sprite list
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number] .move(ship.x, ship.y)
                    sound.stop()
                    sound.play(shoot_sound)
                    break
        for laser_number in range(len(lasers)):
                if lasers[laser_number].x > 0:
                    if ship.rotation == 0:
                        lasers[laser_number].set_frame(rotation=0)
                        lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                        if lasers[laser_number].y < constants.OFF_SCREEN_Y:
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    elif ship.rotation == 1:
                        lasers[laser_number].set_frame(rotation=1)
                        lasers[laser_number].move(lasers[laser_number].x + constants.LASER_SPEED, lasers[laser_number].y)
                        if lasers[laser_number].x > 160:
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    elif ship.rotation == 2:
                        lasers[laser_number].set_frame(rotation=0)
                        lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y + constants.LASER_SPEED)
                        if lasers[laser_number].y > 128:
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    elif ship.rotation == 3:
                        lasers[laser_number].set_frame(rotation=1)
                        lasers[laser_number].move(lasers[laser_number].x - constants.LASER_SPEED, lasers[laser_number].y)
                        if lasers[laser_number].x < 5:
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        # Move ship right
        if keys & ugame.K_RIGHT:
            state_of_button = 2
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + constants.SHIP_MOVEMENT_SPEED * death_mul * diff_mul, ship.y)
                ship.set_frame(rotation=1)
            pass

        # Move ship left
        if keys & ugame.K_LEFT:
            state_of_button = 4
            if ship.x < 5:
                ship.move(5, ship.y)
            else:
                ship.move(ship.x - constants.SHIP_MOVEMENT_SPEED * death_mul * diff_mul, ship.y)
                ship.set_frame(rotation=3)
            pass

        # Move ship up
        if keys & ugame.K_UP:
            state_of_button = 1
            if ship.y < 0:
                ship.move(ship.x, 0)
            else:
                ship.move(ship.x, ship.y - constants.SHIP_MOVEMENT_SPEED * death_mul * diff_mul)
                ship.set_frame(rotation=0)
            pass

        # Move ship down
        if keys & ugame.K_DOWN:
            state_of_button = 3
            if ship.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE * death_mul * diff_mul)
            else:
                ship.move(ship.x, ship.y + constants.SHIP_MOVEMENT_SPEED * death_mul * diff_mul)
                ship.set_frame(rotation=2)
            pass

        # update game logic
        for asteroid_number in range(len(asteroids)):
            if asteroids[asteroid_number].x > 0:
                asteroids[asteroid_number].move(asteroids[asteroid_number].x, asteroids[asteroid_number].y + constants.ENEMY_SPEED  * diff_mul * death_mul)
                if asteroids[asteroid_number].y > constants.SCREEN_Y:
                    asteroids[asteroid_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_enemy(asteroids)
        for enemy_number_1 in range(len(enemy_1)):
            if enemy_1[enemy_number_1].y > 0:
                enemy_1[enemy_number_1].move(enemy_1[enemy_number_1].x + constants.ENEMY_SPEED * death_mul * diff_mul, enemy_1[enemy_number_1].y)
                if enemy_1[enemy_number_1].x > constants.SCREEN_X:
                    enemy_1[enemy_number_1].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_enemy_2(enemy_1)
        for enemy_number_2 in range(len(enemy_2)):
            if enemy_2[enemy_number_2].y > 0:
                enemy_2[enemy_number_2].move(enemy_2[enemy_number_2].x + constants.ENEMY_SPEED * death_mul * diff_mul, enemy_2[enemy_number_2].y)
                if enemy_2[enemy_number_2].x > constants.SCREEN_X:
                    enemy_2[enemy_number_2].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_enemy_3(enemy_2)
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for enemy_number_1 in range(len(enemy_1)):
                    if enemy_1[enemy_number_1].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                                         lasers[laser_number].x + 16, lasers[laser_number].y + 16,
                                         enemy_1[enemy_number_1].x, enemy_1[enemy_number_1].y,
                                         enemy_1[enemy_number_1].x + 16, enemy_1[enemy_number_1].y + 16):
                            enemy_1[enemy_number_1].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            score += 10*diff_mul
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1, 118)
                            score_text.text("Points: {0}".format(score))
                            sound.stop()
                            sound.play(boom_sound)
                            show_enemy_2(enemy_1)
                            show_enemy_2(enemy_1)
                            death_mul += (1/30)
                for enemy_number_2 in range(len(enemy_2)):
                    if enemy_2[enemy_number_2].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                                         lasers[laser_number].x + 16, lasers[laser_number].y + 16,
                                         enemy_2[enemy_number_2].x, enemy_2[enemy_number_2].y,
                                         enemy_2[enemy_number_2].x + 16, enemy_2[enemy_number_2].y + 16):
                            enemy_2[enemy_number_2].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            score += 10*diff_mul
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1, 118)
                            score_text.text("Points: {0}".format(score))
                            sound.stop()
                            sound.play(boom_sound)
                            show_enemy_3(enemy_2)
                            show_enemy_3(enemy_2)
                            death_mul += (1/30)
                for asteroid_number in range(len(asteroids)):
                    if asteroids[asteroid_number].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                                         lasers[laser_number].x + 16, lasers[laser_number].y + 16,
                                         asteroids[asteroid_number].x, asteroids[asteroid_number].y,
                                         asteroids[asteroid_number].x + 16, asteroids[asteroid_number].y + 16):
                            asteroids[asteroid_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            score += 5*diff_mul
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1, 118)
                            score_text.text("Points: {0}".format(score))
                            sound.stop()
                            sound.play(boom_sound)
                            show_enemy(asteroids)
                            show_enemy(asteroids)
                            death_mul += (1/30)
        for enemy_number_1 in range(len(enemy_1)):
            if enemy_1[enemy_number_1].x > 0:
                if stage.collide(enemy_1[enemy_number_1].x, enemy_1[enemy_number_1].y,
                                 enemy_1[enemy_number_1].x + 16, enemy_1[enemy_number_1].y + 16,
                                 ship.x, ship.y,
                                 ship.x + 16, ship.y + 16):
                    lives -= 1
                    ship.move(-100, -100)
                    sound.stop()
                    sound.play(boom_sound)
                    time.sleep(1)
                    if lives == 0:
                        game_over_scene(score)
                    else:
                        lives_text.clear()
                        lives_text.cursor(0,0)
                        lives_text.move(1, 1)
                        lives_text.text("Lives: {0}".format(lives))
                        ship.move (random.randint(16, 146), random.randint(16, 106))
        for enemy_number_2 in range(len(enemy_2)):
            if enemy_2[enemy_number_2].x > 0:
                if stage.collide(enemy_2[enemy_number_2].x, enemy_2[enemy_number_2].y,
                                 enemy_2[enemy_number_2].x + 16, enemy_2[enemy_number_2].y + 16,
                                 ship.x, ship.y,
                                 ship.x + 16, ship.y + 16):
                    lives -= 1
                    ship.move(-100, -100)
                    sound.stop()
                    sound.play(boom_sound)
                    time.sleep(1)
                    if lives == 0:
                        game_over_scene(score)
                    else:
                        lives_text.clear()
                        lives_text.cursor(0,0)
                        lives_text.move(1, 1)
                        lives_text.text("Lives: {0}".format(lives))
                        ship.move (random.randint(16, 146), random.randint(16, 106))
        for asteroid_number in range(len(asteroids)):
            if asteroids[asteroid_number].x > 0:
                if stage.collide(asteroids[asteroid_number].x, asteroids[asteroid_number].y,
                                 asteroids[asteroid_number].x + 16, asteroids[asteroid_number].y + 16,
                                 ship.x, ship.y,
                                 ship.x + 16, ship.y + 16):
                    lives -= 1
                    ship.move(-100, -100)
                    sound.stop()
                    sound.play(boom_sound)
                    time.sleep(1)
                    if lives == 0:
                        game_over_scene(score)
                    else:
                        lives_text.clear()
                        lives_text.cursor(0,0)
                        lives_text.move(1, 1)
                        lives_text.text("Lives: {0}".format(lives))
                        ship.move (random.randint(16, 146), random.randint(16, 106))
        # redraw sprite list
        game.render_sprites(sprites + asteroids + enemy_1 + enemy_2 + lasers)
        game.tick()

The full game code is here for full use for anybody wishing to make this game :)

.. toctree::
   :maxdepth: 1
   :glob:

   Background <background>
   Ship/Player <space_ship>
