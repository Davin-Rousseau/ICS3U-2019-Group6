#!/usr/bin/env python3

# Created by: Davin and DJ
# Created on: Dec 2019
# This file is the "Asteroids" game
#   for CircuitPython

import ugame
import stage
import time
import random

import constants
score = 0
def show_enemy(enemy):
    for enemy_number in range(len(enemy)):
        if enemy[enemy_number].y < 0:
            enemy[enemy_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
            break
def show_enemy_2(enemy):
    for enemy_number in range(len(enemy)):
        if enemy[enemy_number].x < 0:
            enemy[enemy_number].move(constants.OFF_TOP_SCREEN, random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE),)
            break
def show_enemy_3(enemy):
    for enemy_number in range(len(enemy)):
        if enemy[enemy_number].x < 0:
            enemy[enemy_number].move(constants.OFF_TOP_SCREEN, random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE),)
            break

def blank_white_reset_scene():
    # this function is the  blank splash scene game loop

    # do house keeping to ensure everythng is setup
    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list


def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # this function is the game scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(19, 50)
    text1.text("Rousseau & Watson")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 60)
    text2.text("Corporations")
    text.append(text2)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        time.sleep(1.0)
        main_menu_scene()


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


if __name__ == "__main__":
    blank_white_reset_scene()
