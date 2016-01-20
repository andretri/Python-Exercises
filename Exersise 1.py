from random import randint

#PLAYER COORDINATES
player_x = randint(0,9)
player_y = randint(0,9)
#TREASURE COORDINATES
treasure_x = randint(0,9)
treasure_y = randint(0,9)

while(not((treasure_x == player_x) and (treasure_y == player_y))):	
	tmp = raw_input("> Move Where? (w,a,s,d):  ")
	if( (tmp.lower() == "w") and (player_y-1>=0) ):
		player_y-=1
	elif( (tmp.lower() == "a") and (player_x-1>=0) ):
		player_x-=1
	elif( (tmp.lower() == "s") and (player_y+1<=9) ):
		player_y+=1
	elif( (tmp.lower() == "d") and (player_x+1<=9) ):
		player_x+=1
	else:
		print "Out of Boundaries. Select a different route!"
	distance = (abs(treasure_x-player_x) + abs(treasure_y-player_y))
	#print "Your location: ",player_x,",",player_y           [FOR DEBUGGING PURPOSES]
	#print "Treasure location: ",treasure_x,",",treasure_y           [FOR DEBUGGING PURPOSES]
	print "Range From Treasure: %d Tiles" %(distance)

print "Congratulations! You found the Treasure."