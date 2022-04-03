import pygame
import random

pygame.init()

#размеры дисплея
display_widht = 800
display_height = 600

#создание дисплея
display = pygame.display.set_mode((display_widht, display_height))
pygame.display.set_caption('Run Creeper! Run!')

#замена иконки на свою
icon = pygame.image.load(r'backgrouds\icon.png')
pygame.display.set_icon(icon)

#массив куда идет загрузка всех картинок с кактусами
cactus_img = [
    pygame.image.load(r'objects\cactus0.png'),
    pygame.image.load(r'objects\cactus1.png'),
    pygame.image.load(r'objects\cactus2.png')
]
#координаты кактусов, на нечет. местах корды по X, на четных корды по Y
cactus_option = [33, 448, 30, 435, 32, 431]

#топорно сделаная анимация крипера
creeper_img = [pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper1.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png'),
            pygame.image.load(r'creeper\creeper2.png')
            ]

img_counter = 0

health_img = pygame.image.load(r'effects\tnt.jpg')
health_img = pygame.transform.scale(health_img, (30, 30))
health = 1

cloud_img = [
    pygame.image.load(r'objects\cloud1.png'),
    pygame.image.load(r'objects\cloud2.png')
]

ore_img = [
            pygame.image.load(r'objects\cola_ore.png'),
            pygame.image.load(r'objects\diamond_ore.png'),
            pygame.image.load(r'objects\diamond_ore.png'),
            pygame.image.load(r'objects\cola_ore.png'),
            pygame.image.load(r'objects\iron_ore.png'),
            pygame.image.load(r'objects\iron_ore.png')
]


jump_sound = pygame.mixer.Sound(r'sounds\say1.ogg ')
fail_sound = pygame.mixer.Sound(r'sounds\explode4.ogg ')
hit_sound = pygame.mixer.Sound(r'sounds\hit1.ogg')
heart_plus_sound = pygame.mixer.Sound(r'sounds\healt.ogg')
button_sound = pygame.mixer.Sound(r'sounds\click.ogg')


score = 0
record_score = open('record_score.txt')
record_score.seek(0)
max_scores = int(record_score.readline())
record_score.close()

jumped_over_cactus = 0
record_jump = open('record_jump.txt')
record_jump.seek(0)
max_jump = int(record_jump.readline())
record_jump.close()

max_above = 0

sky = pygame.image.load(r'backgrouds\sky.jpg')
land0 = pygame.image.load(r'backgrouds\fon.jpg')
land1 = pygame.image.load(r'backgrouds\fon_sand.jpg')

button = pygame.image.load(r'backgrouds\button.png')

#класс кактуса с размерами и скоростью
class Object:
    def __init__(self, x, y, widht, image, speed):
        self.x = x
        self.y = y
        self.widht = widht
        self.speed = speed
        self.image = image

    def move(self):
        if self.x >= -self.widht:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            self.speed = self.speed * 1.00007
            return True
        else:
            return False

    def return_self(self, radius, y, widht, image):
        self.x = radius
        self.y = y
        self.widht = widht
        self.image = image
        display.blit(self.image, (self.x, self.y))

class Button:
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height
        self.inactive_color = (0, 0, 0)
        self.active_color = (255, 255, 255)

    def draw(self, x, y, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.widht and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_color, (x, y, self.widht, self.height))


            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    action()

        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.widht, self.height))


user_widht = 63
user_height = 97
user_x = 50
user_y = display_height - user_height - 97


clock = pygame.time.Clock()

make_jump = False
jump_counter = 30



def show_menu():
    menu_back = pygame.image.load(r'backgrouds\menu.jpg')
    show = True

    start_button = Button(288, 55)
    quit_button = Button(288, 55)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()


        display.blit(menu_back, (0, 0))
        start_button.draw(488, 294, start_game)
        quit_button.draw(488, 356, quit)
        display.blit(button, (488, 294))
        display.blit(button, (488, 356))
        print_text('Start game', 585, 314)
        print_text('Close game', 585, 376)
        pygame.display.update()
        clock.tick(60)


def start_game():
    global jumped_over_cactus, make_jump, jump_counter, user_y, health, score

    health = 1
    while game_cycle():
        score = 0
        jumped_over_cactus = 0
        make_jump = False
        jump_counter = 30
        user_y = display_height - user_height - 100

