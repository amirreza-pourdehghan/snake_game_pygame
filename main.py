import  consts, sys
from game_manager import GameManager
from snake import Snake
from pygame import init, QUIT, KEYDOWN
from pygame.display import set_mode
from pygame.event import get
from pygame.time import wait

def main():
    init()
    screen = set_mode((consts.height, consts.width))
    screen.fill(consts.back_color)
    game = GameManager(consts.table_size, screen, consts.sx, consts.sy, consts.block_cells)
    snakes = list()
    for snake in consts.snakes:
        print(snake)
        snakes.append(Snake(snake['keys'], game, (snake['sx'], snake['sy']), snake['color'], snake['direction']))

    while True:
        events = get()
        keys = []
        for event in events:
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                keys.append(event.unicode)

        game.handle(keys)
        wait(100)


if __name__ == '__main__':
    main()
