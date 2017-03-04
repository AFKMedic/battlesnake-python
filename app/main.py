import bottle
import os
import random
import math

def isDangerSquare(data, next):
	dangers = []
	
	snakes = data["snakes"]
	for cord in snakes["coords"]:
		danger.append(cord)
		
	print dangers

def getTaunt():
	taunts = [	'This is a taunt!',
				'Woot taunt']
				
	return random.choice(taunts)

@bottle.route('/static/<path:path>')
def static(path):
	return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():

	data = bottle.request.json
	game_id = data['game_id']
	board_width = data['width']
	board_height = data['height']

	head_url = 'https://thumb1.shutterstock.com/display_pic_with_logo/88356/107460737/stock-photo-beautiful-expressive-adorable-happy-cute-laughing-smiling-baby-infant-face-showing-tongue-isolated-107460737.jpg'
	
	# TODO: Do things with data

	return {
		'color': '#ff6666',
		'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
		'head_url': head_url,
		'name': 'Baby Face',
		'head_type': 'safe',
		'tail_type': 'pixel'
	}

	

@bottle.post('/move')
def move():
	global closeFood
	
	data = bottle.request.json
	
	uid = data["you"]
	snakes = data["snakes"]
	
	for snek in snakes:
		if(snek["id"] == uid):
			me = snek
		
	meX = me["coords"][0][0]
	meY = me["coords"][0][1]
	
	closestCord = []
	closestDistX = 100
	closestDistY = 100
	
	for item in data["food"]:
		currentX = abs(meX - item[0])
		currentY = abs(meY - item[1])
		
		if((currentX < closestDistX) and (currentY < closestDistY)):
			closestDistX = currentX
			closestDistY = currentY
			closestCord = item
		
	print(meX, meY)
	print(closestCord)
	
	isDangerSquare(data, closestCord)
	
	if(closestCord[0] > meX):
		nextMove = 'left'
		print ("- left")
	elif(closestCord[0] < meX):
		nextMove = 'right'
		print ("- right")
	elif(closestCord[1] > meY):
		nextMove = 'down'
		print ("- down")
	elif(closestCord[1] < meY):
		nextMove = 'up'
		print ("- up")
		
	
		
	
	# TODO: Do things with data	
	
	return {
		'move': nextMove,
		'taunt': getTaunt()
	}
	
@bottle.post('/end')
def end():
	data = bottle.request.json

	# TODO: Do things with data

	return {
		'taunt': 'BABY FACE!'
	}


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
	bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
