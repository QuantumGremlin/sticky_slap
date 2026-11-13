import asyncio
import pygame

pygame .init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sticky Slap")
clock = pygame.time.Clock()

SKY_BLUE = (135, 206, 235)

async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SKY_BLUE)
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()
asyncio.run(main())                