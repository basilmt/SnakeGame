
import curses
import random
stdscr = curses.initscr()
curses.curs_set(0)


height, width = stdscr.getmaxyx()
stdscr.keypad(True)
stdscr.timeout(100)


snk_x = width // 4
snk_y = height // 2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

food = [height//2, width//2]
stdscr.addch(food[0], food[1], curses.ACS_PI)


key = curses.KEY_RIGHT


while True:

    next_key = stdscr.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
        stdscr.keypad(False)
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]


    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)
    


    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, height - 1),
                random.randint(1, width - 1)
            ]
            food = nf if nf not in snake else None
        stdscr.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        stdscr.addch(tail[0], tail[1], ' ')

    stdscr.addch(snake[0][0], snake[0][1],"O")

                    



