import pygame
# the keyboard is where we type the letter we want to get encypted
class Keyboard :
    def forward (self,letter) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return alphabet.index(letter)

    def backward(self,index):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return alphabet[index]
    
    def draw(self,screen,x,y,w,h,font):
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen,"white",r,width=2,border_radius=15)

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        for letter in letters:
            letter = font.render(letter,True,"grey")
            text_box = letter.get_rect(center=(x+w/2 , y + (i+1)*h/27 ))
            screen.blit(letter,text_box)
            i += 1