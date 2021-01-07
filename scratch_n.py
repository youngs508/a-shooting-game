import pygame, random, sys, time, math, os
from pygame.locals import *
from math import *
import base64
from tkinter import *

"""icon = \
icondata = base64.b64decode(icon)

tempfile = "scratch_n.ico"
iconfile = open(tempfile,"wb")

iconfile.write(icondata)
iconfile.close()"""

"""image_path = resource_path('scratch_n.ico')    
freesansbold = resource_path('freesansbold.ttf')
player1 = resource_path('player.png')
baddie = resource_path('baddie.png')
cherry = resource_path('cherry.png')
gameover = resource_path('gameover.wav')
pickup = resource_path('pickup.wav')
bullet2 = resource_path('bullet2.png')
baddiebullet = resource_path('baddiebullet.png')
bullet3 = resource_path('bullet3.png')
bullet4 = resource_path('bullet4.png')
baddiebullet2 = resource_path('baddiebullet2.png')
baddiebullet3 = resource_path('baddiebullet3.png')
powerBaddie = resource_path('powerBaddie.png')
baddieCaptain = resource_path('baddieCaptain.png')
bluecherry = resource_path('bluecherry.png')
bullet5 = resource_path('bullet5.png')
powerBaddieBullets = resource_path('powerBaddieBullets.png')
cosmos = resource_path('cosmos.png')
sultan1 = resource_path('sultan.png')
sultanBulletImage1 = resource_path('sultanBulletImage.png')"""

