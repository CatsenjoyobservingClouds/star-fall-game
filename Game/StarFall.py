import pygame
import os
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
CENTERW, CENTERH = WIDTH/2, HEIGHT/2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

GAME2_BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'images', 'game2_background.jpg')), (WIDTH, HEIGHT))
GAME1_BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'images', 'game1_background.jpg')), (WIDTH, HEIGHT))
MENU_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(
            'assets', 'images', 'menu_background.jpeg')), (WIDTH, HEIGHT))
END_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join(
        'assets', 'images', 'end_background.jpg')), (WIDTH, HEIGHT))

END_ICON = pygame.image.load(
        os.path.join('assets', 'images', 'end_icon.png'))
MENU_ICON = pygame.image.load(
        os.path.join('assets', 'images', 'menu_icon.jpg'))
GAME1_ICON = pygame.image.load(
        os.path.join('assets', 'images', 'game1_icon.png'))
GAME2_ICON = pygame.image.load(
        os.path.join('assets', 'images', 'game2_icon.png'))

BULLET_HIT_SOUND = pygame.mixer.Sound(
    os.path.join('assets', 'audios', 'hit.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(
    os.path.join('assets', 'audios', 'fire.mp3'))
END_SOUND = pygame.mixer.Sound(os.path.join('assets', 'audios', 'end.wav'))
END2_SOUND = pygame.mixer.Sound(os.path.join('assets', 'audios', 'end2.wav'))
LOST_SOUND = pygame.mixer.Sound(
    os.path.join('assets', 'audios', 'minus_life.wav'))
BONUS_SOUND = pygame.mixer.Sound(os.path.join('assets', 'audios', 'bonus.wav'))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 80)
MENU_FONT = pygame.font.SysFont('comicsans', 60)
MAIN_FONT = pygame.font.SysFont('comicsans', 150)
SUB_FONT = pygame.font.SysFont('ariablack', 40)
BUTTON_FONT = pygame.font.SysFont('comicsans', 35)
SCORE_FONT = pygame.font.SysFont('comicsans', 30)

ENEMY_WIDTH = 80
ENEMY_HEIGHT = 80
BORDER = pygame.Rect(0, CENTERH-2.5, WIDTH, 5)

N_HEALTH = 10
PLANET_WIDTH = 30
PLANET_HEIGHT = 30
STAR_WIDTH = 20
STAR_HEIGHT = 20

VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
BULLET_WIDTH = 10
BULLET_HEIGHT = 25

FIRST_HIT = pygame.USEREVENT + 1
SECOND_HIT = pygame.USEREVENT + 2
PLANET_PICKED = pygame.USEREVENT + 3
STAR_PICKED = pygame.USEREVENT + 4
LIFE_LOST = pygame.USEREVENT + 5

enemy1 = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'enemy_2.png')), (ENEMY_WIDTH, ENEMY_HEIGHT))  # works for different platforms
enemy2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'images', 'enemy_1.png')), (ENEMY_WIDTH, ENEMY_HEIGHT)), 0)


mercury = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'mercury.png')), (PLANET_WIDTH, PLANET_HEIGHT))
venus = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'venus.png')), (1.35*PLANET_WIDTH, 1.35*PLANET_HEIGHT))
earth = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'earth.png')), (1.4*PLANET_WIDTH, 1.4*PLANET_HEIGHT))
mars = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'mars.png')), (1.2*PLANET_WIDTH, 1.2*PLANET_HEIGHT))
jupiter = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'jupiter.png')), (2.5*PLANET_WIDTH, 2.5*PLANET_HEIGHT))
saturn = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'saturn.png')), (4.3*PLANET_WIDTH, 2*PLANET_HEIGHT))
uranus = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'uranus.png')), (3.5*PLANET_WIDTH, 1.8*PLANET_HEIGHT))
neptune = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'neptune.png')), (1.5*PLANET_WIDTH, 1.5*PLANET_HEIGHT))

PLANETS = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

blue = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'blue.png')), (STAR_WIDTH, STAR_HEIGHT))
red = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'red.png')), (PLANET_WIDTH, PLANET_HEIGHT))
yellow = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'yellowish.png')), (PLANET_WIDTH, PLANET_HEIGHT))

STARS = [blue, red, yellow]

