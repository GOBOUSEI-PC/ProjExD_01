import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kt_img = pg.image.load("ex01/fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_newimg = pg.transform.rotozoom(kt_img, 10, 1.0)
    img = [kt_img, kt_newimg]
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(img[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1
        x += 50
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()