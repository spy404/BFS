import time

import utils
from map import cities
from solution import find

import pygame


def select_city(x, y):
    e = 5
    for city, info in cities.items():
        if info['pygame_x'] - e < x < info['pygame_x'] + e:
            if info['pygame_y'] - e < y < info['pygame_y'] + e:
                return city
    return None


def main():
    IRAN_PIC = pygame.image.load('iran.jpg')
    IRAN_PIC = pygame.transform.scale(IRAN_PIC, (utils.SCREEN_WIDTH, utils.SCREEN_HEIGH))

    pygame.init()
    screen = pygame.display.set_mode((utils.SCREEN_WIDTH, utils.SCREEN_HEIGH))
    FONT = pygame.font.Font(None, 17)

    selected_city1 = None
    selected_city2 = None
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                selected_city = select_city(x, y)
                if select_city is not None:
                    if selected_city1 is None:
                        selected_city1 = selected_city
                    else:
                        selected_city2 = selected_city
                        done = True
        screen.fill((0, 0, 0))
        screen.blit(IRAN_PIC, (0, 0))
        for city, info in cities.items():
            pygame.draw.circle(
                screen,
                (255, 0, 0),
                (info['pygame_x'], info['pygame_y']),
                3,
                0,
            )
            screen.blit(FONT.render(city, True, (0, 0, 255)), (info['pygame_x']+5, info['pygame_y']-5))
            neighbors = info['neighbors']
            for neighbor in neighbors.keys():
                pygame.draw.line(
                    screen,
                    (230, 230, 230),
                    (info['pygame_x'], info['pygame_y']),
                    (cities[neighbor]['pygame_x'], cities[neighbor]['pygame_y']),
                    1,
                )
        pygame.display.update()
        pygame.time.Clock().tick(30)


    min_estimated_distance_path = find(selected_city1, selected_city2)

    done = False
    state = 1

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((0, 0, 0))
        screen.blit(IRAN_PIC, (0, 0))
        for city, info in cities.items():
            pygame.draw.circle(
                screen,
                (255, 0, 0),
                (info['pygame_x'], info['pygame_y']),
                3,
                0,
            )
            screen.blit(FONT.render(city, True, (0, 0, 255)), (info['pygame_x']+5, info['pygame_y']-5))
            neighbors = info['neighbors'].keys()
            for neighbor in neighbors:
                pygame.draw.line(
                    screen,
                    (230, 230, 230),
                    (info['pygame_x'], info['pygame_y']),
                    (cities[neighbor]['pygame_x'], cities[neighbor]['pygame_y']),
                    1,
                )
        for i in range(len(min_estimated_distance_path)-1):
            city1 = min_estimated_distance_path[i]
            city2 = min_estimated_distance_path[i+1]
            pygame.draw.line(
                screen,
                (0, 255, 0),
                (cities[city1]['pygame_x'], cities[city1]['pygame_y']),
                (cities[city2]['pygame_x'], cities[city2]['pygame_y']),
                3,
            )
            if state == 1:
                pygame.display.update()
                pygame.time.Clock().tick(30)
                time.sleep(0.5)

        pygame.display.update()
        pygame.time.Clock().tick(30)
        state = 2


main()