DRAGON_WIDTH = 100
DRAGON_HEIGHT = 100
dragonl = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'dragonl.png')), (DRAGON_WIDTH, DRAGON_HEIGHT))
dragonr = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'dragonr.png')), (DRAGON_WIDTH, DRAGON_HEIGHT))

VEL_DRAGON = 7


def draw_window(first, second, first_bullets, second_bullets, first_health, second_health):
    WIN.fill(WHITE)
    WIN.blit(GAME2_BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    first_text = HEALTH_FONT.render("Health: " + str(first_health), 1, WHITE)
    second_text = HEALTH_FONT.render(
        "Health: " + str(second_health), 1, (0, 20, 150))
    WIN.blit(first_text, (0, 0))
    WIN.blit(second_text, (0, HEIGHT-second_text.get_height()))

    WIN.blit(enemy1, (first.x, first.y))
    WIN.blit(enemy2, (second.x, second.y))

    for bullet in first_bullets:
        pygame.draw.rect(WIN, BLUE, bullet, 0, 100, 0, 0, 100)

    for bullet in second_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet, 0, 0, 100, 100, 0)


def game2():
    pygame.mixer.music.load(os.path.join('assets', 'audios', 'game2.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.35)
    pygame.display.set_caption("Game 2")
    pygame.display.set_icon(GAME2_ICON)
    first = pygame.Rect(CENTERW-ENEMY_WIDTH/2, 10, ENEMY_WIDTH, ENEMY_HEIGHT)
    second = pygame.Rect(CENTERW-ENEMY_WIDTH/2, HEIGHT -
                         10-ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT)

    first_bullets = []
    second_bullets = []
    first_health = 10
    second_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # 60 times per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    menu()
                    return

                if event.key == pygame.K_LCTRL and len(first_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(first.x + first.width/2 - BULLET_WIDTH/2,
                                         first.y + first.height - 2, BULLET_WIDTH, BULLET_HEIGHT)
                    first_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(second_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        second.x + second.width/2 - BULLET_WIDTH/2, second.y - 2, BULLET_WIDTH, BULLET_HEIGHT)
                    second_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == FIRST_HIT:
                first_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == SECOND_HIT:
                second_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if first_health <= 0:
            winner_text = "Pikachu wins"
        if second_health <= 0:
            winner_text = "Totoro wins"
        if winner_text != "":
            break

        keys_pressed = pygame.key.get_pressed()
        enemy1_movement(keys_pressed, first)
        enemy2_movement(keys_pressed, second)
        handle_bullets(first_bullets, second_bullets, first, second)
        draw_window(first, second, first_bullets,
                    second_bullets, first_health, second_health)

        pygame.display.update()
    END_SOUND.set_volume(0.5)
    draw_winner(winner_text, END_SOUND)


def enemy1_movement(keys_pressed, first):
    if keys_pressed[pygame.K_a] and first.x - VEL > 0:
        first.x -= VEL
    if keys_pressed[pygame.K_d] and first.x + VEL + first.width < WIDTH:
        first.x += VEL
    if keys_pressed[pygame.K_w] and first.y - VEL > 0:
        first.y -= VEL
    if keys_pressed[pygame.K_s] and first.y + VEL + first.height < BORDER.y:
        first.y += VEL


def enemy2_movement(keys_pressed, second):
    if keys_pressed[pygame.K_LEFT] and second.x - VEL > 0:
        second.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and second.x + VEL + second.width < WIDTH:
        second.x += VEL
    if keys_pressed[pygame.K_UP] and second.y - VEL > BORDER.y + BORDER.height:
        second.y -= VEL
    if keys_pressed[pygame.K_DOWN] and second.y + VEL + second.height < HEIGHT:
        second.y += VEL


def handle_bullets(first_bullets, second_bullets, first, second):
    for bullet in first_bullets:
        bullet.y += BULLET_VEL
        if second.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SECOND_HIT))
            first_bullets.remove(bullet)
        elif bullet.y > HEIGHT:
            first_bullets.remove(bullet)

    for bullet in second_bullets:
        bullet.y -= BULLET_VEL
        if first.colliderect(bullet):
            pygame.event.post(pygame.event.Event(FIRST_HIT))
            second_bullets.remove(bullet)
        elif bullet.y + bullet.height < 0:
            second_bullets.remove(bullet)


def draw_winner(text, sound):
    pygame.display.set_caption("Hooray")
    pygame.display.set_icon(END_ICON)
    pygame.mixer.music.stop()
    sound.play()
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.fill(WHITE)
    WIN.blit(END_BACKGROUND, (0, 0))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
             2, HEIGHT/2 - draw_text.get_height()/2 - 100))
    pygame.display.update()
    pygame.time.delay(2000)

    return_button = Button("return to menu", "return to menu", "#22aaff",
                           "#002E5A", BUTTON_FONT, WIDTH/2, HEIGHT/2 + 30, menu)
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        return_button.draw()
        pygame.display.update()


