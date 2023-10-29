import pygame

def Draw(enigma ,path,screen,width,height,margins,gaps,font) :
    w = (width - margins["left"]-margins["right"]-5*gaps)/6
    h = (height - margins["top"]-margins["bottom"])
    
    # draw the lines defining the path that the letter follows while getting enciphered
    y = [margins["top"]+(signal+1)*h/26 for signal in path]
    x = [width - margins["right"] - w/2]
    for i in [4,3,2,1,0]:
        x.append(margins["left"]+i*(w+gaps)+ w*3/4)
        x.append(margins["left"]+i*(w+gaps)+ w*1/4)
    x.append(margins["left"]+w*3/4)
    for i in [1,2,3,4]:
        x.append(margins["left"]+ i*(w+gaps) +w*1/4)
        x.append(margins["left"]+i*(w+gaps)+w*3/4)
    x.append(width - margins["right"] - w/2)
    if len(path) > 0 :
        for i in range(1,21):
            if i < 10 :
                color = "#43aa8b"  
            elif i <12 :
                color = "#f9c74f"
            else :
                color = "#e63946"
            start = (x[i-1],y[i-1])
            end = (x[i],y[i])
            pygame.draw.line(screen,color,start,end,width=5)


    y = margins["top"]
    x = margins["left"]

    # draw components
    for component in [enigma.re,enigma.r1,enigma.r2,enigma.r3,enigma.pb,enigma.kb]:
        component.draw(screen,x,y,w,h,font)
        x += w +gaps

    # components names
    names = ["reflector","Left","Middle","Right","Plugboard","Key/Lamp"]
    y = margins["top"]*6/7
    for i in range(6):
        x = margins["left"] + w/2 + i * (w+gaps)
        title = font.render(names[i],True,"white")
        text_box = title.get_rect(center = (x,y))
        screen.blit(title,text_box)
