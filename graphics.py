import pygame
pygame.init()

size = (600, 600)

screen = pygame.display.set_mode(size)

image_file = pygame.image.load("images/saved.JPG")

image = pygame.transform.scale(image_file, (600,600))

def brighten():
    for x in range(0, 600):
        for y in range(0, 600):
            color = screen.get_at((x, y))
            r = color[0] + 15
            g = color[1] + 15
            b = color[2] + 15

            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255

            screen.set_at((x, y), (r, g, b))

def darken():
    for x in range(0, 600):
        for y in range(0, 600):
            color = screen.get_at((x, y))
            r = color[0] - 15
            g = color[1] - 15
            b = color[2] - 15

            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0

            screen.set_at((x, y), (r, g, b))

def removeRed():
    for x in range(0,600):
        for y in range(0,600):
            color = screen.get_at((x, y)) # color = [r,g,b,a]

            r = 0
            g = color[1]
            b = color[2]

            screen.set_at((x, y), (r, g, b))

def removeGreen():
    for x in range(0,600):
        for y in range(0,600):
            color = screen.get_at((x, y)) # color = [r,g,b,a]

            r = color[0]
            g = 0
            b = color[2]

            screen.set_at((x, y), (r, g, b))

def removeBlue():
    for x in range(0,600):
        for y in range(0,600):
            color = screen.get_at((x, y)) # color = [r,g,b,a]

            r = color[0]
            g = color[1]
            b = 0

            screen.set_at((x, y), (r, g, b))

def negate():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))

            r = 255 - color[0] # r = 100, new r = 155
            g = 255 - color[1] # g = 55, new g = 200
            b = 255 - color[2]

            screen.set_at((x, y), (r, g, b))

def intensify():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x,y))

            r = color[0]
            g = color[1]
            b = color[2]

            if r > 255/2:
                r = 255
            else:
                r = 0

            if g > 255/2:
                g = 255
            else:
                g = 0

            if b > 255/2:
                b = 255
            else:
                b = 0

            screen.set_at((x, y), (r, g, b))

def grayscale():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x,y))

            r = color[0]
            g = color[1]
            b = color[2]

            average = (r+g+b)/3

            screen.set_at((x,y), (average, average, average))

def twoTone():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x,y))

            r = color[0]
            g = color[1]
            b = color[2]

            # New work:

            brightness = r + g + b

            if brightness > (255*3)/2.0:
               screen.set_at((x,y), (255, 255, 255))

            else:
                screen.set_at((x,y), (0, 0, 0))

def fourTone():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))

            max = 255*3

            r = color[0]
            g = color[1]
            b = color[2]

            brightness = r + g + b

            if brightness > (3/4) * max:
                screen.set_at((x,y), (240, 240, 120))

            elif brightness > (2/4) * max:
                screen.set_at((x,y), (240, 30, 30))

            elif brightness > (1/4) * max:
                screen.set_at((x,y), (15, 150, 15))

            else:
                screen.set_at((x,y), (15, 15, 80))

def maxRed():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))

            r = 255
            g = color[1]
            b = color[2]

            screen.set_at((x, y), (r, g, b))

def maxBlue():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))
            r = color[0]
            g = color[1]
            b = 255

            screen.set_at((x, y), (r, g, b))


def maxGreen():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))
            r = color[0]
            g = 255
            b = color[2]

            screen.set_at((x, y), (r, g, b))

def maxPurple():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))
            r = 255
            g = color[1]
            b = 255

            screen.set_at((x, y), (r, g, b))

def maxYellow():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))
            r = 255
            g = 255
            b = color[2]

            screen.set_at((x, y), (r, g, b))


def maxCyan():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))
            r = color[0]
            g = 255
            b = 255

            screen.set_at((x, y), (r, g, b))


def special():
    negate() # 360000
    brighten() # 360000
    removeRed() # 360000
    removeGreen()

def verticleStripes():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))

            if x % 2 == 0:

                r = color[0]
                g = color[1]
                b = color[2]
                screen.set_at((x, y), (r, g, b))

            else:
                screen.set_at((x, y), (0, 255, 0))



def horizontalStripes():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))

            if y % 2 == 0:

                r = color[0]
                g = color[1]
                b = color[2]
                screen.set_at((x, y), (r, g, b))

            else:
                screen.set_at((x, y), (0, 255, 0))

def mirrorXAxis():
    for y in range(300):
        for x in range(600):
            color = screen.get_at((x, y))

            r = color[0]
            g = color[1]
            b = color[2]
            screen.set_at((x, y), (r, g, b))
            screen.set_at((x, 600 - y), (r, g, b))


def mirrorYAxis():
    for x in range(300):
        for y in range(600):
            color = screen.get_at((x, y))

            r = color[0]
            g = color[1]
            b = color[2]
            screen.set_at((x, y), (r, g, b))
            screen.set_at((600 - x, y), (r, g, b))


def fadeFromTop():
    pass



def sepia():
    for x in range(600):
        for y in range(600):
            color = screen.get_at((x, y))

            r = color[0]
            g = color[1]
            b = color[2]





            final_r = .393 * r + .769 * g + .189 * b
            final_g = .349 * r + .686 * g + .168 * b
            final_b = .272 * r + .534 * g + .131 * b

            final_r = int(final_r)
            final_g = int(final_g)
            final_b = int(final_b)

            screen.set_at((x, y), (final_r, final_g, final_b))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                screen.blit(image, image.get_rect())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                screen.fill([0,255,0])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pygame.draw.circle(screen, [255, 0, 0], (300,300), 10)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                brighten()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                darken()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                removeRed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                removeGreen()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                removeBlue()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(screen, "saved.jpg")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5:
                negate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_6:
                intensify()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                grayscale()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                twoTone()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fourTone()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                maxRed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                special()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                maxBlue()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                maxGreen()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                maxPurple()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                maxYellow()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                maxCyan()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                mirrorYAxis()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                mirrorXAxis()



    pygame.display.flip()