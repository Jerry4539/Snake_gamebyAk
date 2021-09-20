import random
def gameWin(com,you):
	if comp == you:
		return None
	elif comp == 's':
		if you == 'si':
        		return False
	if you =='p':
					return True
	elif comp == 'si':
		if you == 'p':
					return False
	if you == 's':
						return True
	elif comp == 'p':
			if you == 'si':
								return True
	if you == 's':
									return False
									
print("comp Turn : stone (s) paper (p) scissor (si) ?? ")
randoNo=random.randint(1,3)
if randoNo==1:
  	comp ='s'
elif randoNo==2:
  		comp = 'p'
elif randoNo==3:
  			comp = 'si'
  			print(f"the computer has choosen {comp}")  
  	#		print(f"The game has choosen{comp}")			
you = input("Your turn : stone (s) paper (p) scissor (si) ??? ")
a= gameWin (comp,you)
if a==None:
	print("The game was tie")
elif a==True:
		print("You win")
elif a==False:
   			print("You Lose")
   			
   			
   			
   			
   			
   			
   			
   			
   			