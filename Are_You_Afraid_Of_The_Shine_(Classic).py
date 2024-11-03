# -*- coding: utf-8 -*-
"""

Created on Sat Aug 26 09:34:45 2023.

@author: AVITA
"""
import pygame
import sys
import random

pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Are You Afraid Of The Shine?")
pygame.display.set_icon(pygame.image.load("Assets\\Boss.png"))
fps = 60
clock = pygame.time.Clock()
font = "Assets\\Pixelbroidery-0n0G.ttf"
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pink = (255, 192, 203)
purple = (128, 0, 128)
light_purple = (174, 55, 255)
dark_purple = (60, 0, 100)
# Background
r = 0
g = 0
b = 0
increase = 0.5
# Music
pygame.mixer.set_num_channels(20)
title_track = pygame.mixer.Sound("Assets\\Title Track.mp3")
game_track = pygame.mixer.Sound("Assets\\Game Track.mp3")
click_sfx = pygame.mixer.Sound("Assets\\Click.mp3")
torch_blown_sfx = pygame.mixer.Sound("Assets\\Torch Blown.mp3")
knife_hit_sfx = pygame.mixer.Sound("Assets\\Knife Hit.mp3")
knives_out_sfx = pygame.mixer.Sound("Assets\\Knives Out.mp3")
player_damage_sfx = pygame.mixer.Sound("Assets\\Player Damage.mp3")
boss_appears_sfx = pygame.mixer.Sound("Assets\\Boss Appears.mp3")
boss_damage_sfx = pygame.mixer.Sound("Assets\\Boss Damage.mp3")
boss_died_sfx = pygame.mixer.Sound("Assets\\Boss Died.mp3")
# Player
player_sprite = pygame.image.load("Assets\\Ghost.png")
player_image = pygame.transform.scale(player_sprite, (50, 50))
player_x = width / 2
player_y = height / 2
player_rect = player_image.get_rect()
player_rect.center = (player_x, player_y)
player_speed = 2.5
knife = False
player_shield_sprite = pygame.image.load("Assets\\Ghost Shield.png")
player_shield_image = pygame.transform.scale(player_shield_sprite, (75, 75))
player_shield_rect = player_shield_image.get_rect()
player_shield_rect.center = (player_x, player_y)
# Player Health
player_health = 3
health_list = []
health_sprite = pygame.image.load("Assets\\Heart.png")
health_image = pygame.transform.scale(health_sprite, (30, 30))
health_rect1 = health_image.get_rect()
health_rect1.center = (5 + 15, 15 + 5)
health_rect2 = health_image.get_rect()
health_rect2.center = (5 + 15 + 10 + 15, 15 + 5)
health_rect3 = health_image.get_rect()
health_rect3.center = (5 + 15 + 10 + 15 + 10 + 15, 15 + 5)
health = 3
invincibility = False
invincibility_time = 120
count = 0
# Knife
knife_sprite = pygame.image.load("Assets\\Knife.png")
knife_image = pygame.transform.scale(knife_sprite, (30, 10))
kills = 0
angle = 45
knife_rect_list = []
kills_required = 3
# torch
torch_sprite = pygame.image.load("Assets\\Torch.png")
torch_image = pygame.transform.scale(torch_sprite, (30, 40))
torch_rect_list = []
total = 5
torches_broken = 0
torches_required = 10
for a in range(0, total):
    torch_rect = torch_image.get_rect()
    torch_rect.center = (random.randint(0, width), random.randint(0, height))
    torch_rect_list.append(torch_rect)