def menu():
    pygame.mixer.music.load(os.path.join('assets', 'audios', 'menu.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.8)
    pygame.display.set_caption("Menu")
    pygame.display.set_icon(MENU_ICON)
    one = Button("1 Player", "play", "#85C4FF", WHITE,
                 MENU_FONT, WIDTH/2 - 150, HEIGHT/2 + 80, game1)
    two = Button("2 Players", "play", "#85C4FF", WHITE,
                 MENU_FONT, WIDTH/2 + 150, HEIGHT/2 + 80, game2)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        WIN.fill(WHITE)
        WIN.blit(MENU_BACKGROUND, (0, 0))
        draw_text = MAIN_FONT.render("CHOOSE", True, "#A3B3FF")
        WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                 2, HEIGHT/2 - draw_text.get_height()/2 - 120))

        delete_text = SUB_FONT.render(
            "press Delete to quit any game", True, "#67B6FF")
        WIN.blit(delete_text, (WIDTH - delete_text.get_width() -
                 20, HEIGHT/2 - delete_text.get_height()/2 + 300))
        one.draw()
        two.draw()

        pygame.display.update()


surf_rect = HEIGHT - 10
def game1():
    pygame.mixer.music.load(os.path.join('assets', 'audios', 'game1.mp3'))
    pygame.mixer.music.play(-5)
    pygame.mixer.music.set_volume(0.4)
    pygame.display.set_caption("Game 1")
    pygame.display.set_icon(GAME1_ICON)

    global vel_jump, m, jumped, dragon, surf_rect
    dragon = pygame.transform.scale(pygame.image.load(os.path.join(
        'assets', 'images', 'dragonl.png')), (DRAGON_WIDTH, DRAGON_HEIGHT))
    vel_jump = 10
    m = 1
    jumped = False
    surf_rect = HEIGHT - 10
    planets = []
    stars = []
    score = 0
    planet_vel = 3
    star_vel = 6
    health = N_HEALTH
    health_rect = pygame.Rect(WIDTH - 165, 72.5, 140, 25)
    dragon_rect = pygame.Rect(WIDTH // 2 - dragon.get_width() // 2,
                              HEIGHT-dragon.get_height() - 10, dragon.get_width(), dragon.get_height())
    clock = pygame.time.Clock()
    run = True
    delay = 3840
    while run:
        clock.tick(FPS)  # 60 times per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    menu()
                    return

            if event.type == LIFE_LOST:
                health -= 1
                health_rect = pygame.Rect(
                    health_rect.x + 14, 72.5, health_rect.width - 14, 25)
                pygame.draw.rect(WIN, BLACK, health_rect)
                pygame.display.update()
                LOST_SOUND.play()

            if event.type == STAR_PICKED:
                score += 25
                BONUS_SOUND.play()

        delay += 1
        if delay % (96-(star_vel-5)*6) == 0:
            score += 1
            planet = PLANETS[random.randint(0, 7)]
            planets.append([planet, pygame.Rect(random.randint(5, WIDTH - 15 - planet.get_width()), 0 -
                           planet.get_height() - random.randint(0, 30), planet.get_width(), planet.get_height())])
        if delay % (480-(star_vel-5)*6) == 0:
            star = STARS[random.randint(0, 2)]
            stars.append([star, pygame.Rect(random.randint(5, WIDTH - 15 - star.get_width()), 0 -
                         star.get_height() - random.randint(0, 30), star.get_width(), star.get_height())])
        if delay % 1440 == 0:
            star_vel += 1
            planet_vel += 0.5
            delay = 1440

        if health <= 0:
            break

        keys_pressed = pygame.key.get_pressed()
        dragon_movement(keys_pressed, dragon_rect)
        handle_planets(planets, stars, dragon_rect, star_vel, planet_vel)
        draw_game1(dragon_rect, score, health_rect, planets, stars)
        pygame.display.update()
    draw_winner("Your score: " + str(score), END2_SOUND)


