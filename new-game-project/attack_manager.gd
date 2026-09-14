extends Node
class_name attackManager

class attack:
	var tiles : Array[Vector2i] = []
	var damageCounter = 0
	var damageFrame = 1
	var damageDuration = 1  
	var damageAmount = 1
	var damages = "" #Player | Enemy
	var pierceInvis = null
	var stagger = null
	var hitstun = 0
	var blockStagger = null
	var critical = 0
	
	func _init(t : Array[Vector2i], dAmount:int, dFrame:int, dDuration:int, dm:String, args:Array = [], kwargs:Array[Array] = []) -> void:
		tiles = t
		damageFrame = dFrame
		damageDuration = dDuration
		damageAmount = dAmount
		damages = dm
		#actual programming for once
		for arg in args:
			match arg:
				"pierceInvis":
					pierceInvis = true
				"stagger":
					stagger = true
				"blockStagger":
					blockStagger = true
		for kwarg in kwargs:
			var val = kwarg[1]
			match kwarg[0]:
				"hitstun":
					hitstun = val
				"critical":
					critical = val
		
		


var attacks = []


func addAttack(t: Array[Vector2i], amount : int, frame : int, duration : int, damages : String, modifies : Array[String] = []):
	var atk = attack.new(t, amount, frame, duration, damages, modifies)
	for tile in t:
		var Tile: battleTile = %battleField.get_tile(tile)
		if not Tile.isBroken:
			Tile.state = "warning"
			Tile.modulate = Color.YELLOW
	attacks.append(atk)
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

func processAtk(atk: attack):
	atk.damageCounter += 1
	#10 for slow removal
	if atk.damageCounter > (atk.damageFrame + atk.damageDuration + 10):
		for tile in atk.tiles:
			%battleField.get_tile(tile).state = "normal"
			%battleField.get_tile(tile).modulate = Color.WHITE
		
	if atk.damageCounter >= (atk.damageFrame) and atk.damageCounter <= (atk.damageFrame + atk.damageDuration):
		for tile in atk.tiles:
			
			%battleField.get_tile(tile).state = "damage"
			%battleField.get_tile(tile).modulate = Color.RED
			
		if atk.damages == "player":
			if %Player.currentPos in atk.tiles:
				print("Damage player")
		if atk.damages == "enemy":
			if %Enemy.currentPos in atk.tiles:
				print("Damage Enemy")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	for atk in attacks:
		processAtk(atk)
	attacks = attacks.filter(func (atk): return atk.damageCounter <= (atk.damageFrame + atk.damageDuration + 10))
