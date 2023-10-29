import pygame


from key import Keyboard 
from plugboard import Plugboard 
from rotor import rotor 
from reflector import reflector 
from Enigma import Enigma
from draw import Draw
"""
I   = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
II  = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
III = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
IV	= rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
V	= rotor("VZBRGITYUPSDNHLXAWMJQOFECK","Z")
A = reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB  = Keyboard()
PG = Plugboard(["AR","GK","OX"])

letter = "A"
signal = KB.forward(letter)
signal = PG.forward(signal)
signal = III.forward(signal)
signal = II.forward(signal)
signal = I.forward(signal)
signal = A.reflect(signal)
signal = I.backward(signal)
signal = II.backward(signal)
signal = III.backward(signal)
signal = PG.backward(signal)
letter = KB.backward(signal)

print("THE LETTER WAS : A and became : " + letter)
"""
# initializing the screen
pygame.init()
pygame.font.init()
pygame.display.set_caption("ENIGMA PROJECT")

# setting the screen variables
WIDTH = 1600
HEIGHT = 900
SCREEN =pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS = {"top":200, "bottom":200,"left":100,"right":100}
GAP = 100
INPUT = ""
OUTPUT = ""
PATH =[]

#setting fonts
Mono = pygame.font.SysFont('timesnewroman',13)
Bold = pygame.font.SysFont('timesnewroman',13,bold=True)



# the main enigma historicall components
I   = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
II  = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
III = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
IV	= rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
V	= rotor("VZBRGITYUPSDNHLXAWMJQOFECK","Z")
A = reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB  = Keyboard()
PG = Plugboard(["AB","CD","EF"])
"""
E = Enigma(B,IV,II,I,PG,KB)

E.set_rings((1,1,2))

E.Set_Key("CAT")

message = "TESTINGTESTINGTESTINGTESTING"
ENCRYPT = ""
for element in message:
    ENCRYPT = ENCRYPT + E.encryptLetter(element)

print(ENCRYPT)
"""
E = Enigma(B,IV,II,I,PG,KB)

# the animation
ANIMATING = True
while ANIMATING :
    SCREEN.fill("#333333")

    letter_r = Bold.render(INPUT,True,"white")
    text_box = letter_r.get_rect(center=(WIDTH/2 , MARGINS["top"]/2))
    SCREEN.blit(letter_r,text_box)

    letter_r = Mono.render(OUTPUT,True,"#ADD8E6")
    text_box = letter_r.get_rect(center=(WIDTH/2 , MARGINS["top"]/2 + 15 ))
    SCREEN.blit(letter_r,text_box)

    Draw(E,PATH,SCREEN,WIDTH,HEIGHT,MARGINS,GAP,Bold)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            ANIMATING = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN:
                E.r3.rotate()
            else :
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT += letter
                    PATH,cipher = E.encryptLetter(letter)
                    OUTPUT += cipher
                    