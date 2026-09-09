extends Node

var slice = Attack.new();
var heal = Attack.new();

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	
	slice.init("Slice", "slice", 1)
	
	heal.init("Heal", "heal", 1);
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
