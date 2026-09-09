extends HBoxContainer

var loaded  = 0
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

var state = ""
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	
	if Input.is_action_just_released("K_z"):
		match state:
			"item":
				pass
			"skills":
				pass
			"stats":
				pass
			"world":
				pass
			
	var label:Label = get_node("ColorRect/CenterContainer/Label")
	if not loaded:
		get_node('item').grab_focus()
		loaded = 1
	var nodes = ["item", "skills", "stats", "world"]
	for i:String in nodes:
		if get_node(i).has_focus():
			label.text = i.capitalize()
			state = i
			
	
