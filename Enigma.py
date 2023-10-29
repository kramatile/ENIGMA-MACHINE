# the enigma class implements the whole enigma mechanism : passing a letter from the keyboard to the rotors then to the reflectors and all the way around
class Enigma :
    def __init__(self,re,r1,r2,r3,pb,kb) :
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.pb = pb
        self.kb = kb

# set the key : wich means the letters that are at the top : they were set everyday by operators in the same order so it can get decrypted 
    def Set_Key(self,key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])

# sets the rings to a certain order 
    def set_rings(self,rings):
        self.r1.set_ring(rings[0])
        self.r2.set_ring(rings[1])
        self.r3.set_ring(rings[2])

# the encryption algorithm 
    def encryptLetter(self,letter):
        # rotation conditions :
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch :
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()

        elif self.r2.left[0] == self.r2.notch :
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        
        elif self.r3.left[0] == self.r3.notch :
            self.r3.rotate()
            self.r2.rotate()

        else :
            self.r3.rotate()
        
        signal = self.kb.forward(letter)
        path = [signal,signal]
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.re.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)

        # returns the path and the encrypted letter
        return path, self.kb.backward(signal)