torch_change = False
# Enemy
enemy_sprite = pygame.image.load("Assets\\Knight.png")
enemy_image = pygame.transform.scale(enemy_sprite, (50, 75))
enemy_rect = enemy_image.get_rect()
enemy_x = 0
enemy_y = 0
enemy_rect.center = (enemy_x, enemy_y)
enemy_speed = 1.25
# Boss
boss = False
boss_sprite = pygame.image.load("Assets\\Boss.png")
boss_image = pygame.transform.scale(boss_sprite, (75, 100))
boss_rect = boss_image.get_rect()
boss_x = -100
boss_y = -100
boss_rect.center = (boss_x, boss_y)
boss_speed = 2.5
boss_max_health = 3
boss_health = 3
boss_immunity = False
boss_immunity_timer = 0
boss_immunity_time = 60
boss_shield_sprite = pygame.image.load("Assets\\Boss Shield.png")
boss_shield_image = pygame.transform.scale(boss_shield_sprite, (100, 125))
boss_shield_rect = boss_shield_image.get_rect()
boss_shield_rect.center = (boss_x, boss_y)
double_heal_chance = 0
boss_change = False
# Upgrades
yes = 0
upgrade = False
upgrades_list = [
    "Blood Loss",
    "Dark Speed",
    "Immunity Booster",
    "Torch Sorcery",
    "Knife Sorcery",
    "Torch Magic",
    "Dark Magic",
    "Lights Out",
]
upgrades_descrpiton_list = [
    ["Drains The Blood Of The Warriors", "Reduces Speed Of Warriors By 5%"],
    [
        "Gain Power From The Fear Inside The Warriors",
        "Boosts Your Speed By 5%",
    ],
    [
        "Eat The Flesh Of The Warriors",
        "Boosts Invincibility Time By 0.5 Seconds",
    ],
    [
        "Absorb More Light From The Torches",
        "Reduces The Amount Light Required By 1",
    ],
    [
        "Drain More Power From The Warriors",
        "Reduces The Amount Of Kills Required By 1",
    ],
    [
        "Generate More Fear In The People",
        "Boosts The Amount Of Torches That Appear By 1",
    ],
    [
        "Eat The Flesh of The Darkness",
        "Boosts Chance To Heal 2 Hearts After Killing The Boss By 1%",
    ],
    [
        "Decays The Light Radiating From Torches",
        "Reduces The Speed Of Increasing Light BY 0.1%",
    ],
]
upgrades_desc_font = pygame.font.Font(font, 15)
upgrade_title_font = pygame.font.Font(font, 50)
upgrade_title_text = upgrade_title_font.render("Choose An Upgrade", True, pink)
upgrade_title_rect = upgrade_title_text.get_rect()
upgrade_title_rect.center = (width / 2, 100)
upgrade_font = pygame.font.Font(font, 25)
change = False
# Upgrade Icons
blood_loss_icon = pygame.image.load("Assets\\Blood Loss.png")
dark_speed_icon = pygame.image.load("Assets\\Dark Speed.png")
immunity_booster_icon = pygame.image.load("Assets\\Immunity Booster.png")
torch_sprcery_icon = pygame.image.load("Assets\\Torch Sorcery.png")
knife_sorcery_icon = pygame.image.load("Assets\\Knife Sorcery.png")
torch_magic_icon = pygame.image.load("Assets\\Torch Magic.png")
dark_magic_icon = pygame.image.load("Assets\\Dark Magic.png")
lights_out_icon = pygame.image.load("Assets\\Lights Out.png")
upgrades_icon_list = [
    blood_loss_icon,
    dark_speed_icon,
    immunity_booster_icon,
    torch_sprcery_icon,
    knife_sorcery_icon,
    torch_magic_icon,
    dark_magic_icon,
    lights_out_icon,
]
for icon in range(0, len(upgrades_icon_list)):
    upgrades_icon_list[icon] = pygame.transform.scale(
        upgrades_icon_list[icon], (125, 125)
    )
