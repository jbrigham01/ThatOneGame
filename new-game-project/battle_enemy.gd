extends Sprite2D
class_name battleEnemy
var counter = 0
var moo = 0
var currentPos = Vector2i(6,2)
var strat = "start"
var playerAbove = false
var playerBelow = false
var playerinFront = false
var playerBehind = false
var distanceFromPlayer = false


#should inherit from enemy...
# Called when the node enters the scene tree for the first time.
var battleManager: battleManager = null
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	battleManager = get_parent()
	
func move(direction: String):
		#submit a move.. could resolve with battlemaanger
	#for collisions.
	match direction:
		"up":
			battleManager.enemyMove = "up"
		"down":
			battleManager.enemyMove = "down"
		"left":
			battleManager.enemyMove = "left"
		"right":
			battleManager.enemyMove = "right"
		_:
			pass
	pass
	

func strategy() -> void:
	#where to handle cooldown and stagger?
	counter += 1
	#gray will beam horizontally or vertially
	#You should dodge accordingly, and then strike
	if self.strat == "wait":
		#how many fps?
		if moo == 15:
			if playerAbove:
				pass
		moo += 1
	pass
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:


	
	pass
