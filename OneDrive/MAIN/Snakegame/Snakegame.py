import pygame,random

pygame.init()
screen = pygame.display.set_mode((800,760))
clock = pygame.time.Clock()
fps = 60
cell_size = 40
light_green = (95, 166, 5)
run = True
MOVE_SNAKE = pygame.USEREVENT
class SNAKE():
    def __init__(self):
        self.body =  [pygame.math.Vector2(6,6),pygame.math.Vector2(6,7),pygame.math.Vector2(6,8)]
        self.direction = pygame.math.Vector2(1,0)

    def draw_snake(self):
        for self.Block in self.body:
            self.Block_rect = pygame.Rect(self.Block.x * cell_size,self.Block.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(55, 123, 176),self.Block_rect)
    def move_snake(self):
        self.new_head = self.body[0] + self.direction
        self.body.insert(0, self.new_head)
        self.body.pop()
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_d] and self.direction != pygame.math.Vector2(0,1):
            self.direction = pygame.math.Vector2(1,0)
        if self.key[pygame.K_a] and self.direction != pygame.math.Vector2(1,0):
            self.direction = pygame.math.Vector2(-1,0)
        if self.key[pygame.K_w] and self.direction != pygame.math.Vector2(0,1):
            self.direction = pygame.math.Vector2(0,-1)
        if self.key[pygame.K_s] and self.direction != pygame.math.Vector2(0,1):
            self.direction = pygame.math.Vector2(0,1)
        if self.Block.x > 20 or self.Block.x < 0:
            pygame.quit()
        if self.Block.y > 19 or self.Block.y < 0:
            pygame.quit()
    def grow_snake(self):
        self.new_head = self.body[0] + self.direction
        self.body.insert(0, self.new_head)
class FRUIT():
    def __init__(self):
        self.randomize()
    def randomize(self):
        self.col = random.randint(1,19)
        self.row = random.randint(1,19)
    def draw_apple(self):
        self.apple_rect = pygame.Rect(self.col * cell_size,self.row * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255,0,0),self.apple_rect)
class MAIN():
    def __init__(self):
        self.score = 0
        self.Text = pygame.font.SysFont(None,50)
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_apple()
        self.RenderedText = self.Text.render(f"SCORE:{self.score}",True,(255,255,255),None)
        screen.blit(self.RenderedText,(1,1))
    def move_elements(self):
        if self.fruit.apple_rect.colliderect(self.snake.Block_rect):
            self.fruit.randomize()
            self.snake.grow_snake()
            self.score = self.score + 1
main = MAIN()

pygame.time.set_timer(MOVE_SNAKE,100)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == MOVE_SNAKE:
            main.snake.move_snake()

    pygame.display.flip()
    screen.fill(light_green)
    main.draw_elements()
    main.move_elements()
    clock.tick(fps)
pygame.quit()