import pygame,random
pygame.init()
WIDTH,HEIGHT = 800,800
screen = pygame.display.set_mode((800,800))
BLUE = (20,80,180)
run = True
pygame.display.set_caption("FruitCatcher")
Basket_Img = pygame.image.load("ASSETS/Basket.png")
Basket_Size = pygame.transform.scale(Basket_Img,(100,100))
Apple_Img = pygame.image.load("ASSETS/Apple.png")
Apple_Size = pygame.transform.scale(Apple_Img,(100,100))
Banana_Img = pygame.image.load("ASSETS/Banana.png")
Banana_Size = pygame.transform.scale(Banana_Img,(200,200))
Orange_Img = pygame.image.load("ASSETS/grape.png")
Orange_Size = pygame.transform.scale(Orange_Img,(200,200))



class BASKET:
    def __init__(self):
        self.basketx = 400
        self.baskety = 550
        self.speed = 1

    def draw_basket(self):
        screen.fill(BLUE)
        self.basket_rect = pygame.Rect(self.basketx - 50,self.baskety - 10,100,20)
        pygame.draw.rect(screen,(0,0,244),self.basket_rect)
        screen.blit(Basket_Size,(self.basket_rect))
    def move_basket(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_d]:
            self.basketx += self.speed
        elif self.keys[pygame.K_a]:
            self.basketx -= self.speed
    def check_collision(self):
        if self.basketx >= 800-100:
            self.basketx = 699
        if self.basketx <= 0:
            self.basketx = 1
class FRUITS:
    def __init__(self):
        self.fruits = ["Apple","Banana","Grape"]
        self.Gravity = 1
        self.randomize_fruits()
        self.fruit_rect = pygame.Rect(self.XPOS,self.YPOS + 30,100,20)

    def randomize_fruits(self):
        self.XPOS = random.randint(200,600)
        self.YPOS = 50
        self.fruit = random.choice(self.fruits)
    def random_hitbox(self):
        self.fruit_rect.x = self.XPOS
        self.fruit_rect.y = self.YPOS + 30

    def draw_fruit(self):
        pygame.draw.rect(screen,(255,0,0),self.fruit_rect)
        if self.fruit == "Apple":
            screen.blit(Apple_Size,(self.XPOS,self.YPOS))

        elif self.fruit == "Banana":
            screen.blit(Banana_Size,(self.XPOS,self.YPOS))

        elif self.fruit == "Grape":
            screen.blit(Orange_Size,(self.XPOS,self.YPOS))

    def fruit_falling(self):
        self.YPOS += self.Gravity
        self.random_hitbox()
        if self.YPOS >= 1000:
            self.randomize_fruits()
        if self.YPOS >= 800:
            pygame.quit()
        
class MAIN:
    def __init__(self):
        self.score = 0
        self.fruit = FRUITS()
        self.basket = BASKET()
    def draw_elements(self):

        self.basket.draw_basket()
        self.fruit.draw_fruit()
        self.fruit.fruit_falling()
    def move_elements(self):
        self.basket.move_basket()
        self.basket.check_collision()
    def check_collision(self):
        if self.fruit.fruit_rect.colliderect(self.basket.basket_rect):
            self.score = self.score+ 1 
            self.fruit.randomize_fruits()
    def draw_score(self):
        font = pygame.font.SysFont(None,50)
        score_text = font.render(f"Score: {self.score}",True,(255,255,255))
        screen.blit(score_text,(20,20))

main = MAIN()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    main.draw_elements()
    main.move_elements()
    main.check_collision()
    main.draw_score()
    pygame.display.flip()
pygame.quit()