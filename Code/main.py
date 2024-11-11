import pygame
import random
import asyncio
from pygame.locals import *

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'
        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def walk(self):
        # Update body
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Initialize the mixer
        pygame.display.set_caption("SnakeRun")
        
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.high_score = 0
        
        # Load sounds
        try:
            self.background_music = pygame.mixer.Sound("resources/bg_music_1.wav")
            self.crash_sound = pygame.mixer.Sound("resources/crash.wav")
            self.background_music.set_volume(0.5)
            self.background_music.play(loops=-1)
        except Exception as e:
            print(f"Error loading sounds: {e}")
            self.background_music = None
            self.crash_sound = None

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        if hasattr(self, 'background_music') and self.background_music:
            self.background_music.play(loops=-1)

    def is_collision(self, x1, y1, x2, y2):
        return x1 >= x2 and x1 < x2 + SIZE and y1 >= y2 and y1 < y2 + SIZE

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Snake eating apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            if self.snake.length > self.high_score:
                self.high_score = self.snake.length

        # Snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                if self.crash_sound:
                    self.background_music.stop()
                    self.crash_sound.play()
                raise Exception("Collision Occurred")

        # Snake colliding with boundaries
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            if self.crash_sound:
                self.background_music.stop()
                self.crash_sound.play()
            raise Exception("Hit the boundary")

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over! Score: {self.snake.length}", True, (255, 255, 255))
        line2 = font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
        line3 = font.render("Press Enter to play again or Escape to exit", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        self.surface.blit(line2, (200, 350))
        self.surface.blit(line3, (200, 400))
        pygame.display.flip()

    async def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                        self.reset()
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True

            await asyncio.sleep(0.25)

if __name__ == '__main__':
    game = Game()
    asyncio.run(game.run())
