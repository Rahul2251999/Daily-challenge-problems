s = input()
t = input()
#pos = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,'e' : 5,'f' : 6,'g' : 7,'h' : 8}
ps = [(ord(s[0]) - 96), int(s[1])]
pt = [(ord(t[0]) - 96), int(t[1])]
tt = ps

path = []
c = 0
#sensing shortest part
while(pt != tt):
    if(tt[0] == pt[0]):
        if(tt[1] <  pt[1]):
            tt[1] = tt[1]+1
            path.append("U")
           
            c += 1
        elif(tt[1] > pt[1]):
            tt[1] = tt[1]-1
            path.append("D")
            c += 1   #gdyulfgyles
           
    elif(tt[1] == pt[1]):
        if(tt[0] <  pt[0]):
            tt[0] = tt[0]+1
            path.append("R")
            c += 1
           
        elif(tt[0] > pt[0]):
            tt[0] = tt[0]-1
            path.append("L")
            c += 1
           
    elif(tt[0] < pt[0]) and (tt[1] < pt[1]):
        tt[0] = tt[0]+1
        tt[1] = tt[1]+1
        path.append("RU")
        c += 1
       
    elif(tt[0] < pt[0]) and (tt[1] > pt[1]):
        tt[0] = tt[0]+1
        tt[1] = tt[1]-1
        path.append("RD")
        c += 1
       

    elif(tt[0] > pt[0]) and (tt[1] < pt[1]):
        tt[0] = tt[0]-1
        tt[1] = tt[1]+1
        path.append("LU")
        c += 1
       

    elif(tt[0] > pt[0]) and (tt[1] > pt[1]):
        tt[0] = tt[0]-1
        tt[1] = tt[1]-1
        path.append("LD")
        c += 1
       
   
print(c)
for i in range(c):
    print(path[i])         
