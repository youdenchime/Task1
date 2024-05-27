import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game settings
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])  # Random initial speed along x-axis
        self.speed_y = 2  # Initial speed along y-axis

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        # Check if the ball hits the left or right wall
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x  # Reverse the direction along x-axis
        # Check if the ball hits the top wall
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y  # Reverse the direction along y-axis

class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2  # Center the paddle horizontally
        self.y = HEIGHT - self.height - 10  # Position the paddle near the bottom

    def move(self, direction):
        # Move the paddle left or right
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10

class Game:
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)  # Default font for displaying text
        self.game_over = False

    def handle_events(self):
        # Handle events such as quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    def update(self):
        # Update the game state
        self.ball.move()  # Move the ball
        self.ball.check_collision()  # Check for collisions
        # Check if the ball hits the paddle
        if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                # Ball hits the paddle, reverse its direction and increase score
                self.ball.y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                self.ball.speed_y = -self.ball.speed_y
                self.score += 1
            else:
                # Ball misses the paddle, game over
                self.game_over = True

    def draw(self, screen):
        # Draw game objects on the screen
        screen.fill(BLACK)  # Fill the screen with black color
        # Draw the ball
        pygame.draw.circle(screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        # Draw the paddle
        pygame.draw.rect(screen, WHITE, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        # Display the score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        # Display game over message if the game is over
        if self.game_over:
            game_over_text = self.font.render(f"Your score: {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(game_over_text, game_over_rect)

def main():
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create a window
    pygame.display.set_caption("Simple Pong")  # Set the window title
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    game = Game()  # Create a game object

    # Main game loop
    while not game.game_over:
        game.handle_events()  # Handle events
        keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
        # Move the paddle based on key presses
        if keys[pygame.K_LEFT]:
            game.paddle.move("left")
        if keys[pygame.K_RIGHT]:
            game.paddle.move("right")
        game.update()  # Update the game state
        game.draw(screen)  # Draw game objects on the screen
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Cap the frame rate at 60 frames per second

    pygame.quit()  # Quit Pygame when the game is over

if __name__ == "__main__":
    main()  