def draw_game1(dragon_rect, score, health_rect, planets, stars):
    global surf_rect
    WIN.fill(WHITE)
    WIN.blit(GAME1_BACKGROUND, (0, 0))

    for planet in planets:
        WIN.blit(planet[0], (planet[1].x, planet[1].y))

    for star in stars:
        WIN.blit(star[0], (star[1].x, star[1].y))

    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (WIDTH-score_text.get_width() - 35, 5))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(WIDTH - 170, 70, 150, 30))
    pygame.draw.rect(WIN, BLACK, health_rect)

    WIN.blit(dragon, (dragon_rect.x, dragon_rect.y + 3))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(
        0, surf_rect, WIDTH, HEIGHT - surf_rect + dragon_rect.width))


vel_jump = 10
m = 1
jumped = False
dragon = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'images', 'dragonl.png')), (DRAGON_WIDTH, DRAGON_HEIGHT))


def dragon_movement(keys_pressed, dragon_rect):
    global vel_jump, m, jumped, dragon, surf_rect
    if keys_pressed[pygame.K_LEFT] and dragon_rect.x - VEL_DRAGON > 0:
        if keys_pressed[pygame.K_UP]:
            dragon_rect.x -= (VEL_DRAGON + 3)
        else:
            dragon_rect.x -= VEL_DRAGON
        dragon = dragonl
    if keys_pressed[pygame.K_RIGHT] and dragon_rect.x + VEL_DRAGON + dragon_rect.width < WIDTH:
        if keys_pressed[pygame.K_UP]:
            dragon_rect.x += (VEL_DRAGON + 3)
        else:
            dragon_rect.x += VEL_DRAGON
        dragon = dragonr
    if jumped == False and keys_pressed[pygame.K_SPACE]:
        jumped = True
    elif jumped:
        f = 0.5*m*(vel_jump**2)
        dragon_rect.y -= f
        vel_jump = vel_jump - 1
        if vel_jump < 0:
            m = -1
        if vel_jump < -10:
            jumped = False
            vel_jump = 10
            m = 1
            if dragon_rect.y - 185 > 0:
                surf_rect -= 5


def handle_planets(planets, stars, dragon_rect, star_vel, planet_vel):
    global surf_rect
    for planet in planets:
        planet[1].y += planet_vel
        
        if dragon_rect.colliderect(planet[1]):
            planets.remove(planet)
        elif planet[1].y > surf_rect:
            pygame.event.post(pygame.event.Event(LIFE_LOST))
            planets.remove(planet)
    for star in stars:
        star[1].y += star_vel
        if dragon_rect.colliderect(star[1]):
            pygame.event.post(pygame.event.Event(STAR_PICKED))
            stars.remove(star)
        elif star[1].y > surf_rect:
            stars.remove(star)


class Button():
    def __init__(self, text, change_text, color, background_color, font, pos_x, pos_y, function):
        self.pressed = False
        self.function = function

        self.change_text = change_text
        self.background_color = background_color
        self.color = color
        self.text = text
        self.font = font

        self.text_surf = font.render(text, True, color)
        self.top_rect = pygame.Rect(pos_x - self.text_surf.get_width()/2, pos_y - self.text_surf.get_height(
        )/2, self.text_surf.get_width() + 20, self.text_surf.get_height())

        self.top_color = background_color
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(WIN, self.top_color, self.top_rect, border_radius=10)
        WIN.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            clock = pygame.time.Clock()
            clock.tick(15)
            self.top_color = self.color
            self.text_surf = self.font.render(
                self.change_text, True, self.background_color)
            self.text_rect = self.text_surf.get_rect(
                center=self.top_rect.center)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    self.pressed = False
                    pygame.mixer.music.stop()
                    pygame.time.delay(500)
                    self.function()
        else:
            self.top_color = self.background_color
            self.text_surf = self.font.render(self.text, True, self.color)
            self.text_rect = self.text_surf.get_rect(
                center=self.top_rect.center)


# for safe import later
if __name__ == "__main__":
    menu()
