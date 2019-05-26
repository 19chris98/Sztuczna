print("3-gracz\n1-ściana\n0-puste pole\n4-7-bomby")
a = [[1,1,1,1,1,1,1,1],
     [1,3,1,0,0,0,0,1],
     [1,0,0,0,0,4,1,1],
     [1,0,0,1,1,1,9,1],
     [1,0,1,0,1,0,0,1],
     [1,0,0,0,0,0,0,1],
     [1,0,1,4,1,5,1,1],
     [1,1,1,1,1,1,1,1]
     ]
#klasy bomb
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
        if(int(x)==3):
            return 1
        else:
            return 0
class BombaNr3:
    def ProbaRoz(self,x):
        if(int(x)==5):
            return 1
        else:
            return 0

#wypisanie planszy
for i in range(0,8):
    print(a[i])

#rozbrajanie
for i in range (1,7):
	for j in range (1,7):
		if a[i][j]==4:
			bomb=BombaNr0()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=0
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=0
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=0
		if a[i][j]==7:
			bomb=BombaNr1()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=0
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=0
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=0
		if a[i][j]==5:
			bomb=BombaNr2()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=0
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=0
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=0
		if a[i][j]==6:
			bomb=BombaNr3()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=0
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=0
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=0

#wypisanie planszy
for i in range(0,8):
    print(a[i])
