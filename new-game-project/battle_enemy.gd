extends Sprite2D
class_name battleEnemy
var counter = 0
var currentPos = Vector2i(6,2)
#should inherit from enemy...
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.
	
func move(dir: String, fast: bool):
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	#strategy
	counter += 1
	
	pass