def open_random_music():
    music = random.randrange(0, 6)
    if music == 0:
        pygame.mixer.music.load(r'musics\Aria Math.mp3 ')
    elif music == 1:
        pygame.mixer.music.load(r'musics\Beginning 2.mp3')
    elif music == 2:
        pygame.mixer.music.load(r'musics\Haunt Muskie.mp3')
    elif music == 3:
        pygame.mixer.music.load(r'musics\Living Mice.mp3')
    elif music == 4:
        pygame.mixer.music.load(r'musics\Mice on Venus.mp3')
    else:
        pygame.mixer.music.load(r'musics\Blind Spots.mp3')

    music_play = pygame.mixer.music.play()
    music_repeat = pygame.mixer.music.play(-1)
    return music_play, music_repeat


#функция для запуска игры
def game_cycle():
    global make_jump

    open_random_music()

    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    cloud, ore = open_random_objects()

    heart = Object(display_widht, 280, 30, health_img, 5)


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] or key[pygame.K_UP]:
            make_jump = True
        if key[pygame.K_ESCAPE]:
            pause()

        if make_jump:
            jump()

        count_scores(cactus_arr)

        display.blit(sky, (0, 0))
        display.blit(land0, (0, 500))

        print_text('Scores: ' + str(round(score)), 550, 10)
        print_text('Jumped over cactus: ' + str(jumped_over_cactus), 550, 30)
        print_text('SPACE or K_UP for jump', 550, 50)
        print_text('ESC for pause', 550, 70)


        draw_array(cactus_arr)
        move_objects(cloud, ore)
        draw_creeper()


        if check_collision(cactus_arr):
            pygame.mixer.music.stop()
            game = False

        heart.move()
        hearts_plus(heart)
        show_health()


        pygame.display.update()
        clock.tick(60)

    return game_over()


def jump():
    global user_y, make_jump, jump_counter
    if jump_counter >= -30:
        if jump_counter == 30:
            pygame.mixer.Sound.play(jump_sound)
        user_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_cactus_arr(array):
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    widht = cactus_option[choice * 2]
    height = cactus_option[choice * 2 +1]
    array.append(Object(display_widht + 20, height, widht, img, 5))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    widht = cactus_option[choice * 2]
    height = cactus_option[choice * 2 +1]
    array.append(Object(display_widht + 300, height, widht, img, 5))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    widht = cactus_option[choice * 2]
    height = cactus_option[choice * 2 +1]
    array.append(Object(display_widht + 600, height, widht, img, 5))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_widht:
        radius = display_widht
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum

    if score < 1000:
        choise = random.randrange(0, 5)
        if choise == 0:
            radius += random.randrange(30, 31)
        else:
            radius += random.randrange(700, 1400)
    elif score <=1500:
        choise = random.randrange(0, 5)
        if choise == 0:
            radius += random.randrange(30, 31)
        else:
            radius += random.randrange(1050, 2100)
    else:
        choise = random.randrange(0, 5)
        if choise == 0:
            radius += random.randrange(30, 31)
        else:
            radius += random.randrange(1400, 2800)

    return radius


def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array, cactus)



def draw_creeper():
    global img_counter
    if img_counter == 16:
        img_counter = 0
    display.blit(creeper_img[img_counter], (user_x, user_y))
    img_counter += 1



def object_return(objects, obj):
    radius = find_radius(objects)

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    widht = cactus_option[choice * 2]
    height = cactus_option[choice * 2 + 1]

    obj.return_self(radius, height, widht, img)


def open_random_objects():
    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]
    cloud = Object(display_widht, 80, 155, img_of_cloud, 2.5)

    choice1 = random.randrange(0, 6)
    img_of_ore = ore_img[choice1]
    ore = Object(0, display_height - 88, 800, img_of_ore, 5)


    return cloud, ore


def move_objects(cloud, ore):

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_widht, random.randrange(10, 200), cloud.widht, img_of_cloud)

    check = ore.move()
    if not check:
        choice1 = random.randrange(0, 6)
        img_of_ore = ore_img[choice1]
        ore.return_self(display_widht, display_height - 88, ore.widht, img_of_ore)


