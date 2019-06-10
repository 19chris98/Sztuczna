from scieżka import astar
def main():
	a = [[1,1,1,1,1,1,1,1],
		 [1,1,1,0,1,3,5,1],
		 [1,0,0,0,0,4,1,1],
		 [1,0,0,1,1,1,0,1],
		 [1,0,1,0,1,0,0,1],
		 [1,0,0,0,0,1,0,1],
		 [1,0,1,7,7,7,1,1],
		 [1,1,1,1,1,1,1,1]
		 ]
	nowe=[0,0,0,0,0,0,0,0,0,0]
	print(a[0])
	print(a[1])
	print(a[2])
	print(a[3])
	print(a[4])
	print(a[5])
	print(a[6])
	print(a[7])
	q=0
	#petla do ilosci bomb
	while q<4:
		#ustalenie gdzie znajduje sie nasz robot
		for i in range(0,7):
			for j in range(0,7):
				if(a[i][j]==3):
					robot = (i, j)
					iRobota = i
					jRobota = j 
		#wyszukiwanie od konca
		for i in range(0,7):
			for j in range(0,7):
				if(a[i][j]==4 or a[i][j]==5 or a[i][j]==6 or a[i][j]==7):
					finish = (i, j)
					iBomby = i 
					jBomby = j	
		#zadeklarowanie temp
		temp = [[0 for x in range(7)]for y in range(7)]
		#tworzenie tymczasowej macierzy by dzialala z funkcja szukania a*(zmienienie bomb, '3' na 0 by dalo sie tam wchodzic i przechodzic )
		for i in range(0,7):
			for j in range(0,7):
				if(a[i][j]==3 or a[i][j]==4 or a[i][j]==5 or a[i][j]==6 or a[i][j]==7):
					temp[i][j]=0
				else:
					temp[i][j]=a[i][j]	
		#uzycie funkcji chodzenia
		print("start: "+str(robot))
		print("finish: "+str(finish))
		path = astar(temp, robot, finish)
		print(path)
		#tu proba rozbrojenia
		if a[iBomby][jBomby] in [3,4,5,6,7]:
			if a[iBomby][jBomby]>=5 and a[iBomby][jBomby]<7:
				if a[iBomby][jBomby]>=6:
					a[iBomby][jBomby] = 3
					a[iRobota][jRobota] = 0
					q=q+1
				else:
					a[iBomby][jBomby] = 3
					a[iRobota][jRobota] = 0
					q=q+1
			if a[iBomby][jBomby]== 4:
				a[iBomby][jBomby] = 3
				a[iRobota][jRobota] = 0
				q=q+1
			if a[iBomby][jBomby]==7:
				if nowe[a[iBomby][jBomby]]==0:
					for i in range(1,9):
						if i==1 or i==2 or i==3 or i==4 or i==6 or i==7 or i==8:
							pass
						else:
							a[iBomby][jBomby] = 3
							a[iRobota][jRobota] = 0
							print(i)
							q=q+1
							nowe[7]=1
							print(nowe)
				else:
					a[iBomby][jBomby] = 3
					a[iRobota][jRobota] = 0
					q=q+1	
		else:
			print("niepoprawna zmienna")
			pass
						
	#tu mozna zrobic przejscie robota do bazy i usunac ta "3" z macierzy wtedy zostanie tylko baza oraz "0" i "1"	
	print("Pole minowe po zakończeniu z robotem nadal na polu")
	print(a[0])
	print(a[1])
	print(a[2])
	print(a[3])
	print(a[4])
	print(a[5])
	print(a[6])
	print(a[7])
if __name__ == '__main__':
    main()
