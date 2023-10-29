import  pygame
# the plugboard is an intermediate board that passes the signal provided by the keyboard to the rotors after deviating it
class Plugboard :
    def __init__(self,pairs) :
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_a = self.left.find(A)
            pos_b = self.left.find(B)
            self.left = self.left[:pos_a]+B+self.left[pos_a+1:]
            self.left = self.left[:pos_b]+A+self.left[pos_b+1:]

    def forward(self,signal) :
        A = self.right[signal]
        return self.left.find(A)

    def backward(self,signal):
        B = self.left[signal]
        return self.right.find(B)
    
    def draw(self,screen,x,y,w,h,font):
        r = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen,"white",r,width=2,border_radius=15)

        
        for i in range(26): 
            letter_r = self.right[i]
            letter_r = font.render(letter_r,True,"grey")
            text_box = letter_r.get_rect(center=(x+w/4 , y + (i+1)*h/27 ))
            screen.blit(letter_r,text_box)

            letter_r = self.left[i]
            letter_r = font.render(letter_r,True,"grey")
            text_box = letter_r.get_rect(center=(x+w*3/4 , y + (i+1)*h/27 ))
            screen.blit(letter_r,text_box)




            