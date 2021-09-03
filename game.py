import pygame
import random
from pygame.image import load
from inputdata import  Player, animal, animalSmall,bird,birdSmall
from imagesound import load_sprite, get_random_position
from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.font.init()
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.mixer.music.load(f"music/music1.wav")
pygame.mixer.music.play(loops=-1)
   
shoot = pygame.mixer.Sound(f"music/shoot.wav")
move2 = pygame.mixer.Sound(f"music/music1.wav")
bomb = pygame.mixer.Sound(f"music/bomb.wav")
move1 = pygame.mixer.Sound(f"music/shoot2.wav")
hit1 = pygame.mixer.Sound(f"music/collision1.wav")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
score = 0

class Glitter(pygame.sprite.Sprite):
    def __init__(self):
        super(Glitter, self).__init__()
        self.surf = pygame.image.load(f"model/Glitter.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(500, 600),
            )
        )
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
             self.kill()

class Etn(pygame.sprite.Sprite):
    def __init__(self):
        super(Etn, self).__init__()
        self.surf = pygame.image.load(f"model/k2.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(460,520),
            )
        )
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
             self.kill()
class Ctn(pygame.sprite.Sprite):
    def __init__(self):
        super(Ctn, self).__init__()
        self.surf = pygame.image.load(f"model/d1.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                0,
                random.randint(490,520),
            )
        )
        self.speed = random.randint(3, 8)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > 1000:
             self.kill()



def display_score(score):
    font = pygame.font.SysFont('Cooper Black', 30)
    score_text = 'Score: ' + str(score)
    text_img = font.render(score_text, True, (255,0,0))
    screen.blit(text_img, [350, 150])


class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"img/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0
	def update(self):
		explosion_speed = 4
		self.counter += 1
		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()



class Shoot(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.x1=x
		
		img = pygame.image.load(f"model/spray.png")
		
		self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0
	def update(self):
		pos = self.x1+150
		self.rect.move_ip(5,0)

		if self.rect.right> pos:
			self.kill()






ADDGlitter = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGlitter,500)
ADDEtn = pygame.USEREVENT + 2
pygame.time.set_timer(ADDEtn,10000)
ADDCtn = pygame.USEREVENT + 3
pygame.time.set_timer(ADDCtn,5000)
Glitters = pygame.sprite.Group()
etns = pygame.sprite.Group()
explosions = pygame.sprite.Group()
shoots = pygame.sprite.Group()
ctns = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()



