import asyncio
import pygame

# --- Constants ---
WIDTH, HEIGHT = 480, 360
FPS = 60
SQUARE_SIZE = 40
SPEED = 4
BG_COLOR = (30, 30, 30)
SQUARE_COLOR = (72, 160, 240)

async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Move the Square")
    clock = pygame.time.Clock()

    x = WIDTH // 2 - SQUARE_SIZE // 2
    y = HEIGHT // 2 - SQUARE_SIZE // 2

    running = True
    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= SPEED
        if keys[pygame.K_RIGHT]:
            x += SPEED
        if keys[pygame.K_UP]:
            y -= SPEED
        if keys[pygame.K_DOWN]:
            y += SPEED

        # Keep square inside window
        x = max(0, min(WIDTH - SQUARE_SIZE, x))
        y = max(0, min(HEIGHT - SQUARE_SIZE, y))

        # Draw
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, SQUARE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)  # Required by pygbag — yields control to the browser

    pygame.quit()

asyncio.run(main())