def print_text(message, x, y, font_color = (0, 0, 0), font_type = r'backgrouds\9303.ttf', font_size=15):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def print_text1(message, x, y, font_color = (0, 0, 0), font_type = r'backgrouds\9303.ttf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def pause():
        paused = True

        pygame.mixer.music.pause()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()

            print_text1('Pause!', 301, 50)
            print_text('Press ENTER to continue or Q for exit', 234, 150)
            print_text('If you exit, the record will not be saved', 224, 175)

            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                paused = False
            if key[pygame.K_q]:
                pygame.quit()
                quit()

            pygame.display.update()
            clock.tick(15)

        pygame.mixer.music.unpause()

def count_scores(barriers):
    global jumped_over_cactus, max_above, score
    above_cactus = 0
    score += 0.055

    if -20 <= jump_counter < 25:
        for barrier in barriers:
            if user_y + user_height <= barrier.y:
                if barrier.x <= user_x <= barrier.x + barrier.widht:
                    above_cactus += 1
                elif barrier.x <= user_x + user_widht <= barrier.x + barrier.widht:
                    above_cactus += 1
        max_above = max(max_above, above_cactus)
    else:
        if jump_counter == -30:
            jumped_over_cactus += max_above
            max_above = 0



def game_over():
    global jumped_over_cactus, max_scores, max_jump, score

    if score > max_scores:
        max_scores = score
        mx_str = str(round(max_scores))
        record_score = open('record_score.txt', 'w')
        record_score.write(mx_str)
        record_score.close()

    if jumped_over_cactus > max_jump:
        max_jump = jumped_over_cactus
        mx_str = str(max_jump)
        record_jump = open('record_jump.txt', 'w')
        record_jump.write(mx_str)
        record_jump.close()
        print(max_jump)

    jumped_over_cactus = 0
    score = 0
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text1('You died! ', 270, 200)
        print_text1('Your record: ' + str(round(max_scores)) + '!', 150, 250)
        print_text('Max jumped over cactus: ' + str(max_jump) + '!', 280, 310)

        open_menu_rect = Button(288, 55)
        close_game_rect = Button(288, 55)
        start_over_rect = Button(288, 55)

        open_menu = open_menu_rect.draw(111, 338, show_menu)
        display.blit(button, (111, 338))
        print_text('Open menu', 208, 358)

        start_over = close_game_rect.draw(421, 338, start_game)
        display.blit(button, (421, 338))
        print_text('Start over', 517, 358)

        close_game = start_over_rect.draw(266, 400, quit)
        display.blit(button, (266, 400))
        print_text('Exit game', 370, 420) 

        if open_menu:
            return False
        elif close_game:
            return True

        #key = pygame.key.get_pressed()
        #if key[pygame.K_RETURN]:
        #    return True
        #if key[pygame.K_ESCAPE]:
        #    return False

        pygame.display.update()
        clock.tick(15)

def check_collision(barriers):
    for barrier in barriers:
        if not make_jump:
            if barrier.x  <= user_x + user_widht - 10<= barrier.x + barrier.widht:
                if check_healt():
                    object_return(barriers, barrier)
                    return False
                else:
                    return True
        else:
            if user_y + user_height >= barrier.y:
                if (barrier.x <= user_x + user_widht - 10 <= barrier.x + barrier.widht) or (barrier.x <= user_x <= barrier.x + barrier.widht):
                    if check_healt():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
    return False

def show_health():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img, (x ,20))
        x += 40
        show += 1


def check_healt():
    global health
    health -=1
    if health == 0:
        pygame.mixer.Sound.play(fail_sound)
        return False
    else:
        pygame.mixer.Sound.play(hit_sound)
        return True


def hearts_plus(heart):
    global health, user_x, user_y, user_widht, user_height

    if heart.x <= heart.widht:
        radius = display_widht + random.randrange(500, 10000)
        heart.return_self(radius, random.randrange(280, 400), heart.widht, heart.image)

    if user_x <= heart.x <= user_x + user_widht:
        if user_y <= heart.y + heart.widht <= user_y + user_height:
            pygame.mixer.Sound.play(heart_plus_sound)
            if health < 3:
                health += 1

            radius = display_widht + random.randrange(500, 10000)
            heart.return_self(radius, random.randrange(280, 400), heart.widht, heart.image)

show_menu()
pygame.quit()
quit()
