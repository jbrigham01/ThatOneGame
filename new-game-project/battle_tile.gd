extends Sprite2D
class_name battleTile
var state = "normal"
var isOccupied = false
var isBroken = false
var damageCounter = 0
var damage = 0
var damageFrame = 0
var damageDuration = 0



# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.
	
func damageTick():
	"""
	self.damageCounter += 1
	if self.damageCounter >= damageFrame and self.damageCounter <= (self.damageFrame + damageDuration):
		self.state = "damage"
		if 
			if self.damages == "player":
				if player.
			pass
			#self.occupant.damage()
		pass
		"""
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