class GameSet:  
    """Design of Dodger game.""" 
    def __init__(self):
                
        pygame.init()
        

        #self.resource_path(relative_path)
        self.WINDOWWIDTH = 550
        self.WINDOWHEIGHT = 600
        self.BUTTONSIZE = 200
        self.BUTTONGAPSIZE = 20

        self.GRAY = (185, 185, 185)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.RED = (255,0,0)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (155,155,0)
        self.WHITE = (255,255,255)
        self.TEXTCOLOR = self.WHITE
        self.TEXTSHADOWCOLOR = self.GRAY
        self.XMARGIN = int((self.WINDOWWIDTH - (2*self.BUTTONSIZE) - self.BUTTONGAPSIZE)/2)
        self.YMARGIN = int((self.WINDOWHEIGHT - (2*self.BUTTONSIZE) - self.BUTTONGAPSIZE)/2)
        self.FPS = 60
        self.BADDIEMINSIZE = 40
        self.BADDIEMAXSIZE = 80
        self.CHERRYMINSIZE = 20
        self.CHERRYMAXSIZE = 40
        self.BADDIEMINSPEED = 1
        self.BADDIEMAXSPEED = 2
        self.CHERRYMINSPEED = 1
        self.CHERRYMAXSPEED = 2
        self.ADDNEWBADDIERATE = 6
        self.ADDNEWMIXRATE = 2
        self.ADDNEWBULLETRATE = 20
        self.ADDNEWCHERRYRATE = 10
        self.PLAYERMOVERATE = 5
        self.BULLETMINMOVERATE = 4
        self.BULLETMAXMOVERATE = 8
        self.BULLETMINMOVERATE_ = 1
        self.BULLETMAXMOVERATE_ = 2
        self.BULLETWIDTH = 1
        self.BULLETHEIGHT = 4
        self.CHERRYMOVERATE = 30
        self.ADDBADDIEBULLETRATE = 200
        self.ADDMIXBULLETRATE = 200

        self.MOVESPEED = 4
        self.YELLOWRECT = pygame.Rect(self.XMARGIN,self.YMARGIN+self.BUTTONSIZE+self.BUTTONGAPSIZE,self.BUTTONSIZE,self.BUTTONSIZE)
        self.GREENRECT = pygame.Rect(self.XMARGIN+self.BUTTONSIZE+self.BUTTONGAPSIZE,self.YMARGIN+self.BUTTONSIZE+self.BUTTONGAPSIZE,self.BUTTONSIZE,self.BUTTONSIZE)

        # set up pygame, the window, and the mouse cursor
        relative_path = ["freesansbold.ttf", "freesansbold.ttf", "baddie.png", "powerBaddie.png", "baddieCaptain.png", "sultan.png", "bullet2.png",
        "bullet3.png", "bullet4.png", "baddiebullet.png", "baddiebullet2.png", "baddiebullet3.png", "bullet5.png", "powerBaddieBullets.png", 
        "sultanBulletImage.png", "cherry.png", "bluecherry.png", "cosmos.png", "gameover.wav", "pickup.wav", "Firework.mid"]
        root = Tk()
        for r in relative_path:
            path = self.resource_path(r)
            root.iconbitmap(path)
        
        self.FPSCLOCK = pygame.time.Clock()
        self.WINDOWSURFACE = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT), FULLSCREEN)
        self.BASICFONT = pygame.font.Font(None, 18)
        self.BIGFONT = pygame.font.Font(None, 100)
        pygame.display.set_caption('Dodger')
        pygame.mouse.set_visible(False)
        
        self.font = pygame.font.SysFont(None, 48)
        
        datafile = "scratch_n.ico"
        if not hasattr(sys, "frozen"):
            datafile = os.path.join(os.path.dirname(__file__), datafile) 
        else:  
            datafile = os.path.join(sys.prefix, datafile)
        
        root.iconbitmap(default=datafile)

        self.nums=0
        self.num2=0
        self.baddies = []
        self.powerBaddies = [] 
        self.baddieCaptains = [] 
        self.sultans = []
        self.bullets = []
        self.baddieBullets = []
        self.pbaddieBullets = []
        self.baddieCaptainBullets = []
        self.sultanBullets = []  
        self.cherries = [] 
        
        self.t = 0
        self.ds = 0 
        self.dr = 0
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.reverseCheat = False
        self.slowCheat = False
        self.baddieAddCounter = 0
        self.powerBaddieAddCounter = 0
        self.baddieCaptainAddCounter = 0
        self.sultanAddCounter = 0
        self.bulletAddCounter = 0
        self.bulletAddCounter1 = 0
        self.bulletAddCounter2 = 0
        self.bulletAddCounter3 = 0
        self.baddiecBulletAddCounter = 0
        self.mixAddCounter = 0
        self.cherryAddCounter = 0
        self.bcherryAddCounter = 0
        self.baddieBulletAddCounter = 0
        self.pbaddieBulletAddCounter = 0
        self.sultanBulletAddCounter = 0
        self.angle = 0
        self.sultan_angle = 60
        self.length = 2
        self.sultan_length = 2
        self.shotAngleRate = 0.02
        self.shotSpeed = 0.005
        self.healthbar = 20
        self.su_healthbar = 20
        self.level = 1 
        self.score = 0
        self.TOPSCORE = [0] * 3
        self.musicPlaying = True

        # set up images
        self.playerImage = pygame.image.load('player.png')
        self.playerStretchedImage = pygame.transform.scale(self.playerImage, (40, 40))
        self.player = self.playerStretchedImage.get_rect()
        self.baddieImage = pygame.image.load('baddie.png')
        self.powerBaddieImage = pygame.image.load('powerBaddie.png')
        self.baddieCaptainImage = pygame.image.load('baddieCaptain.png')
        self.sultanImage = pygame.image.load('sultan.png') 
        self.sultanStretchedImage = pygame.transform.scale(self.sultanImage, (40, 40))
        self.bulletImage = pygame.image.load('bullet2.png')
        self.bulletUpgradeImage = pygame.image.load('bullet3.png')
        self.bulletUpgradeImage2 = pygame.image.load('bullet4.png')
        self.baddieBulletImage = pygame.image.load('baddiebullet.png')
        self.baddieBulletUpgradeImage = pygame.image.load('baddiebullet2.png')
        self.baddieBulletUpgradeImage2 = pygame.image.load('baddiebullet3.png')
        self.baddieBulletUpgradeImage3 = pygame.image.load('bullet5.png')
        self.baddieBulletUpgradeImage4 = pygame.image.load('powerBaddieBullets.png')
        self.sultanBulletImage = pygame.image.load('sultanBulletImage.png')
        self.cherryImage = pygame.image.load('cherry.png')
        self.bcherryImage = pygame.image.load('bluecherry.png')
        self.backgroundImage = pygame.image.load('cosmos.png').convert()
        self.backgroundRect = self.backgroundImage.get_rect()
        self.backStretchedImage = pygame.transform.scale(self.backgroundImage, (600, 600))

        self.font = pygame.font.SysFont(None, 48)

        # set up sounds
        self.pickUpSound = pygame.mixer.Sound('pickup.wav')
        self.gameOverSound = pygame.mixer.Sound('gameover.wav')
        pygame.mixer.music.load('firework.mid')
        #musicPlaying = True

        # show the "Start" screen
        self.drawText('Dodger', self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3), (self.WINDOWHEIGHT / 3))
        self.drawText('Press a key to start.', self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3) - 30, (self.WINDOWHEIGHT / 3) + 50)
        
        pygame.display.update()

    def set_baddies(self):
        """Set baddie lists."""
        self.baddies.append([])
        self.powerBaddies.append([]) 
        self.baddieCaptains.append([]) 
        self.sultans.append([])
        self.bullets.append([])
        self.baddieBullets.append([])
        self.pbaddieBullets.append([])
        self.baddieCaptainBullets.append([])
        self.sultanBullets.append([])  

    def clear_baddies(self):
        """Clear all of the baddies on the screen."""
        level = self.get()
        self.baddies[level-1].clear()
        self.powerBaddies[level-1].clear() 
        self.baddieCaptains[level-1].clear() 
        self.sultans[level-1].clear()
        self.bullets[level-1].clear()
        self.baddieBullets[level-1].clear()
        self.pbaddieBullets[level-1].clear()
        self.baddieCaptainBullets[level-1].clear()
        self.sultanBullets[level-1].clear()  
        self.cherries.clear()

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def main(self):
        """Main game loop"""
        
        self.waitForPlayerToPressKey()
        
        while True:
            pygame.mixer.music.play(-1, 0.0)
            
            self.player.topleft = (self.WINDOWWIDTH / 2, self.WINDOWHEIGHT - 50)
            score, level = self.runGame()
            # Stop the game and show the "Game Over" screen.
            pygame.mixer.music.stop()
            self.gameOverSound.play()
        
            if level == 3 and score >= 1000:
                self.drawText("Congratulation! You win.", self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3), (self.WINDOWHEIGHT / 3))
                pygame.display.update()
                self.waitForPlayerToPressKey()
            else:
                self.drawText('GAME OVER', self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3), (self.WINDOWHEIGHT / 3))
                pygame.display.update()
                self.waitForPlayerToPressKey()

            self.drawText('Press a key to play again.', self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3) - 80, (self.WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            self.waitForPlayerToPressKey()

            self.gameOverSound.stop()

    def runGame(self):
        # set up the start of the game
        
        lastFallTime = time.time()
        lastMoveDownTime = time.time()
        lastMoveSidewaysTime = time.time()
        flag = False
        turn = 3
        fl = 0

        while True: # the game loop runs while the game part is playing 

            # Draw the game world on the window.
            self.WINDOWSURFACE.blit(self.backStretchedImage, self.backgroundRect)

            if fl == 0:
                self.set_baddies()
                level = self.get()
                self.drawText(f"Level {level}", self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3), (self.WINDOWHEIGHT / 3))
                pygame.display.update()
                self.waitForPlayerToPressKey()
                fl = 1

            # Draw the score and top score.
            self.drawText('Score: %s' % (self.score), self.font, self.WINDOWSURFACE, 10, 0)
            self.drawText('Top Score: %s' % (self.TOPSCORE[level-1]), self.font, self.WINDOWSURFACE, 10, 40)
            
            if self.score < 200 or self.score > 400 and self.score < 500:
                # Add baddies
                self.baddie_generation()
                # Add baddie bullets
                self.baddie_bullet_generation()

            # baddies move
            self.baddie_move()

            # baddie bullets move
            self.baddie_bullet_move()
            

            if 400 >= self.score >= 75:
                # Add powerBaddies
                self.powerBaddie_generation()
                # Add powerbaddie bullets
                self.powerBaddie_bullet_generation()

            # powerbaddies move
            self.powerBaddie_move()

            # powerbaddie bullets move
            self.powerBaddie_bullet_move()
            

            if 500 > self.score >= 190:  
                # Add baddieCaptains  
                self.baddieCaptain_generation()
                # Add baddiecaptain bullets
                self.baddieCaptain_bullet_generation_1()
            elif 1000 > self.score >= 500:
                # Add baddieCaptains  
                self.baddieCaptain_generation()
                # Add baddiecaptain bullets
                self.baddieCaptain_bullet_generation_2()
            
            # baddiecaptains move
            self.baddieCaptain_move() 

            # baddiecaptain bullets move
            self.baddieCaptain_bullet_move()


            if 800 > self.score >= 500:
                # Add sultan
                self.sultan_generation()
                # Add sultan bullets
                self.sultan_bullet_generation_1()
            elif 1000 > self.score >= 800:
                # Add sultan
                self.sultan_generation()
                # Add sultan bullets
                self.sultan_bullet_generation_2()

            # sultans move
            self.sultan_move()    

            # sultan bullets move
            self.sultan_bullet_move()


            # Add player's bullets
            self.player_bullet_generation(flag)
            
            # player bullets move
            self.player_bullet_move()         

            # Add cherries
            self.cherry_generation()

            # cherries move
            self.cherry_move()

            # Add bluecherries
            self.bluecherry_generation()

            # blue cherries move
            self.bluecherry_move()


            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()

                if event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flag=True                       
                    if event.key == K_LEFT or event.key == ord('a'):
                        self.moveRight = False
                        self.moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        self.moveLeft = False
                        self.moveRight = True
                    if event.key == K_UP or event.key == ord('w'):
                        self.moveDown = False
                        self.moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):
                        self.moveUp = False
                        self.moveDown = True

                if event.type == KEYUP:
                    if event.key == pygame.K_SPACE:
                        flag = False
                        
                    
                    if (event.key == K_p):
                        pygame.mixer.music.stop()
                        self.showTextScreen('Paused')
                        pygame.mixer.music.play(-1, 0.0)
                        lastFallTime = time.time()
                        lastMoveDownTime = time.time()
                        lastMoveSidewaysTime = time.time()
                        
                    if event.key == K_ESCAPE:
                        self.terminate()

                    if event.key == K_LEFT or event.key == ord('a'):
                        self.moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        self.moveRight = False
                    if event.key == K_UP or event.key == ord('w'):
                        self.moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        self.moveDown = False

                if event.type == MOUSEMOTION:
                    # If the mouse moves, move the player where the cursor is.
                    self.player.move_ip(event.pos[0] - self.player.centerx, event.pos[1] - self.player.centery)
        
            # Move the player around.
            if self.moveLeft and self.player.left > 0:
                self.player.move_ip(-1 * self.PLAYERMOVERATE, 0)
            if self.moveRight and self.player.right < self.WINDOWWIDTH:
                self.player.move_ip(self.PLAYERMOVERATE, 0)
            if self.moveUp and self.player.top > 0:
                self.player.move_ip(0, -1 * self.PLAYERMOVERATE)
            if self.moveDown and self.player.bottom < self.WINDOWHEIGHT:
                self.player.move_ip(0, self.PLAYERMOVERATE)

            # Move the mouse cursor to match the player.
            if self.isOnBoard(self.player):
                pygame.mouse.set_pos(self.player.centerx, self.player.centery)

            if self.healthbar > 50:
                self.healthbar = 50

            # Check if any of the cherries have hit the player
            for ch in self.cherries:
                if self.player.colliderect(ch['rect']) and ch['sig'] == 1:
                    self.healthbar += 3                
                    self.nums = 0
                    self.score += 2
                    self.cherries.remove(ch)
                    if self.musicPlaying:
                        self.pickUpSound.play()
                    break     
            
                elif self.player.colliderect(ch['rect']) and ch['sig'] == 2:           
                    self.healthbar += 6                                
                    self.nums = 2
                    self.score += 4
                    self.cherries.remove(ch)
                    if self.musicPlaying:
                        self.pickUpSound.play()
                    break

            
        
            

            # Draw the player's rectangle and healthbar
            if self.healthbar > 20:
                player_health_color = self.GREEN
            elif self.healthbar > 10:
                player_health_color = self.YELLOW
            else:
                player_health_color = self.RED

            for pb in self.powerBaddies[level-1]:
                if pb['healthbar'] > 10:
                    pb_health_color = self.GREEN
                elif pb['healthbar'] > 5:
                    pb_health_color = self.YELLOW
                else:
                    pb_health_color = self.RED

            for bc in self.baddieCaptains[level-1]:
                if bc['healthbar'] > 10:
                    bc_health_color = self.GREEN
                elif bc['healthbar'] > 5:
                    bc_health_color = self.YELLOW
                else:
                    bc_health_color = self.RED

            for su in self.sultans[level-1]:
                if su['healthbar'] > 10:
                    su_health_color = self.GREEN
                elif su['healthbar'] > 5:
                    su_health_color = self.YELLOW
                else:
                    su_health_color = self.RED

            if self.isOnBoard(self.player): 
                self.WINDOWSURFACE.blit(self.playerStretchedImage, self.player)
                if self.player.left + self.healthbar < self.WINDOWWIDTH:
                    pygame.draw.rect(self.WINDOWSURFACE,player_health_color, (self.player.left, self.player.bottom+10, self.healthbar, 10))
                elif self.player.left + self.healthbar >= self.WINDOWWIDTH:
                    pygame.draw.rect(self.WINDOWSURFACE,player_health_color, (self.player.left, self.player.bottom+10, self.WINDOWWIDTH - self.player.left, 10))
            


            for pb in self.powerBaddies[level-1]:
                pygame.draw.rect(self.WINDOWSURFACE,pb_health_color, (pb['rect'].left, pb['rect'].bottom+10, pb['healthbar'], 10))

            for bc in self.baddieCaptains[level-1]:
                pygame.draw.rect(self.WINDOWSURFACE,bc_health_color, (bc['rect'].left, bc['rect'].bottom+10, bc['healthbar'], 10))

            for su in self.sultans[level-1]:
                pygame.draw.rect(self.WINDOWSURFACE,su_health_color, (su['rect'].left, su['rect'].bottom+10, su['healthbar'], 10))
                
            # Check if any of the baddieBullets have hit the player
            for ba in self.baddieBullets[level-1]:
                
                if self.player.colliderect(ba['line']):
                    self.healthbar -= 2
                    self.score -= 1
                    self.baddieBullets[level-1].remove(ba)
                    
            # Check if any of the pbaddieBullets have hit the player
            for pbb in self.pbaddieBullets[level-1]:
                
                if self.player.colliderect(pbb['line']):
                    self.healthbar -= 4
                    self.score -= 2
                    self.pbaddieBullets[level-1].remove(pbb)           
                       
            # Check if any of the baddieCaptainBullets have hit the player
            for bcb in self.baddieCaptainBullets[level-1]:
                
                if self.player.colliderect(bcb['line']):
                    self.healthbar -= 6
                    self.score -= 5
                    self.baddieCaptainBullets[level-1].remove(bcb)

            # Check if any of the sultanBullets have hit the player
            for sub in self.sultanBullets[level-1]:
                
                if self.player.colliderect(sub['line']):
                    self.healthbar -= 8
                    self.score -= 8
                    self.sultanBullets[level-1].remove(sub)  
                
      
            # remove baddies by colliding bullets
        
            for b in self.baddies[level-1]:
                for bu in self.bullets[level-1]:
                    if bu['line'].colliderect(b['rect']):
                        self.baddies[level-1].remove(b)
                        self.bullets[level-1].remove(bu)
                        self.score += 1 # increase score
                        break

            # remove powerBaddies by colliding bullets
        
            for pb in self.powerBaddies[level-1]:
                for bu in self.bullets[level-1]:
                    if bu['line'].colliderect(pb['rect']):
                        pb['healthbar'] -= 10
                        self.bullets[level-1].remove(bu)
                        if pb['healthbar'] == 0:
                            self.powerBaddies[level-1].remove(pb)
                            self.score += 5 # increase score
                            break
 

            # remove a baddieCaptain by colliding bullets
            
            for bc in self.baddieCaptains[level-1]:
                for bu in self.bullets[level-1]:
                    if bu['line'].colliderect(bc['rect']):
                        bc['healthbar'] -= 5
                        self.bullets[level-1].remove(bu)
                        if bc['healthbar'] == 0:
                            self.baddieCaptains[level-1].remove(bc)
                            self.score += 10 #increase score
                            break
                    
                        
            # remove a sultan by colliding bullets   
            for su in self.sultans[level-1]:
                for bu in self.bullets[level-1]:
                    if bu['line'].colliderect(su['rect']):
                        su['healthbar'] -= 3
                        self.bullets[level-1].remove(bu)
                        if su['healthbar'] == 0:
                            self.sultans[level-1].remove(su)
                            self.score += 15 #increase score
                            break         
                    
               
                    
            if self.score >= 25 and self.score < 75:
                for bu in self.bullets[level-1]:
                    bu['surface'] = pygame.transform.scale(self.bulletUpgradeImage,(self.BULLETWIDTH * 20, self.BULLETHEIGHT * 10))
                for ba in self.baddieBullets[level-1]:
                    ba['surface'] = pygame.transform.scale(self.baddieBulletUpgradeImage,(self.BULLETWIDTH * 20, self.BULLETHEIGHT * 10))

            elif self.score >= 75 and self.score < 1000:
                for bu in self.bullets[level-1]:
                    bu['surface'] = pygame.transform.scale(self.bulletUpgradeImage2,(self.BULLETWIDTH * 30, self.BULLETHEIGHT * 15))
                for ba in self.baddieBullets[level-1]:
                    ba['surface'] = pygame.transform.scale(self.baddieBulletUpgradeImage2,(self.BULLETWIDTH * 30, self.BULLETHEIGHT * 15))
    

            #if self.isOnBoard(player):
                #self.WINDOWSURFACE.blit(self.playerStretchedImage, player)
                #pygame.draw.rect(self.WINDOWSURFACE,player_health_color, (player.left, player.bottom+10, healthbar, 10))

            #self.ma_draw([player])
            self.mab_draw(self.bullets[level-1])

            # Delete baddies that have fallen past the bottom.
            self.del_life(self.baddies[level-1])
            self.del_life(self.powerBaddies[level-1])
            self.del_life(self.baddieCaptains[level-1])
            self.del_life(self.sultans[level-1])
            
            # Delete baddie bullets that have fallen past the bottom.
            self.del_bullet(self.baddieBullets[level-1])
            
            # Delete powerBaddie bullets that have fallen past the bottom.
            self.del_bullet(self.pbaddieBullets[level-1])

            # Delete baddieCaptain bullets that have gone to the top.
            self.del_bullet(self.baddieCaptainBullets[level-1])

            # Delete sultan bullets that have fallen past the bottom.
            self.del_bullet(self.sultanBullets[level-1])
            
            # Delete cherries that have fallen past the bottom.
            self.del_lifes(self.cherries)

            # Delete bullets that have gone up above and each side of the window.
            self.del_bullet(self.bullets[level-1])
            
            # Draw each cherry
            self.ma_draw(self.cherries)
            
            # Draw each baddie
            self.ma_draw(self.baddies[level-1])
            
            # Draw each powerBaddies
            self.ma_draw(self.powerBaddies[level-1])
            

            # Draw baddieCaptains
            self.ma_draw(self.baddieCaptains[level-1]) 
            
            # Draw sultans
            self.ma_draw(self.sultans[level-1])
        
            # Draw each baddie bullet
            self.mab_draw(self.baddieBullets[level-1])
            
            # Draw each powerbaddie bullet
            self.mab_draw(self.pbaddieBullets[level-1])

            # Draw each baddieCaptain bullet
            self.mab_draw(self.baddieCaptainBullets[level-1])

            # Draw each sultan baddie bullet
            self.mab_draw(self.sultanBullets[level-1])
            
            pygame.display.update()

            # Check if any of the baddies have hit the player.
            for b in self.baddies[level-1]:
                if self.player.colliderect(b['rect']):
                    self.baddies[level-1].remove(b)
                    self.healthbar -= 5

            for pb in self.powerBaddies[level-1]:
                if self.player.colliderect(pb['rect']):
                    self.powerBaddies[level-1].remove(pb)
                    self.healthbar -= 8

            for bc in self.baddieCaptains[level-1]:
                if self.player.colliderect(bc['rect']):
                    self.baddieCaptains[level-1].remove(bc)
                    self.healthbar -= 10
                        
            for su in self.sultans[level-1]:
                if self.player.colliderect(su['rect']):
                    su['healthbar'] -= 2
                    self.healthbar -= 12
                    for i in range(2):
                        self.player.move_ip(self.PLAYERMOVERATE*4, 0)
                        self.player.move_ip(-self.PLAYERMOVERATE*4, 0)
            
            
            # Game termination
            #level = self.get()
            if self.score >= 1000:
                self.clear_baddies()
                if self.level < 3:
                    self.level += 1 
                    turn = 3
                    fl = 0
                    self.score = 0
                    self.player.topleft = (self.WINDOWWIDTH / 2, self.WINDOWHEIGHT - 50)
                else:
                    break
            
            elif self.score < 0 or self.healthbar <= 0:
                turn -= 1
                if turn == 0:
                    if self.score > self.TOPSCORE[level-1]:
                        self.TOPSCORE[level-1] = self.score
                    self.score = 0
                    self.clear_baddies()
                    turn = 3
                self.player.topleft = (self.WINDOWWIDTH / 2, self.WINDOWHEIGHT - 50)
                self.healthbar = 20
                self.nums = 0
                if turn < 3:
                    self.drawText(f'{turn} more players left.', self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3), (self.WINDOWHEIGHT / 3))
                    pygame.display.update()
                    self.waitForPlayerToPressKey()
                self.drawText('Press any key to continue.', self.font, self.WINDOWSURFACE, (self.WINDOWWIDTH / 3) - 80, (self.WINDOWHEIGHT / 3) + 50)
                pygame.display.update()
                self.waitForPlayerToPressKey()

            self.FPSCLOCK.tick(self.FPS)

        return self.score, self.level 

    def get(self):
        return self.level

    def baddie_generation(self):
        level = self.get()
        if level == 1:
            con_num = 10
        elif level == 2:
            con_num = 8
        elif level == 3:
            con_num = 6

        self.baddieAddCounter += 1
            
        if self.baddieAddCounter == self.ADDNEWBADDIERATE * con_num:
            self.baddieAddCounter = 0
            self.baddieSize = random.randint(self.BADDIEMINSIZE, self.BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, self.WINDOWWIDTH-self.baddieSize), 0 - self.baddieSize, self.baddieSize, self.baddieSize),
                        'speed': random.randint(self.BADDIEMINSPEED, self.BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(self.baddieImage, (self.baddieSize, self.baddieSize)),
                        }
            
            self.baddies[level-1].append(newBaddie)
            

        #return baddies

    def baddie_move(self):
        level = self.get()
        # Move the baddies down.
        for b in self.baddies[level-1]:
            b['rect'].move_ip(0, b['speed'])
        

        #return baddies

    def powerBaddie_generation(self):
        level = self.get()
        # Add power baddies
        if level == 1:
            con_num = 10
        elif level == 2:
            con_num = 8
        elif level == 3:
            con_num = 6
        
        self.powerBaddieAddCounter += 1
        
        if self.powerBaddieAddCounter == self.ADDNEWBADDIERATE * con_num:
            self.powerBaddieAddCounter = 0
            pbaddieSize = random.randint(self.BADDIEMINSIZE, self.BADDIEMAXSIZE)
            newPowerBaddie = {'rect': pygame.Rect(random.randint(0, self.WINDOWWIDTH-pbaddieSize), 0 - pbaddieSize-20, pbaddieSize, pbaddieSize),
                            'speed': random.randint(self.BADDIEMINSPEED-1, self.BADDIEMAXSPEED-1),
                            'surface': pygame.transform.scale(self.powerBaddieImage, (pbaddieSize, pbaddieSize)),
                            'healthbar': 20,
                            }

            
            self.powerBaddies[level-1].append(newPowerBaddie)
            

        #return powerBaddies

    def powerBaddie_move(self):
        level = self.get()
        # Move the powerBaddies down.
        for pb in self.powerBaddies[level-1]:
            
            if pb['rect'].left < self.player.left and pb['rect'].top < self.player.top: 
                pb['rect'].move_ip(pb['speed'], pb['speed'])
            elif pb['rect'].left > self.player.left and pb['rect'].top < self.player.top:
                pb['rect'].move_ip(-pb['speed'], pb['speed'])
            elif pb['rect'].left == self.player.left and pb['rect'].top < self.player.top:
                pb['rect'].move_ip(0, pb['speed'])        
            elif pb['rect'].top >= self.player.top and pb['rect'].left < self.player.left:
                pb['rect'].move_ip(pb['speed'], -pb['speed'])
            elif pb['rect'].top >= self.player.top and pb['rect'].left >= self.player.left:
                pb['rect'].move_ip(-pb['speed'], -pb['speed'])

        

        

    def baddieCaptain_generation(self):
        level = self.get()
        # Add baddieCaptains  
        if level == 1:
            con_num = 10
        elif level == 2:
            con_num = 8
        elif level == 3:
            con_num = 6

        self.baddieCaptainAddCounter += 1
        
        if self.baddieCaptainAddCounter == self.ADDNEWBADDIERATE * con_num:
            self.baddieCaptainAddCounter = 0
            baddieCaptainSize = random.randint(self.BADDIEMINSIZE * 2, self.BADDIEMAXSIZE * 2)
            newBaddieCaptain = {'rect': pygame.Rect(random.randint(0, self.WINDOWWIDTH-baddieCaptainSize), 0 - baddieCaptainSize-20, baddieCaptainSize, baddieCaptainSize),
                              'speed': random.randint(self.BADDIEMINSPEED-1, self.BADDIEMAXSPEED-1),
                              'surface': pygame.transform.scale(self.baddieCaptainImage, (baddieCaptainSize, baddieCaptainSize)),
                              'healthbar': 15,
                              }

            
            self.baddieCaptains[level-1].append(newBaddieCaptain)
            
        
        #return baddieCaptains  

    def baddieCaptain_move(self):
        level = self.get()
        # Move the baddieCaptain down.
        for bc in self.baddieCaptains[level-1]:
            if bc['rect'].left < self.player.left: 
                bc['rect'].move_ip(bc['speed'], bc['speed'])
            elif bc['rect'].left > self.player.left: 
                bc['rect'].move_ip(-bc['speed'], bc['speed'])
            elif bc['rect'].left == self.player.left: 
                bc['rect'].move_ip(0, bc['speed'])

    def sultan_generation(self):
        level = self.get()
        # Add a sultan
        if level == 1:
            con_num = 10
        elif level == 2:
            con_num = 8
        elif level == 3:
            con_num = 6

        self.sultanAddCounter += 1
        
        if self.sultanAddCounter == self.ADDNEWBADDIERATE * con_num:
            self.sultanAddCounter = 0
            
            newSultan = {'rect':pygame.Rect(random.randint(0, self.WINDOWWIDTH-self.BADDIEMAXSIZE), 0 - self.BADDIEMAXSIZE-20, self.BADDIEMAXSIZE, self.BADDIEMAXSIZE),
                         'speed': 1,
                         'surface': pygame.transform.scale(self.sultanStretchedImage, (self.BADDIEMAXSIZE, self.BADDIEMAXSIZE)),
                         'healthbar': 15,
                        }
            
            
            self.sultans[level-1].append(newSultan)
            

    def sultan_move(self):
        level = self.get()
        # move the sultan data structure
        for su in self.sultans[level-1]:
            if su['rect'].left < self.player.left and su['rect'].top < self.player.top: 
                su['rect'].move_ip(su['speed'], su['speed'])
            elif su['rect'].left > self.player.left and su['rect'].top < self.player.top: 
                su['rect'].move_ip(-su['speed'], su['speed'])
            elif su['rect'].left == self.player.left and su['rect'].top < self.player.top: 
                su['rect'].move_ip(0, su['speed'])
            elif su['rect'].left > self.player.left and su['rect'].top >= self.player.top:
                su['rect'].move_ip(-su['speed'], -su['speed'])
            elif su['rect'].left <= self.player.left and su['rect'].top >= self.player.top: 
                su['rect'].move_ip(su['speed'], -su['speed'])

    def cherry_generation(self):
        # Add cherries
        if not self.reverseCheat and not self.slowCheat:
            self.cherryAddCounter += 1

        if self.cherryAddCounter == self.ADDNEWCHERRYRATE * 5:
            self.cherryAddCounter = 0
            cherrySize = random.randint(self.CHERRYMINSIZE, self.CHERRYMAXSIZE)
            newCherry = {'rect': pygame.Rect(random.randint(0, self.WINDOWWIDTH-cherrySize), 0 - cherrySize, cherrySize, cherrySize),
                         'speed': random.randint(self.CHERRYMINSPEED, self.CHERRYMAXSPEED),
                         'surface': pygame.transform.scale(self.cherryImage, (cherrySize, cherrySize)),
                         'sig': 1,
                         }

            self.cherries.append(newCherry)


    def cherry_move(self):
        # Move the cherries down
        for ch in self.cherries:   
            ch['rect'].move_ip(0, ch['speed'])

        #return cherries

    def bluecherry_generation(self):
        # Add bluecherries
        if not self.reverseCheat and not self.slowCheat:
            self.bcherryAddCounter += 1

        if self.bcherryAddCounter == self.ADDNEWCHERRYRATE * 5:
            self.bcherryAddCounter = 0
            bcherrySize = random.randint(self.CHERRYMINSIZE, self.CHERRYMAXSIZE)
            newbCherry = {'rect': pygame.Rect(random.randint(0, self.WINDOWWIDTH-bcherrySize), 0 - bcherrySize, bcherrySize, bcherrySize),
                         'speed': random.randint(self.CHERRYMINSPEED, self.CHERRYMAXSPEED),
                         'surface': pygame.transform.scale(self.bcherryImage, (bcherrySize, bcherrySize)),
                         'sig': 2,
                         }

            self.cherries.append(newbCherry)

        #return cherries

    def bluecherry_move(self):
        # Move the cherries down
        for bch in self.cherries:   
            bch['rect'].move_ip(0, bch['speed'])

        #return cherries

    def player_bullet_generation(self, flag):
        level = self.get()
        """Make player bullets."""       
        self.bulletAddCounter += 10
                
        if self.bulletAddCounter == self.ADDNEWBULLETRATE:
            self.bulletAddCounter = 0
            self.angle += 5
            self.angle %= 360
            self.length += 0.2
            self.length %= 12
            if self.length < 2:
                self.length += 2
            if flag == True:
                newBullet = {'line': pygame.Rect(self.player.centerx, self.player.bottom, self.BULLETWIDTH, self.BULLETHEIGHT),
                            'speed': self.BULLETMAXMOVERATE,
                            'speedx': self.length*cos(radians(self.angle)),
                            'speedy': self.length*sin(radians(self.angle)),
                            'surface':pygame.transform.scale(self.bulletImage, (self.BULLETWIDTH * 10, self.BULLETHEIGHT * 10)),
                            }
                if self.nums == 0:
                    newBullet['tag'] = 1
                elif self.nums == 2:
                    newBullet['tag'] = 2 
                self.bullets[level-1].append(newBullet)

        #return bullets

    def player_bullet_move(self):
        level = self.get()
        # Move player's bullets up and right and left sides            
        #while True:
        for bu in self.bullets[level-1]:
            if bu['tag'] == 1:
                bu['line'].move_ip(0, -bu['speed'])

            elif bu['tag'] == 2:
                bu['line'].move_ip(bu['speedx'], -bu['speedy'])
                
            #break 

        #return bullets

    def baddie_bullet_generation(self):
        level = self.get()
        """Make baddies bullets."""   
        self.baddieBulletAddCounter += 5

        if self.baddieBulletAddCounter == self.ADDBADDIEBULLETRATE:
            self.baddieBulletAddCounter = 0
            for b in self.baddies[level-1]:
                if b['rect'].top >= 0:
                    newBaddieBullet = {'line': pygame.Rect(b['rect'].centerx, b['rect'].top, self.BULLETWIDTH, self.BULLETHEIGHT),
                                      'speed': random.randint(self.BULLETMINMOVERATE, self.BULLETMAXMOVERATE),
                                      'surface':pygame.transform.scale(self.baddieBulletImage, (self.BULLETWIDTH * 3, self.BULLETHEIGHT * 10)),
                                      }

                    self.baddieBullets[level-1].append(newBaddieBullet)

        #return baddieBullets

    def baddie_bullet_move(self):
        level = self.get()
        # Move baddie bullets down    
        for ba in self.baddieBullets[level-1]:
            ba['line'].move_ip(0, ba['speed'])

        #return baddieBullets

    def powerBaddie_bullet_generation(self):
        level = self.get()
        """Make baddies bullets."""   
        
        self.pbaddieBulletAddCounter += 10

        if self.pbaddieBulletAddCounter == 100:
            self.pbaddieBulletAddCounter = 0
            for pb in self.powerBaddies[level-1]:
                if pb['rect'].top >= 0:
                    newpBaddieBullet = {'line': pygame.Rect(pb['rect'].centerx, pb['rect'].top, self.BULLETWIDTH, self.BULLETHEIGHT),
                                       'speed': random.randint(self.BULLETMINMOVERATE, self.BULLETMAXMOVERATE),
                                       'surface':pygame.transform.scale(self.baddieBulletUpgradeImage4, (self.BULLETWIDTH * 20, self.BULLETHEIGHT * 7)),
                                       }

                    self.pbaddieBullets[level-1].append(newpBaddieBullet) 

        #return pbaddieBullets

    def powerBaddie_bullet_move(self):
        level = self.get()
        # Move powerbaddie bullets down
        for pbb in self.pbaddieBullets[level-1]:
            pbb['line'].move_ip(0, pbb['speed'])

        #return pbaddieBullets

    def baddieCaptain_bullet_generation_1(self):
        level = self.get()
        # Make baddieCaptain bullets
        
        self.baddiecBulletAddCounter += 10
        
        if self.baddiecBulletAddCounter == 100:
            self.baddiecBulletAddCounter = 0
            for bc in self.baddieCaptains[level-1]:
                if bc['rect'].top >= 0:
                    newBaddieCaptainBullet = {'line': pygame.Rect(bc['rect'].centerx, bc['rect'].top, self.BULLETWIDTH, self.BULLETHEIGHT),
                                             'speed': random.randint(self.BULLETMINMOVERATE_, self.BULLETMAXMOVERATE_),
                                             'surface':pygame.transform.scale(self.baddieBulletUpgradeImage3, (self.BULLETWIDTH * 20, self.BULLETHEIGHT * 7)),
                                             }

                    self.baddieCaptainBullets[level-1].append(newBaddieCaptainBullet)

        #return baddieCaptainBullets

    def baddieCaptain_bullet_generation_2(self):
        level = self.get()
        
        self.baddiecBulletAddCounter += 5
        
        if self.baddiecBulletAddCounter == 50:
            self.baddiecBulletAddCounter = 0
            for bc in self.baddieCaptains[level-1]:
                if bc['rect'].top >= 0:
                    newBaddieCaptainBullet = {'line': pygame.Rect(bc['rect'].centerx, bc['rect'].top, self.BULLETWIDTH, self.BULLETHEIGHT),
                                             'speed': random.randint(self.BULLETMINMOVERATE, self.BULLETMAXMOVERATE),
                                             'surface':pygame.transform.scale(self.baddieBulletUpgradeImage3, (self.BULLETWIDTH * 20, self.BULLETHEIGHT * 7)),
                                             }

                    self.baddieCaptainBullets[level-1].append(newBaddieCaptainBullet)

        #return baddieCaptainBullets

    def baddieCaptain_bullet_move(self):
        level = self.get()
        # Move baddiecaptain bullets down
        for bcb in self.baddieCaptainBullets[level-1]:
            
            if bcb['line'].left < self.player.left and bcb['line'].top < self.player.top:
                bcb['line'].move_ip(bcb['speed'], bcb['speed'])
            elif bcb['line'].left >= self.player.left and bcb['line'].top < self.player.top:
                bcb['line'].move_ip(-bcb['speed'], bcb['speed'])
            elif bcb['line'].left < self.player.left and bcb['line'].top >= self.player.top:
                bcb['line'].move_ip(bcb['speed'], -bcb['speed'])
            elif bcb['line'].left >= self.player.left and bcb['line'].top >= self.player.top:
                bcb['line'].move_ip(-bcb['speed'], -bcb['speed'])
            

        #return baddieCaptainBullets

    def sultan_bullet_generation_1(self):
        level = self.get()
        # Add SultanBullets
        
        for su in self.sultans[level-1]:
            if su['rect'].top >= 0:
                if abs(su['rect'].centerx - self.player.centerx) < 100:
                    self.sultanBulletAddCounter += 20
        
                    if self.sultanBulletAddCounter == 100:
                        self.sultanBulletAddCounter = 0
                        if 60 <= self.sultan_angle <= 120 and self.num2 == 0:
                            self.sultan_angle += 1
                            if self.sultan_angle == 120:
                                self.num2 = 1
                        elif 60 <= self.sultan_angle <= 120 and self.num2 == 1:
                            self.sultan_angle -= 1
                            if self.sultan_angle == 60:
                                self.num2 = 0
            
                        self.sultan_length+=0.2
                        self.sultan_length %= 12
                        if self.sultan_length < 2:
                            self.sultan_length+=2
            
            
                        newSultanBullets = {'line': pygame.Rect(su['rect'].centerx, su['rect'].centery, self.BULLETWIDTH, self.BULLETHEIGHT),
                                            'speedx': self.sultan_length*cos(radians(self.sultan_angle)),
                                            'speedy': self.sultan_length*sin(radians(self.sultan_angle)),
                                            'surface':pygame.transform.scale(self.sultanBulletImage, (self.BULLETWIDTH * 20, self.BULLETHEIGHT * 7)),
                                            }

                        self.sultanBullets[level-1].append(newSultanBullets)

        #return sultanBullets 

    def sultan_bullet_generation_2(self):
        level = self.get()
        
            
        self.sultanBulletAddCounter += 4
        
        if self.sultanBulletAddCounter == 400:
            self.sultanBulletAddCounter = 0
            for su in self.sultans[level-1]:
                if su['rect'].top >= 0:
                    #if (su['rect'].centerx-player.centerx) == 0:
                        #player.centerx = su['rect'].centerx + 1
                    try:
                        self.sultan_angle = degrees(atan((self.player.centery-su['rect'].centery)/(self.player.centerx-su['rect'].centerx)))
                    except ZeroDivisionError:
                        #player.centerx = su['rect'].centerx + 1
                        self.sultan_angle = degrees(atan(self.player.centery-su['rect'].centery))
                #sultan_angle = sultan_angle - 30
                #if 30 <= sultan_angle <= 90:
                    for i in range(0,60,2): 
                        self.sultan_angle += i
                    
                    #num2 = 1
                
            
                        self.sultan_length+=0.5
                        self.sultan_length %= 12
                        if self.sultan_length < 2:
                            self.sultan_length+=2
                
                    
                        newSultanBullets = {'line': pygame.Rect(su['rect'].centerx, su['rect'].centery, self.BULLETWIDTH, self.BULLETHEIGHT),
                                            'speedx': self.sultan_length*cos(radians(self.sultan_angle)),
                                            'speedy': self.sultan_length*sin(radians(self.sultan_angle)),
                                            'surface':pygame.transform.scale(self.sultanBulletImage, (self.BULLETWIDTH * 20, self.BULLETHEIGHT * 7)),
                                            }

                        self.sultanBullets[level-1].append(newSultanBullets)

        #return sultanBullets

    def sultan_bullet_move(self):
        level = self.get()
        # Move sultan bullets down
        for sub in self.sultanBullets[level-1]:
            sub['line'].move_ip(sub['speedx'], sub['speedy'])

        #return sultanBullets

    """def control_level(self, level):
        if level == 1:
            self.con_num = 10"""

    def makeTextObjs(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()

    def checkForKeyPress(self):
        self.checkForQuit()

        for event in pygame.event.get([KEYDOWN, KEYUP]):
            if event.type == KEYDOWN:
                continue
            return event.key
        return None

    def showTextScreen(self, text):
        titleSurf, titleRect = self.makeTextObjs(text, self.BIGFONT, self.TEXTSHADOWCOLOR)
        titleRect.center = (int(self.WINDOWWIDTH/2), int(self.WINDOWHEIGHT/2))
        self.WINDOWSURFACE.blit(titleSurf, titleRect)

        titleSurf, titleRect = self.makeTextObjs(text, self.BIGFONT, self.TEXTCOLOR)
        titleRect.center = (int(self.WINDOWWIDTH/2)-3, int(self.WINDOWHEIGHT/2)-3)
        self.WINDOWSURFACE.blit(titleSurf, titleRect)

        pressKeySurf, pressKeyRect = self.makeTextObjs('Press a key to play.', self.BASICFONT, self.TEXTCOLOR)
        pressKeyRect.center = (int(self.WINDOWWIDTH/2), int(self.WINDOWHEIGHT/2) + 100)
        self.WINDOWSURFACE.blit(pressKeySurf, pressKeyRect)

        while self.checkForKeyPress() == None:
            pygame.display.update()
            self.FPSCLOCK.tick()

    def checkForQuit(self):
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self.terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back

            
    def hitCherry(self):
        for ch in self.cherry:
            if self.player.colliderect(ch['rect']):
                
                self.cherry.remove(ch)
                return True
                #if musicPlaying:
                    #pickUpSound.play()
                
           
                        
        
    def playerBulletHasHitBaddie(self, xi, yi):
        for y in yi:
            for x in xi:
                if x['line'].colliderect(y['line']):
                    xi.remove(x)
                    yi.remove(y)
                    self.score += 3
                    break
                
            
            
        
    def terminate(self):
        pygame.quit()
        sys.exit()

    def waitForPlayerToPressKey(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: # pressing escape quits
                        self.terminate()
                    return

    def playerHasHitBaddie(self):
        for b in self.baddies:
            if self.player.colliderect(b['rect']):
                self.baddies.remove(b)
                b['sig'] = True
                return True
        return False

    def playerHasHitCherry(self):
        for ch in self.cherries:
            if self.player.colliderect(ch['rect']):
                return True
        return False

    def drawText(self, text, font, surface, x, y):
        
        textobj = font.render(text, 1, self.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        

        

            
    def bulletMove1(self):
       #for i in range(100): 
        for bu in self.bullets:
            bu['line'].move_ip(0, -bu['speed'])
            
    def bulletStop(self):
        for bu in self.bullets:
            bu['line'].move_ip(0, 0)

    def ma_draw(self, ma):
        for i in ma:
            if self.isOnBoard(i['rect']):
                self.WINDOWSURFACE.blit(i['surface'],i['rect'])

    def mab_draw(self, mab):
        for i in mab:
            if self.isOnBoard(i['line']):
                self.WINDOWSURFACE.blit(i['surface'],i['line'])

    def del_life(self, list):
        for i in list:
            if not self.isOnBoards(i['rect']):
                list.remove(i)
                i['healthbar'] = 0

    def del_lifes(self, list):
        for i in list:
            if not self.isOnBoards(i['rect']):
                list.remove(i)

    def del_bullet(self, list):
        for i in list:
            if i['line'].bottom > self.WINDOWHEIGHT or i['line'].top < 0 or i['line'].left > self.WINDOWWIDTH or i['line'].right < 0:
                list.remove(i)

    def del_collide_bullet(self, list):
        
        for i in list:
                
            list.remove(i)

    def getValidMoves(self, baddies, bullets):
        dis = []
        
        while True:
            if baddies['rect'].bottom < self.player.top and baddies['rect'].left > self.player.right:  
                bullets['line'].left += bullets['speed']
                bullets['line'].top -= bullets['speed']
        
            elif baddies['rect'].bottom < self.player.top and baddies['rect'].right <= self.player.left:  
                bullets['line'].left -= bullets['speed']
                bullets['line'].top -= bullets['speed']
        
            elif baddies['rect'].top >= self.player.bottom and baddies['rect'].left > self.player.right:  
                bullets['line'].left += bullets['speed']
                bullets['line'].top += bullets['speed']
        
            elif baddies['rect'].top >= self.player.bottom and baddies['rect'].right <= self.player.left:  
                bullets['line'].left -= bullets['speed']
                bullets['line'].top += bullets['speed']

            if baddies['rect'].colliderect(bullets['line']):
                s = sqrt((baddies['rect'].centerx-self.player.centerx) ** 2 + (baddies['rect'].centery-self.player.centery) ** 2)
                dis.append(s)
                baddies.remove(baddies)
                bullets.remove()
                return dis
            elif self.isOnBoard(baddies, i):
                continue
            elif not self.isOnBoard(baddies, i):
                return False
                
    def isOnBoard(self, x):
        #for b in x:
        return x.left >= 0 and x.right <= self.WINDOWWIDTH and x.bottom >= 0 and x.top <= self.WINDOWHEIGHT 

    def isOnBoards(self, i):
        
        return i.top <= self.WINDOWHEIGHT and i.right <= self.WINDOWWIDTH 

    def whoGoesFirst(self):
        if random.randint(0, 1) == 0:
            return -mixSize
        else:
            return self.WINDOWHEIGHT

    def collide(self, i):
        for j in i:
            i.remove(j)

    def minimum(self, baddies):
        u=k=0
        y=z=dict()
        for i in range(len(baddies)):
            for j in range(len(baddies)-1,i,-1):
                y = baddies[j-1]
                z = baddies[j]
                k = int((self.player.centerx - y['rect'].left)**2 +(self.player.centery - y['rect'].top)**2)
                u = int((self.player.centerx - z['rect'].left)**2 +(self.player.centery - z['rect'].top)**2)
                            
                if u > k:
                    u,k=k,u            
                    z['rect'], y['rect'] = y['rect'], z['rect']
                
        return [u, z]

    def draw(self, bullets):
        for b in bullets:
            self.WINDOWSURFACE.blit(b['surface'], b['line'])

if __name__ == '__main__':   
    
    game = GameSet()    
    game.main()