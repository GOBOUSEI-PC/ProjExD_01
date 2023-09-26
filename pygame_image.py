import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    gb_img = pg.transform.flip(bg_img, True, False)
    tmr = 0

    kt_img = pg.image.load("ex01/fig/3.png")

    #動くコウカトン
    kt_moveimg = pg.transform.flip(kt_img, True, False)
    kt_aimg = pg.transform.rotozoom(kt_moveimg, 5, 1.0)
    kt_bimg = pg.transform.rotozoom(kt_moveimg, 10, 1.0)

    #さまざまなコウカトン
    koukaton = [kt_moveimg, kt_aimg, kt_bimg, kt_aimg ]

    x1 = 0
    x2 = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if x1 == -2400:
            x1 = 800
        screen.blit(bg_img,[x1,0])

        if x2 == -3200:
            x2 = 0
        screen.blit(gb_img,[x2+1600,0])

        screen.blit(koukaton[tmr%4], [300, 200])
        pg.display.update()

        x1 -= 50
        x2 -= 50
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()