class Extinction:
    MIN_DIST=450
    global score
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load(f"model/a1.png")
        
        self.clock = pygame.time.Clock()
        self.player = Player ((400,300))
        
        self.animals=[]
        for _ in range(3):
           while True:
              position = get_random_position(self.screen)
              if (
                   position.distance_to(self.player.position)
                   > self.MIN_DIST
                 ):
                break
           self.animals.append(animal(position))
        self.animalssmall=[]
        for _ in range(0):
           while True:
              position = get_random_position(self.screen)
              if (
                   position.distance_to(self.player.position)
                   > self.MIN_DIST
                 ):
                break
           self.animalssmall.append(animalSmall(position))


        self.birds=[]
        for _ in range(2):
           while True:
              position = get_random_position(self.screen)
              if (
                   position.distance_to(self.player.position)
                   > self.MIN_DIST
                 ):
                break
           self.birds.append(bird(position))
        self.birdssmall=[]
        for _ in range(0):
           while True:
              position = get_random_position(self.screen)
              if (
                   position.distance_to(self.player.position)
                   > self.MIN_DIST
                 ):
                break
           self.birdssmall.append(birdSmall(position))


        
    def _get_game_objects(self):
        game_objects = [*self.animals, *self.animalssmall, *self.birds, *self.birdssmall]
        if self.player:
           game_objects.append(self.player)
        return game_objects


    def main_loop(self):
        i=0
        
        while True:
            
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(i,0))
            self.background = pygame.image.load(f"model/a1.png")
            width, height = pygame.display.get_surface().get_size()
            self.background = pygame.transform.scale(self.background,(width,height))
            self.screen.blit(self.background,(width+i,0))
            if ( i==-width):
                 self.screen.blit(self.background,(width+i,0))
                 i=0
            i-=1
            
     
            
            count1 = len(self.animals)
            
            if (count1 <= 1):
                for _ in range(2):
                    position = get_random_position(self.screen)
                    if (
                        position.distance_to(self.player.position)
                        > self.MIN_DIST
                        ):
                        break
                    self.animals.append(animal(position))
                    self.animalssmall.append(animalSmall(position))
            
            
            count3 = len(self.birds)
            
            if (count3 <= 1):
                for _ in range(3):
                    position = get_random_position(self.screen)
                    if (
                        position.distance_to(self.player.position)
                        > self.MIN_DIST
                        ):
                        break
                    self.birds.append(bird(position))
                    self.birdssmall.append(birdSmall(position))

            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Eshika")

    def _handle_input(self):
        global score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.display.quit()
              pygame.mixer.quit()
              exit()
            elif (self.player and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):            
              score = 0
              idea = Extinction()
              idea.main_loop()
              

            elif event.type == ADDGlitter:
              new_Glitter = Glitter()
              Glitters.add(new_Glitter)
              all_sprites.add(new_Glitter)
            elif event.type == ADDEtn:
              new_dino1 = Etn()
              etns.add(new_dino1)
              all_sprites.add(new_dino1)
            elif event.type == ADDCtn:
              new_dino2 = Ctn()
              ctns.add(new_dino2)
              all_sprites.add(new_dino2)

              
        is_key_pressed = pygame.key.get_pressed()
        
        if self.player:
           if is_key_pressed[pygame.K_UP]:
                self.player.godown()
                move1.play()
           elif is_key_pressed[pygame.K_DOWN]:
                self.player.goup()
                move1.play()
           elif is_key_pressed[pygame.K_RIGHT]:
                self.player.goright()
                move1.play()
           elif is_key_pressed[pygame.K_LEFT]:
                self.player.goleft()
                move1.play()              
           elif is_key_pressed[pygame.K_RSHIFT]:
              
              p1 = self.player.position
              a1 = int(p1[0])+ 10
              b1 = int(p1[1])
              new_shoot = Shoot(a1,b1)
              shoots.add(new_shoot)
              shoot.play()
              for animal in self.animals[:]:
                  v1= animal.position
                  if v1[0] > a1:
                     dist1 = (v1[0]-a1)
                     dist2 = abs(b1 - v1[1])
                     if (dist2 < 30 and dist1 < 200):
                         score += 5
                         self.animals.remove(animal)
                         break
              for animal1 in self.animalssmall[:]:
                  v1= animal1.position
                  if v1[0] > a1:
                     dist1 = (v1[0]-a1)
                     dist2 = abs(b1 - v1[1])
                     if (dist2 < 30 and dist1 < 200):
                         score += 5                  
                         self.animalssmall.remove(animal1)
                         break
              for bird in self.birds[:]:
                  v1= bird.position
                  if v1[0] > a1:
                     dist1 = (v1[0]-a1)
                     dist2 = abs(b1 - v1[1])
                     if (dist2 < 30 and dist1 < 200):
                         score += 5                  
                         self.birds.remove(bird)
                         break
              for bird1 in self.birdssmall[:]:
                  v1= bird1.position
                  if v1[0] > a1:
                     dist1 = (v1[0]-a1)
                     dist2 = abs(b1 - v1[1])
                     if (dist2 < 30 and dist1 < 200):
                         score += 5           
                         self.birdssmall.remove(bird1)
                         break                    
              for c1 in ctns:
                  v1= c1.rect.left
                  v2= c1.rect.top
                  if v1 > a1:
                     dist1 = (v1-a1)
                     dist2 = abs(b1 - v2)
                     if (dist2 < 60 and dist1 < 200):
                         score += 5                                     
                         c1.kill()
                         break
              for c1 in etns:
                  v1= c1.rect.left
                  v3= c1.rect.right
                  v2=c1.rect.top
                  v4=c1.rect.bottom
                  v5= (v2+v4)/2
                  if v1 > a1:
                     dist1 = (v1-a1)
                     dist2 = abs(b1 - v2)
                     dist3 = abs(b1-v5)
                     if (dist2 < 20 and dist1 < 200):
                         score += 5                                     
                         c1.kill()
                         break
                     if (dist3 < 80 and dist1 < 200):
                         score += 5                                     
                         c1.kill()
                         break
                            

             
           elif is_key_pressed[pygame.K_RCTRL]:
              
              p = self.player.position
              a = int(p[0])- 80
              b = int(p[1])- 100
              new_explosion = Explosion(a,b)
              explosions.add(new_explosion)
              bomb.play()
              for animal in self.animals[:]:
                  v = animal.position
                  if ( animal.position.distance_to((a,b))< 70 ):
                      self.animals.remove(animal)
                      score += 5
                      break
              for animal1 in self.animalssmall[:]:
                  v = animal1.position                 
                  if ( animal1.position.distance_to((a,b))< 70 ):
                      self.animalssmall.remove(animal1)
                      score += 5
                      break
              for bird in self.birds[:]:
                  v = bird.position
                  if ( bird.position.distance_to((a,b))< 70 ):
                      self.birds.remove(bird)
                      score += 5
                      break                    
              for bird1 in self.birdssmall[:]:
                  v = bird1.position                 
                  if ( bird1.position.distance_to((a,b))< 70 ):
                      self.birdssmall.remove(bird1)
                      score += 5
                      break
              for c1 in ctns:
                  v = c1.rect.left
                  v1= c1.rect.top
                  v2 = c1.rect.bottom
                  v3 = c1.rect.right                  
                  v4=a-v2
                  v5=v2-b
                  v6=v1-a
                  v7=a-v                  
                  if (v7<250 and v4<250 and v5< 150 and v6<150):
                      c1.kill()
                      score += 5
                      break              
              for c1 in etns:
                  v = c1.rect.left
                  v1= c1.rect.top
                  v2 = c1.rect.bottom
                  v3 = c1.rect.right
                  
                  v4 =abs(b-v2)  
                  v5= b- v1 
                  v6 = a-v
                  
                  if (v4<150 and v5<70 and v6< 70 ):
                      c1.kill()
                      score += 5
                      break
                  





    def _process_game_logic(self):
        global score
        for game_object in self._get_game_objects():
             game_object.move(self.screen)
        if self.player:
           for animal in self.animals[:]:
               if animal.collides_with(self.player):
                 
                 score -= 5
                 break
               
           for animal1 in self.animalssmall[:]:
               if animal1.collides_with(self.player):
                 
                 score -= 5
                 break
               
                         
        
       
    def _draw(self):
        global score
        #self.screen.blit(self.home,(600,250))
        #self.screen.blit(self.hospital,(145,415))
        for game_object in self._get_game_objects():
             game_object.draw(self.screen)
        display_score(score)
        font = pygame.font.SysFont('Cooper Black', 25)
        start_text = 'Use Arrows to move, RightShift to shoot , RightCtrl to bomb' 
        text_img = font.render(start_text, True,(231,48,36))
        self.screen.blit(text_img, [10, 1])

        font = pygame.font.SysFont('Cooper Black', 25)
        start_text = 'Score 100 to Win, -100 to Lose ' 
        text_img = font.render(start_text, True,(2,92,6))
        self.screen.blit(text_img, [300, 100])

        font = pygame.font.SysFont('Cooper Black', 20)
        start_text = 'Press SPACE ' 
        text_img = font.render(start_text, True,(2,92,6))
        self.screen.blit(text_img, [600, 300])
        
        font = pygame.font.SysFont('Cooper Black', 20)
        start_text = 'to START game ' 
        text_img = font.render(start_text, True,(2,92,6))
        self.screen.blit(text_img, [600, 315])
        
        font = pygame.font.SysFont('Ravie', 60)
        start_text = 'ExtinctZilla ' 
        text_img = font.render(start_text, True,(255,255,0))
        self.screen.blit(text_img, [110, 50])
        for entity in all_sprites:
             self.screen.blit(entity.surf, entity.rect)
        explosions.draw(self.screen)
        shoots.draw(self.screen)
        Glitters.update()
        etns.update()
        explosions.update()
        shoots.update()
        ctns.update()
        pygame.display.flip()
        self.clock.tick(40)



