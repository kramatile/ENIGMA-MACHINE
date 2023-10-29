import pygame
# complicated mechanical components with complexe wiring that helps encypt a letter with a certain deviation
class rotor :
    def __init__(self,wiring,notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring 
        self.notch = notch

    def forward(self,signal) :
        A = self.right[signal]
        return self.left.find(A)

    def backward(self,signal):
        B = self.left[signal]
        return self.right.find(B)
    
    def show(self):
        print(self.right)
        print(self.left)
        print("")
    
    def rotate(self,n=1,forward = True):
        for i in range(n):
            if forward == True :
                self.right = self.right[1:] + self.right[0]
                self.left = self.left[1:] + self.left[0]
            else : 
                self.right = self.right[25] + self.right[:25]
                self.left = self.left[25] + self.left[:25]
                

    def rotate_to_letter(self,letter):
        position = self.left.find(letter)
        self.rotate(position)

    def set_ring(self,n):

        notch_position = self.left.find(self.notch)
        self.notch = self.left[(notch_position - n + 1) % 26]

        self.show()
        self.rotate(n-1,forward=False)
        self.show()

    def draw(self,screen,x,y,w,h,font):
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen,"white",r,width=2,border_radius=15)

        
        for i in range(26): 
            
            letter_r = self.left[i]
            letter_r = font.render(letter_r,True,"grey")
            text_box = letter_r.get_rect(center=(x+w/4 , y + (i+1)*h/27 ))
            if i == 0:
                pygame.draw.rect(screen,"teal",text_box,border_radius=5)
            
            if self.left[i] == self.notch :
                letter_r = font.render(self.notch,True,"#333333")
                pygame.draw.rect(screen,"white",text_box,border_radius=5)

            screen.blit(letter_r,text_box)

            letter_r = self.right[i]
            letter_r = font.render(letter_r,True,"grey")
            text_box = letter_r.get_rect(center=(x+w*3/4 , y + (i+1)*h/27 ))
            screen.blit(letter_r,text_box)


            



    """def rotate(self,letter):
        position_translation = self.left.find(letter)
        self.right = self.right[position_translation:] + self.right[0:position_translation]
        self.left = self.left[position_translation:] + self.left[0:position_translation]"""
