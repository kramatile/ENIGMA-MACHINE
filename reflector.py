import pygame
# is the last components and it reflects the signal back to the keyboard 
class reflector :
    def __init__(self,wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring 

    def reflect(self,signal) :
        A = self.right[signal]
        return self.left.find(A)
    
    def draw(self,screen,x,y,w,h,font):
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen,"white",r,width=2,border_radius=15)

        
        for i in range(26): 
            
            letter_r = self.left[i]
            letter_r = font.render(letter_r,True,"grey")
            text_box = letter_r.get_rect(center=(x+w/4 , y + (i+1)*h/27 ))

            screen.blit(letter_r,text_box)

            letter_r = self.right[i]
            letter_r = font.render(letter_r,True,"grey")
            text_box = letter_r.get_rect(center=(x+w*3/4 , y + (i+1)*h/27 ))
            screen.blit(letter_r,text_box)