# Score
score = 0
bosses_killed = 0
score_font = pygame.font.Font(font, 50)
score_game_font = pygame.font.Font(font, 20)
score_plus_font = pygame.font.Font(font, 10)
torch_score = score_plus_font.render("+20", True, white)
kill_score = score_plus_font.render("+50", True, white)
boss_score = score_plus_font.render("+100", True, white)
torch_score_rect = torch_score.get_rect()
kill_score_rect = kill_score.get_rect()
boss_score_rect = boss_score.get_rect()
torch_score_appear = False
kill_score_appear = False
boss_score_appear = False
torch_score_count = 0
kill_score_count = 0
boss_score_count = 0
scores = open("Assets\\Scores.txt", "a+")
scores.write("0")
scores.write("\n")
scores.close()
scoreslist = []
# Title Screen
title_sprite = pygame.image.load("Assets\\Title.png")
title_image = pygame.transform.scale(title_sprite, (800, 800))
title_rect = title_image.get_rect()
title_rect.center = (width / 2, 125)
play_button_sprite = pygame.image.load("Assets\\Start.png")
play_button_image = pygame.transform.scale(play_button_sprite, (400, 100))
play_button_rect = play_button_image.get_rect()
play_button_rect.center = (width / 2, 300)
exit_button_sprite = pygame.image.load("Assets\\Quit.png")
exit_button_image = pygame.transform.scale(exit_button_sprite, (400, 100))
exit_button_rect = exit_button_image.get_rect()
exit_button_rect.center = (width / 2, 425)
# Game Control
hard_timer = 0
pause = False
gamestart = False
gameover = False
gameover_sprite = pygame.image.load("Assets\\Gameover.png")
gameover_image = pygame.transform.scale(gameover_sprite, (750, 250))
gameover_rect = gameover_image.get_rect()
gameover_rect.center = (width / 2, 150)
retry_button_sprite = pygame.image.load("Assets\\Retry.png")
retry_button_image = pygame.transform.scale(retry_button_sprite, (350, 100))
menu_button_sprite = pygame.image.load("Assets\\Menu.png")
menu_button_image = pygame.transform.scale(menu_button_sprite, (350, 100))
# Pause Event
restart_button_sprite = pygame.image.load("Assets\\Restart.png")
restart_button_image = pygame.transform.scale(
    restart_button_sprite, (350, 100)
)
resume_button_sprite = pygame.image.load("Assets\\Resume.png")
resume_button_image = pygame.transform.scale(resume_button_sprite, (350, 100))
main_menu_button_sprite = pygame.image.load("Assets\\Main Menu.png")
main_menu_button_image = pygame.transform.scale(
    main_menu_button_sprite, (350, 100)
)
# Timer
timer_font = pygame.font.Font(font, 25)
time = "00:00:00"
frames = 0
seconds = 0
minutes = 0
hours = 0
while True:
    # Window Control
    if gamestart:
        title_track.stop()
        game_track.play(99999)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Channel(4).play(click_sfx)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.Channel(4).play(click_sfx)
                    pause = True
        window.fill((r, g, b))
        if boss and not boss_immunity:
            if boss_x <= player_x and not knife:
                window.blit(boss_image, boss_rect)
            if boss_x > player_x and not knife:
                window.blit(
                    pygame.transform.flip(boss_image, True, False), boss_rect
                )
            if boss_x > player_x and knife:
                window.blit(boss_image, boss_rect)
            if boss_x < player_x and knife:
                window.blit(
                    pygame.transform.flip(boss_image, True, False), boss_rect
                )
        # Repulsion
        if boss and boss_immunity:
            if boss_x > player_x and not boss_x >= width:
                boss_x += 1.6
            if boss_x < player_x and not boss_x <= 0:
                boss_x -= 1.6
            if boss_y > player_y and not boss_y >= height:
                boss_y += 1.6
            if boss_y < player_y and not boss_y <= 0:
                boss_y -= 1.6
            if boss_x <= player_x:
                window.blit(boss_image, boss_rect)
            if boss_x > player_x:
                window.blit(
                    pygame.transform.flip(boss_image, True, False), boss_rect
                )
        for rect in torch_rect_list:
            window.blit(torch_image, rect)
        window.blit(player_image, player_rect)
        if enemy_x <= player_x and not knife:
            window.blit(enemy_image, enemy_rect)
        if enemy_x > player_x and not knife:
            window.blit(
                pygame.transform.flip(enemy_image, True, False), enemy_rect
            )
        if enemy_x > player_x and knife:
            window.blit(enemy_image, enemy_rect)
        if enemy_x < player_x and knife:
            window.blit(
                pygame.transform.flip(enemy_image, True, False), enemy_rect
            )
        if knife:
            knife_rot_image1 = pygame.transform.rotate(knife_image, 0 * angle)
            knife_rect1 = knife_rot_image1.get_rect()
            knife_rect1.center = (player_rect.left, player_y)
            knife_rect_list.append(knife_rect1)
            window.blit(knife_rot_image1, knife_rect1)

            knife_rot_image2 = pygame.transform.rotate(knife_image, 5 * angle)
            knife_rect2 = knife_rot_image2.get_rect()
            knife_rect2.center = player_rect.topright
            knife_rect_list.append(knife_rect2)
            window.blit(knife_rot_image2, knife_rect2)

            knife_rot_image3 = pygame.transform.rotate(knife_image, 6 * angle)
            knife_rect3 = knife_rot_image3.get_rect()
            knife_rect3.center = (player_x, player_rect.top)
            knife_rect_list.append(knife_rect3)
            window.blit(knife_rot_image3, knife_rect3)

            knife_rot_image4 = pygame.transform.rotate(knife_image, 7 * angle)
            knife_rect4 = knife_rot_image4.get_rect()
            knife_rect4.center = player_rect.topleft
            knife_rect_list.append(knife_rect4)
            window.blit(knife_rot_image4, knife_rect4)

            knife_rot_image5 = pygame.transform.rotate(knife_image, 4 * angle)
            knife_rect5 = knife_rot_image5.get_rect()
            knife_rect5.center = (player_rect.right, player_y)
            knife_rect_list.append(knife_rect5)
            window.blit(knife_rot_image5, knife_rect5)

            knife_rot_image6 = pygame.transform.rotate(knife_image, 3 * angle)
            knife_rect6 = knife_rot_image6.get_rect()
            knife_rect6.center = player_rect.bottomright
            knife_rect_list.append(knife_rect6)
            window.blit(knife_rot_image6, knife_rect6)

            knife_rot_image7 = pygame.transform.rotate(knife_image, 2 * angle)
            knife_rect7 = knife_rot_image7.get_rect()
            knife_rect7.center = (player_x, player_rect.bottom)
            knife_rect_list.append(knife_rect7)
            window.blit(knife_rot_image7, knife_rect7)

            knife_rot_image8 = pygame.transform.rotate(knife_image, 1 * angle)
            knife_rect8 = knife_rot_image8.get_rect()
            knife_rect8.center = player_rect.bottomleft
            knife_rect_list.append(knife_rect8)
            window.blit(knife_rot_image8, knife_rect8)
        if health > 0:
            window.blit(health_image, health_rect1)
            if health > 1:
                window.blit(health_image, health_rect2)
                if health > 2:
                    window.blit(health_image, health_rect3)
        score_game_text = score_game_font.render(
            "Score:" + str(score), True, white
        )
        score_game_rect = score_game_text.get_rect()
        score_game_rect.center = (width / 2, 20)
        window.blit(score_game_text, score_game_rect)
        # Timer Stuff
        if seconds <= 9 and minutes <= 9 and hours <= 9:
            time = "0" + str(hours) + ":0" + str(minutes) + ":0" + str(seconds)
        elif seconds > 9 and minutes <= 9 and hours <= 9:
            time = "0" + str(hours) + ":0" + str(minutes) + ":" + str(seconds)
        elif seconds <= 9 and minutes > 9 and hours <= 9:
            time = "0" + str(hours) + ":" + str(minutes) + ":0" + str(seconds)
        elif seconds <= 9 and minutes <= 9 and hours > 9:
            time = str(hours) + ":0" + str(minutes) + ":0" + str(seconds)
        elif seconds > 9 and minutes > 9 and hours <= 9:
            time = "0" + str(hours) + ":" + str(minutes) + ":" + str(seconds)
        elif seconds > 9 and minutes <= 9 and hours > 9:
            time = str(hours) + ":0" + str(minutes) + ":" + str(seconds)
        elif seconds <= 9 and minutes > 9 and hours > 9:
            time = str(hours) + ":" + str(minutes) + ":0" + str(seconds)
        elif seconds > 9 and minutes > 9 and hours > 9:
            time = str(hours) + ":" + str(minutes) + ":" + str(seconds)
        timer_text = timer_font.render(time, True, white)
        timer_rect = timer_text.get_rect()
        timer_rect.center = (945, 22.5)
        window.blit(timer_text, timer_rect)
        if pause:
            game_track.stop()
            resume_button_rect = resume_button_image.get_rect()
            resume_button_rect.center = (width / 2, 100)
            restart_button_rect = restart_button_image.get_rect()
            restart_button_rect.center = (width / 2, 250)
            main_menu_button_rect = main_menu_button_image.get_rect()
            main_menu_button_rect.center = (width / 2, 400)
            window.blit(resume_button_image, resume_button_rect)
            window.blit(restart_button_image, restart_button_rect)
            window.blit(main_menu_button_image, main_menu_button_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button_rect.collidepoint(event.pos):
                        click_sfx.play()
                        pause = False
                    if restart_button_rect.collidepoint(event.pos):
                        time = "00:00:00"
                        frames = 0
                        seconds = 0
                        minutes = 0
                        hours = 0
                        click_sfx.play()
                        r = 0
                        g = 0
                        b = 0
                        increase = 0.5
                        player_x = width / 2
                        player_y = height / 2
                        player_rect = player_image.get_rect()
                        player_rect.center = (player_x, player_y)
                        player_speed = 2.5
                        knife = False
                        health_rect1 = health_image.get_rect()
                        health_rect1.center = (5 + 15, 15 + 5)
                        health_rect2 = health_image.get_rect()
                        health_rect2.center = (5 + 15 + 10 + 15, 15 + 5)
                        health_rect3 = health_image.get_rect()
                        health_rect3.center = (
                            5 + 15 + 10 + 15 + 10 + 15,
                            15 + 5,
                        )
                        health = 3
                        boss_x = -100
                        boss_y = -100
                        boss_rect.center = (boss_x, boss_y)
                        boss = False
                        double_heal_chance = 0
                        invincibility = False
                        invincibility_time = 120
                        count = 0
                        kills = 0
                        torch_rect_list = []
                        total = 5
                        torches_broken = 0
                        torches_required = 10
                        for a in range(0, total):
                            torch_rect = torch_image.get_rect()
                            torch_rect.center = (
                                random.randint(0, width - 10),
                                random.randint(0, height - 10),
                            )
                            torch_rect_list.append(torch_rect)
                        torch_change = False
                        enemy_x = 0
                        enemy_y = 0
                        enemy_rect.center = (enemy_x, enemy_y)
                        enemy_speed = 1.25
                        yes = 0
                        upgrade = False
                        change = False
                        score = 0
                        gamestart = True
                        gameover = False
                        pause = False
                        break
                    if main_menu_button_rect.collidepoint(event.pos):
                        time = "00:00:00"
                        frames = 0
                        seconds = 0
                        minutes = 0
                        hours = 0
                        click_sfx.play()
                        r = 0
                        g = 0
                        b = 0
                        increase = 0.5
                        player_x = width / 2
                        player_y = height / 2
                        player_rect = player_image.get_rect()
                        player_rect.center = (player_x, player_y)
                        player_speed = 2.5
                        knife = False
                        health_rect1 = health_image.get_rect()
                        health_rect1.center = (5 + 15, 15 + 5)
                        health_rect2 = health_image.get_rect()
                        health_rect2.center = (5 + 15 + 10 + 15, 15 + 5)
                        health_rect3 = health_image.get_rect()
                        health_rect3.center = (
                            5 + 15 + 10 + 15 + 10 + 15,
                            15 + 5,
                        )
                        health = 3
                        boss_x = -100
                        boss_y = -100
                        boss_rect.center = (boss_x, boss_y)
                        boss = False
                        double_heal_chance = 0
                        invincibility = False
                        invincibility_time = 120
                        count = 0
                        kills = 0
                        torch_rect_list = []
                        total = 5
                        torches_broken = 0
                        torches_required = 10
                        for a in range(0, total):
                            torch_rect = torch_image.get_rect()
                            torch_rect.center = (
                                random.randint(0, width - 10),
                                random.randint(0, height - 10),
                            )
                            torch_rect_list.append(torch_rect)
                        torch_change = False
                        enemy_x = 0
                        enemy_y = 0
                        enemy_rect.center = (enemy_x, enemy_y)
                        enemy_speed = 1.25
                        yes = 0
                        upgrade = False
                        change = False
                        score = 0
                        gamestart = False
                        gameover = False
                        pause = False
                        break
    if not gamestart:
        title_track.play(99999)
        window.fill(black)
        window.blit(title_image, title_rect)
        window.blit(play_button_image, play_button_rect)
        window.blit(exit_button_image, exit_button_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    click_sfx.play()
                    gamestart = True
                elif exit_button_rect.collidepoint(event.pos):
                    click_sfx.play()
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Player Movement
    if not gameover:
        if not upgrade:
            if gamestart:
                if not pause:
                    yes = 0
                    key = pygame.key.get_pressed()
                    if key[pygame.K_RIGHT] and not (player_x >= width):
                        player_x += player_speed
                    if key[pygame.K_LEFT] and not (player_x <= 0):
                        player_x -= player_speed
                    if key[pygame.K_UP] and not (player_y <= 0):
                        player_y -= player_speed
                    if key[pygame.K_DOWN] and not (player_y >= height):
                        player_y += player_speed
                    player_rect.center = (player_x, player_y)
                    # Enemy Movement
                    if not knife:
                        if enemy_x < player_x:
                            enemy_x += enemy_speed
                        if enemy_x > player_x:
                            enemy_x -= enemy_speed
                        if enemy_y < player_y:
                            enemy_y += enemy_speed
                        if enemy_y > player_y:
                            enemy_y -= enemy_speed
                        enemy_rect.center = (enemy_x, enemy_y)
                    if knife:
                        if enemy_x < player_x and not (enemy_x <= 0):
                            enemy_x -= enemy_speed
                        if enemy_x > player_x and not (enemy_x >= width):
                            enemy_x += enemy_speed
                        if enemy_y < player_y and not (enemy_y <= 0):
                            enemy_y -= enemy_speed
                        if enemy_y > player_y and not (enemy_y >= height):
                            enemy_y += enemy_speed
                        enemy_rect.center = (enemy_x, enemy_y)
                    if boss:
                        # Boss Movement
                        if not knife:
                            if boss_x < player_x:
                                boss_x += boss_speed
                            if boss_x > player_x:
                                boss_x -= boss_speed
                            if boss_y < player_y:
                                boss_y += boss_speed
                            if boss_y > player_y:
                                boss_y -= boss_speed
                            boss_rect.center = (boss_x, boss_y)
                        if knife:
                            if boss_x < player_x and not (boss_x <= 0):
                                boss_x -= boss_speed
                            if boss_x > player_x and not (boss_x >= width):
                                boss_x += boss_speed
                            if boss_y < player_y and not (boss_y <= 0):
                                boss_y -= boss_speed
                            if boss_y > player_y and not (boss_y >= height):
                                boss_y += boss_speed
                            boss_rect.center = (boss_x, boss_y)
                    if not knife:
                        # Player To torch Collision
                        for rect in torch_rect_list:
                            if pygame.Rect.colliderect(player_rect, rect):
                                pygame.mixer.Channel(1).play(torch_blown_sfx)
                                torches_broken += 1
                                r = 0
                                g = 0
                                b = 0
                                torch_score_rect.center = (
                                    rect.centerx,
                                    rect.centery,
                                )
                                torch_rect_list.remove(rect)
                                torch_rect = torch_image.get_rect()
                                torch_rect.center = (
                                    random.randint(0, width - 10),
                                    random.randint(0, height - 10),
                                )
                                torch_rect_list.append(torch_rect)
                                torch_score_appear = True
                                score += 20
                                break
                    if torch_score_appear:
                        window.blit(torch_score, torch_score_rect)
                        torch_score_count += 1
                    if torch_score_count == 60:
                        torch_score_appear = False
                        torch_score_count = 0
                    # Knife To Enemy Collision
                    if knife:
                        for knife_rect in knife_rect_list:
                            if enemy_rect.colliderect(knife_rect):
                                kill_score_rect.center = (
                                    enemy_rect.centerx,
                                    enemy_rect.centery,
                                )
                                kill_score_appear = True
                                pygame.mixer.Channel(2).play(knife_hit_sfx)
                                kills += 1
                                enemy_x = random.choice([0, width])
                                enemy_y = random.choice([0, height])
                                enemy_rect.center = (enemy_x, enemy_y)
                                knife = False
                                torch_change = True
                                knife_rect_list = []
                                score += 50
                                break
                        if boss:
                            for knife_rect in knife_rect_list:
                                if (
                                    pygame.Rect.colliderect(
                                        boss_rect, knife_rect
                                    ) and not boss_immunity
                                ):
                                    pygame.mixer.Channel(2).play(knife_hit_sfx)
                                    if boss_health > 1:
                                        pygame.mixer.Channel(6).play(
                                            boss_damage_sfx
                                        )
                                    boss_health -= 1
                                    boss_immunity = True
                                    knife = False
                                    torch_change = True
                                    knife_rect_list = []
                                    break
                    if kill_score_appear:
                        kill_score_count += 1
                        window.blit(kill_score, kill_score_rect)
                    if kill_score_count == 60:
                        kill_score_count = 0
                        kill_score_appear = False
                    # Background Color
                    r += increase
                    g += increase
                    b += increase
                    if r > 255 and g > 255 and b > 255:
                        health = 0
                    if (
                        not invincibility and not knife and (
                            (
                                pygame.Rect.colliderect(
                                    player_rect, enemy_rect
                                ) or (
                                    (
                                        pygame.Rect.colliderect(
                                            player_rect, boss_rect
                                        ) and not boss_immunity
                                    )
                                )
                            )
                        )
                    ):
                        pygame.mixer.Channel(3).play(player_damage_sfx)
                        health -= 1
                        invincibility = True
                    frames += 1
                    if frames == fps:
                        frames = 0
                        seconds += 1
                    if seconds == 60:
                        seconds = 0
                        minutes += 1
                    if minutes == 60:
                        minutes = 0
                        hours += 1
                    hard_timer += 1
                    if hard_timer % 7200 == 0 and hard_timer != 0:
                        torches_required += 1
                        kills_required += 1
                        enemy_speed += (5 / 100) * enemy_speed
                        player_speed -= (5 / 100) * player_speed
                        if len(torch_rect_list) > 1:
                            torch_rect_list.pop()
                        increase += (0.1 / 100) * increase
                        hard_timer = 0
            # Game Stats Conditions
            if (
                torches_broken % torches_required == 0 and torches_broken != 0 and not torch_change
            ):
                if not knife:
                    pygame.mixer.Channel(8).play(knives_out_sfx)
                knife = True
            if (torches_broken - 1) % torches_required == 0:
                torch_change = False
            if kills % kills_required == 0 and kills != 0 and not change:
                upgrade = True
            if (kills - 1) % kills_required == 0:
                change = False
            if kills % 10 == 0 and kills != 0 and not boss and not boss_change:
                boss = True
                pygame.mixer.Channel(5).play(boss_appears_sfx)
            if (kills - 1) % 10 == 0:
                boss_change = False
        # Upgrade Control
        if upgrade:
            game_track.stop()
            if yes % 2 == 0:
                upgrade1 = random.randint(0, len(upgrades_list) - 1)
                upgrade2 = random.randint(0, len(upgrades_list) - 1)
                while upgrade2 == upgrade1:
                    upgrade2 = random.randint(0, len(upgrades_list) - 1)
                yes += 1
            pygame.draw.rect(
                window, light_purple, pygame.Rect(50, 50, 900, 400)
            )
            window.blit(upgrade_title_text, upgrade_title_rect)
            button_color1 = purple
            button_color2 = purple
            pygame.draw.rect(
                window, button_color1, pygame.Rect(75, 150, 412.5, 275)
            )
            pygame.draw.rect(
                window, button_color2, pygame.Rect(512.5, 150, 412.5, 275)
            )
            mousex, mousey = pygame.mouse.get_pos()
            if (pygame.Rect(75, 150, 412.5, 275)).collidepoint(mousex, mousey):
                button_color1 = dark_purple
            if (pygame.Rect(512.5, 150, 412.5, 275)).collidepoint(
                mousex, mousey
            ):
                button_color2 = dark_purple
            pygame.draw.rect(
                window, button_color1, pygame.Rect(75, 150, 412.5, 275)
            )
            pygame.draw.rect(
                window, button_color2, pygame.Rect(512.5, 150, 412.5, 275)
            )
            upgrade_text1 = upgrade_font.render(
                upgrades_list[upgrade1], True, pink
            )
            upgrade_text2 = upgrade_font.render(
                upgrades_list[upgrade2], True, pink
            )
            upgrade_rect1 = upgrade_text1.get_rect()
            upgrade_rect2 = upgrade_text2.get_rect()
            upgrade_rect1.center = (75 + (412.5 / 2), 172.5)
            upgrade_rect2.center = ((412.5 / 2) + 100 + 412.5, 172.5)
            window.blit(upgrade_text1, upgrade_rect1)
            window.blit(upgrade_text2, upgrade_rect2)
            upgrade_desc_text1 = upgrades_desc_font.render(
                upgrades_descrpiton_list[upgrade1][0], True, pink
            )
            upgrade_desc_text2 = upgrades_desc_font.render(
                upgrades_descrpiton_list[upgrade2][0], True, pink
            )
            upgrade_desc_rect1 = upgrade_desc_text1.get_rect()
            upgrade_desc_rect2 = upgrade_desc_text2.get_rect()
            upgrade_desc_rect1.center = (75 + (412.5 / 2), 215)
            upgrade_desc_rect2.center = ((412.5 / 2) + 100 + 412.5, 215)
            upgrade_desc1 = upgrades_desc_font.render(
                upgrades_descrpiton_list[upgrade1][1], True, pink
            )
            upgrade_desc2 = upgrades_desc_font.render(
                upgrades_descrpiton_list[upgrade2][1], True, pink
            )
            upgrade_desc1_rect = upgrade_desc1.get_rect()
            upgrade_desc2_rect = upgrade_desc2.get_rect()
            upgrade_desc1_rect.center = (75 + (412.5 / 2), 230)
            upgrade_desc2_rect.center = ((412.5 / 2) + 100 + 412.5, 230)
            window.blit(upgrade_desc_text1, upgrade_desc_rect1)
            window.blit(upgrade_desc_text2, upgrade_desc_rect2)
            window.blit(upgrade_desc1, upgrade_desc1_rect)
            window.blit(upgrade_desc2, upgrade_desc2_rect)
            icon_rect1 = upgrades_icon_list[upgrade1].get_rect()
            icon_rect1.center = (287.5, 325)
            icon_rect2 = upgrades_icon_list[upgrade2].get_rect()
            icon_rect2.center = (731.25, 325)
            window.blit(upgrades_icon_list[upgrade1], icon_rect1)
            window.blit(upgrades_icon_list[upgrade2], icon_rect2)
            # Click Detection
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (pygame.Rect(75, 150, 412.5, 275)).collidepoint(
                        event.pos
                    ):
                        click_sfx.play()
                        if upgrade1 == 0:
                            enemy_speed -= (5 / 100) * enemy_speed
                        elif upgrade1 == 1:
                            player_speed += (5 / 100) * player_speed
                        elif upgrade1 == 2:
                            invincibility_time += 30
                        elif upgrade1 == 3:
                            if torches_required > 1:
                                torches_required -= 1
                        elif upgrade1 == 4:
                            if kills_required > 1:
                                kills_required -= 1
                        elif upgrade1 == 5:
                            torch_rect = torch_image.get_rect()
                            torch_rect.center = (
                                random.randint(0, width),
                                random.randint(0, height),
                            )
                            torch_rect_list.append(torch_rect)
                        elif upgrade1 == 6:
                            double_heal_chance += 0.01
                        elif upgrade1 == 7:
                            increase -= (0.1 / 100) * increase
                        change = True
                        upgrade = False
                        break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (pygame.Rect(512.5, 150, 412.5, 275)).collidepoint(
                        event.pos
                    ):
                        click_sfx.play()
                        if upgrade2 == 0:
                            enemy_speed -= (5 / 100) * enemy_speed
                        elif upgrade2 == 1:
                            player_speed += (5 / 100) * player_speed
                        elif upgrade2 == 2:
                            invincibility_time += 30
                        elif upgrade2 == 3:
                            if torches_required > 1:
                                torches_required -= 1
                        elif upgrade2 == 4:
                            if kills_required > 1:
                                kills_required -= 1
                        elif upgrade2 == 5:
                            torch_rect = torch_image.get_rect()
                            torch_rect.center = (
                                random.randint(0, width),
                                random.randint(0, height),
                            )
                            torch_rect_list.append(torch_rect)
                        elif upgrade2 == 6:
                            double_heal_chance += 0.01
                        elif upgrade2 == 7:
                            increase -= (0.1 / 100) * increase
                        change = True
                        upgrade = False
                        break
        if invincibility and not upgrade:
            count += 1
            player_shield_rect.center = (player_x, player_y)
            window.blit(player_shield_image, player_shield_rect)
        if count == invincibility_time:
            invincibility = False
            count = 0
        if health == 0:
            pygame.mixer.music.load("Assets\\Game Over.mp3")
            pygame.mixer.music.play()
            scores = open("Assets\\Scores.txt", "a+")
            scores.write(str(score))
            scores.write("\n")
            scores.seek(0)
            scoring_list = scores.readlines()
            highscore_list = []
            for a in scoring_list:
                highscore_list.append(int(a))
            highscore = max(highscore_list)
            scores.close()
            gameover = True
        if boss_immunity and not upgrade:
            boss_immunity_timer += 1
            boss_shield_rect.center = (boss_x, boss_y)
            window.blit(boss_shield_image, boss_shield_rect)
        if boss_immunity_timer == boss_immunity_time:
            boss_immunity = False
            boss_immunity_timer = 0
        if boss_health == 0:
            pygame.mixer.Channel(7).play(boss_died_sfx)
            score += 100
            boss_score_rect.center = (boss_rect.centerx, boss_rect.centery)
            boss_score_appear = True
            boss_change = True
            bosses_killed += 1
            if player_health < 3:
                player_health += 1
            if (
                player_health == 2 and double_heal_chance > 0 and random.random() < double_heal_chance
            ):
                player_health = 3
            boss = False
            boss_x = random.choice([-100, 1100])
            boss_y = random.choice([-100, 650])
            boss_rect.center = (boss_x, boss_y)
            boss_immunity_time += 30
            boss_max_health += 1
            boss_health = boss_max_health
            boss_speed += (5 / 100) * boss_speed
        if boss_score_appear:
            boss_score_count += 1
            window.blit(boss_score, boss_score_rect)
        if boss_score_count == 60:
            boss_score_count = 0
            boss_score_appear = False
    if gameover:
        game_track.stop()
        window.blit(gameover_image, gameover_rect)
        retry_button_rect = retry_button_image.get_rect()
        retry_button_rect.center = (275, 400)
        window.blit(retry_button_image, retry_button_rect)
        menu_button_rect = menu_button_image.get_rect()
        menu_button_rect.center = (725, 400)
        window.blit(menu_button_image, menu_button_rect)
        highscore_text = score_font.render(
            "High Score:" + str(highscore), True, red
        )
        highscore_rect = highscore_text.get_rect()
        highscore_rect.center = (725, 300)
        score_text = score_font.render("Total Score:" + str(score), True, red)
        score_rect = score_text.get_rect()
        score_rect.center = (275, 300)
        window.blit(score_text, score_rect)
        window.blit(highscore_text, highscore_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button_rect.collidepoint(event.pos):
                    time = "00:00:00"
                    frames = 0
                    seconds = 0
                    minutes = 0
                    hours = 0
                    click_sfx.play()
                    r = 0
                    g = 0
                    b = 0
                    increase = 0.5
                    player_x = width / 2
                    player_y = height / 2
                    player_rect = player_image.get_rect()
                    player_rect.center = (player_x, player_y)
                    player_speed = 2.5
                    knife = False
                    health_rect1 = health_image.get_rect()
                    health_rect1.center = (5 + 15, 15 + 5)
                    health_rect2 = health_image.get_rect()
                    health_rect2.center = (5 + 15 + 10 + 15, 15 + 5)
                    health_rect3 = health_image.get_rect()
                    health_rect3.center = (5 + 15 + 10 + 15 + 10 + 15, 15 + 5)
                    health = 3
                    boss_x = -100
                    boss_y = -100
                    boss_rect.center = (boss_x, boss_y)
                    boss = False
                    double_heal_chance = 0
                    invincibility = False
                    invincibility_time = 120
                    count = 0
                    kills = 0
                    torch_rect_list = []
                    total = 5
                    torches_broken = 0
                    torches_required = 10
                    for a in range(0, total):
                        torch_rect = torch_image.get_rect()
                        torch_rect.center = (
                            random.randint(0, width - 10),
                            random.randint(0, height - 10),
                        )
                        torch_rect_list.append(torch_rect)
                    torch_change = False
                    enemy_x = 0
                    enemy_y = 0
                    enemy_rect.center = (enemy_x, enemy_y)
                    enemy_speed = 1.25
                    yes = 0
                    upgrade = False
                    change = False
                    score = 0
                    gamestart = True
                    gameover = False
                    pause = False
                    break
                elif menu_button_rect.collidepoint(event.pos):
                    time = "00:00:00"
                    frames = 0
                    seconds = 0
                    minutes = 0
                    hours = 0
                    click_sfx.play()
                    r = 0
                    g = 0
                    b = 0
                    increase = 0.5
                    player_x = width / 2
                    player_y = height / 2
                    player_rect = player_image.get_rect()
                    player_rect.center = (player_x, player_y)
                    player_speed = 2.5
                    knife = False
                    health_rect1 = health_image.get_rect()
                    health_rect1.center = (5 + 15, 15 + 5)
                    health_rect2 = health_image.get_rect()
                    health_rect2.center = (5 + 15 + 10 + 15, 15 + 5)
                    health_rect3 = health_image.get_rect()
                    health_rect3.center = (5 + 15 + 10 + 15 + 10 + 15, 15 + 5)
                    health = 3
                    boss_x = -100
                    boss_y = -100
                    boss_rect.center = (boss_x, boss_y)
                    boss = False
                    double_heal_chance = 0
                    invincibility = False
                    invincibility_time = 120
                    count = 0
                    kills = 0
                    torch_rect_list = []
                    total = 5
                    torches_broken = 0
                    torches_required = 10
                    for a in range(0, total):
                        torch_rect = torch_image.get_rect()
                        torch_rect.center = (
                            random.randint(0, width - 10),
                            random.randint(0, height - 10),
                        )
                        torch_rect_list.append(torch_rect)
                    torch_change = False
                    enemy_x = 0
                    enemy_y = 0
                    enemy_rect.center = (enemy_x, enemy_y)
                    enemy_speed = 1.25
                    yes = 0
                    upgrade = False
                    change = False
                    score = 0
                    gamestart = False
                    gameover = False
                    pause = False
                    break
    pygame.display.update()
    clock.tick(fps)
