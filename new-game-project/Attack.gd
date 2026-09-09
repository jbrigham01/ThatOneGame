extends Node
class_name Attack

var gameName: String
var strat: String
var power: int


func init(nm: String, st: String, pw:int) -> void:
	gameName = nm
	strat = st
	power = pw
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
