print("7-gracz\n8-ściana\n9-puste pole\n0-1-bomby")
a = [[8,8,8,8,8,8,8,8],
     [8,7,1,8,9,9,9,8],
     [8,2,0,9,9,3,1,8],
     [8,9,9,9,9,9,9,8],
     [8,9,9,9,9,9,9,8],
     [8,9,9,9,9,9,9,8],
     [8,9,9,9,9,9,1,8],
     [8,8,8,8,8,8,8,8]
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
		if a[i][j]==0:
			bomb=BombaNr0()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=9
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=9
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=9
		if a[i][j]==1:
			bomb=BombaNr1()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=9
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=9
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=9
		if a[i][j]==2:
			bomb=BombaNr2()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=9
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=9
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=9
		if a[i][j]==3:
			bomb=BombaNr3()
			for k in range (1,8):
				if k>=6:
					break;
				else:
					if k>=2:
						if k>=4:
							if a[i][j]>=3:
								bomb.ProbaRoz(5)
								a[i][j]=9
						else:
							if a[i][j]>=1:
								bomb.ProbaRoz(3)
								a[i][j]=9
							else:
								if a[i][j]==1:
									bomb.ProbaRoz(2)
									a[i][j]=9

#wypisanie planszy
for i in range(0,8):
    print(a[i])
