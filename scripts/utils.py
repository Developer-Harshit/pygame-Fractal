import pygame


class DemoObject:
    def __init__(self, pos, o_size):
        self.pos = list(pos)
        self.size = o_size

        self.rect = pygame.surface.Surface(self.size)
        self.rect.fill((100, 20, 190))

    def render(self, surf):
        surf.blit(self.rect, self.pos)

    def transformBy(self, ratio):
        self.pos = [self.pos[0] * ratio[0], self.pos[1] * ratio[1]]
        mySize = self.rect.get_size()
        self.rect = pygame.transform.scale(
            self.rect, (mySize[0] * ratio[0], mySize[1] * ratio[1])
        )
