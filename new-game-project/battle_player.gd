extends Sprite2D
class_name battlePlayer

var currentPos:Vector2i = Vector2i(1,2)
var cHealth = Player.cHealth
var mHealth = Player.mHealth
var cMp = Player.cMp
var mMp = Player.mMp
var attack = Player.attack
var magic = Player.magic
var defense = Player.defense
var speed = Player.speed
var luck = Player.luck
var zMove = Moves.slice#Player.zMove
var xMove = Player.xMove
var cMove = Player.cMove
var spMove = Player.spMove
var state = "normal"
var moveCooldown = 0
var counter = 0
var battleManager: battleManager = null
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	battleManager = get_parent()
	pass # Replace with function body.

func useAttack(move: Attack):
	self.counter = 0
	self.state = move.strat
	

func move(direction: String):
	#submit a move.. could resolve with battlemaanger
	#for collisions.
	match direction:
		"up":
			battleManager.playerMove = "up"
		"down":
			battleManager.playerMove = "down"
		"left":
			battleManager.playerMove = "left"
		"right":
			battleManager.playerMove = "right"
		_:
			pass
			
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func strategy():
	pass
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	print("Current state: ", state)
	print("Curre pos:", position)
	if state not in ["paralyzed", "cooldown"] and not moveCooldown:
		if Input.is_action_just_pressed("k_Up"):
			move("up")
		if Input.is_action_just_pressed("k_Down"):
			move("down")
		if Input.is_action_just_pressed("k_Left"):
			move("left")
		if Input.is_action_just_pressed("k_Right"):
			move("right")
		if Input.is_action_just_pressed("k_Z"):
			var pts: Array[Vector2i] = [self.currentPos + Vector2i(1,0)]
			%attackManager.addAttack(pts, 10, 10, 10, "player")
			#useAttack(zMove)
			
		if Input.is_action_just_pressed("k_X"):
			useAttack(xMove)
		if Input.is_action_just_pressed("k_C"):
			useAttack(cMove)
	if state == "slice":
		counter += 1
		if counter == 10:
			#shift to slice animations?
			state = "normal"
			pass
			
			#how to submit attack to battlefield?
			
		
		
		
			
		
	pass
