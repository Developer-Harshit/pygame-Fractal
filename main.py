# Setup Project

import pygame
from random import randint, random, choice, random

import sys
from math import cos, sin, pi

print("Starting Game")

from scripts.const import WIDTH, HEIGHT, BG_COLOR, BLUE, RED


def remap(value, ti, tf, si, sf):
    result = ((value - ti) * (sf - si) / (tf - ti)) + si
    return result


class Branch:
    def __init__(self, pos, b_len, angle, a_inc, surf=None):
        self.pos = list(pos)
        self.len = b_len
        self.angle = angle + choice([-1, +1]) * random() / 5
        self.end_pos = (
            cos(self.angle) * self.len + self.pos[0],
            -sin(self.angle) * self.len + self.pos[1],
        )
        self.a_inc = a_inc
        self.child = []

        self.shape = surf
        pygame.draw.line(
            self.shape,
            (144, 150 - int(remap(self.len, 1, HEIGHT / 3, 17, 120)), 7),
            self.pos,
            self.end_pos,
            int(remap(self.len, 5, HEIGHT / 3, 1, 10)),
        )

        self.createBranch()

    def createBranch(self):
        if self.len < 5:
            return
        surf = pygame.surface.Surface((WIDTH, HEIGHT))
        surf.set_colorkey((0, 0, 0))
        surf.set_alpha(int(remap(self.len, 5, HEIGHT / 3, 50, 255)))
        self.child = [
            Branch(
                self.end_pos,
                self.len * randint(45, 60) / 100,
                self.angle + self.a_inc,
                self.a_inc,
                surf,
            ),
            Branch(
                self.end_pos,
                self.len * randint(45, 60) / 100,
                self.angle - self.a_inc,
                -self.a_inc,
                surf,
            ),
        ]
        if random() > 0.999:
            self.child.append(
                Branch(
                    self.end_pos,
                    self.len * randint(55, 60) / 100,
                    (
                        self.child[0].angle / choice([0.4, 0.6])
                        + self.child[1].angle / choice([0.4, 0.6])
                    ),
                    (self.child[0].a_inc / random() + self.child[1].a_inc / random()),
                    surf,
                )
            )

    def render(self, surf):
        if self.len < 1:
            return
        surf.blit(self.shape, (0, 0))

        for bran in self.child:
            bran.render(surf)

        pass


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Basic Screen")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.display = self.screen.copy()

        self.clock = pygame.time.Clock()
        surf = pygame.surface.Surface((WIDTH, HEIGHT))
        surf.set_colorkey((0, 0, 0))
        self.root = Branch(
            (WIDTH / 2, HEIGHT - 20),
            HEIGHT / 3,
            pi / 2,
            pi / 8,
            surf,
        )
        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False

    def run(self):
        running = True

        while running:
            # For Background ------------------------------------------------------|

            self.display.fill(BG_COLOR)
            self.root.render(self.display)
            if self.a_pressed:
                self.root.a_inc -= 0.1

            if self.d_pressed:
                self.root.a_inc += 0.1

            if self.w_pressed:
                self.root.len += 5

            if self.s_pressed:
                self.root.len -= 5

            if self.a_pressed or self.d_pressed or self.w_pressed or self.s_pressed:
                self.root.createBranch()

            # Checking Events -----------------------------------------------------|
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_a:
                        self.a_pressed = True

                    if event.key == pygame.K_d:
                        self.d_pressed = True
                    if event.key == pygame.K_w:
                        self.w_pressed = True

                    if event.key == pygame.K_s:
                        self.s_pressed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.a_pressed = False
                    if event.key == pygame.K_d:
                        self.d_pressed = False
                    if event.key == pygame.K_w:
                        self.w_pressed = False

                    if event.key == pygame.K_s:
                        self.s_pressed = False

                    pass
            # Rendering Screen ----------------------------------------------------|
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(60)

    def quit(self):
        # Quit --------------------------------------------------------------------|
        pygame.quit()
        sys.exit()
        exit()


if __name__ == "__main__":
    game = Game()
    game.run()
    game.quit()
print("Game Over")
