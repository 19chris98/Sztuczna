print("7-gracz\n8-ściana\n9-puste pole\n0-1-bomby")
b=[0,0,0,0]
a = [[8,8,8,8], [8,7,1,8], [8,2,0,8],[8,8,8,8]]
test=[
	[0,1,"no"],
	[1,2,"no"],
	[0,8,"yes"],
	[0,4,"no"],
	[0,6,"no"],
	[1,2,"no"],
	[1,5,"no"],
	[1,2,"no"],
	[2,4,"no"],
	[2,8,"no"],
	[3,7,"no"],
	[2,6,"no"],
	[3,4,"no"],
	[3,3,"no"],
	[3,5,"yes"]
	]
for i in range(0,8):
	if test[i][2]=="yes":
		b[test[i][0]]=test[i][1]
print (b)
class BombaNr0:
    def ProbaRoz(self,x):
        if(int(x)==2):
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
        if(int(x)==8):
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
		print(i,j)
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
print ("Bomby zostały rozbrojone za podejściem nr: ",d)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print (b)
print("Do rozbrojenia bomby numer 0, użyjemy narzędzia nr.:",b[0])
print("Do rozbrojenia bomby numer 1, użyjemy narzędzia nr.:",b[1])
