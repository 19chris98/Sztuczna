print("7-gracz\n8-ściana\n9-puste pole\n0-1-bomby")
b=[0,0,0,0]
a = [[8,8,8,8], [8,7,1,8], [8,2,0,8],[8,8,8,8]]
zapas=a
class BombaNr0:
    def ProbaRoz(self,x):
        if(int(x)==8):
            return 1
        else:
            return 0
class BombaNr1:
    def ProbaRoz(self,x):
        if(int(x)==3):
            return 1
        else:
            return 0
class BombaNr2:
    def ProbaRoz(self,x):
        if(int(x)==2):
            return 1
        else:
            return 0
class BombaNr3:
    def ProbaRoz(self,x):
        if(int(x)==5):
            return 1
        else:
            return 0
print (b)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
d=0
for i in range (1,3):
	for j in range (1,3):
		if a[i][j]==0:
			bomb=BombaNr0()
			if (b[0]==0):
				for h in range (1,9):
					d=d+1
					if bomb.ProbaRoz(h)==1:
						b[0]=h
						a[i][j]=9
						print ("Bomba na polu nr: ",i,j," została rozbrojona")
						break
			else:
				bomb.ProbaRoz(b[0])
				a[i][j]=9
				d=d+1
				print ("Bomba na polu nr: ",i,j," została rozbrojona")
		if a[i][j]==1:
			bomb=BombaNr1()
			if (b[1]==0):
				for h in range (1,9):
					d=d+1
					if bomb.ProbaRoz(h)==1:
						b[1]=h
						a[i][j]=9
						print ("Bomba na polu nr: ",i,j," została rozbrojona")
						break
			else:
				bomb.ProbaRoz(b[1])
				a[i][j]=9
				d=d+1
				print ("Bomba na polu nr: ",i,j," została rozbrojona")
		if a[i][j]==2:
			bomb=BombaNr2()
			if (b[2]==0):
				for h in range (1,9):
					d=d+1
					if bomb.ProbaRoz(h)==1:
						b[2]=h
						a[i][j]=9
						print ("2Bomba na polu nr: ",i,j," została rozbrojona")
						break
			else:
				bomb.ProbaRoz(b[2])
				a[i][j]=9
				d=d+1
				print ("Bomba na polu nr: ",i,j," została rozbrojona")
		if a[i][j]==3:
			bomb=BombaNr3()
			if (b[3]==0):
				for h in range (1,9):
					d=d+1
					if bomb.ProbaRoz(h)==1:
						b[3]=h
						a[i][j]=9
						print ("Bomba na polu nr: ",i,j," została rozbrojona")
						break
			else:
				bomb.ProbaRoz(b[3])
				a[i][j]=9
				d=d+1
				print ("Bomba na polu nr: ",i,j," została rozbrojona")
				
print ("Bomby zostały rozbrojone za podejściem nr: ",d)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print (b)
for i in range (0,4):
	if b[i]!=0:
		print("Do rozbrojenia bomby numer",i,", użyjemy narzędzia nr.:",b[i])
	else:
		print("Nie było bomby nr.:",i,", lub w danych testowych było za mało informacji")
