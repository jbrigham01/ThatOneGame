extends Node2D

#uh is this just the jumping off point for the game?
func _ready() -> void:
	#should load in a save here.
	print("loaded!")
	get_tree().change_scene_to_file("mainMenu.tscn")
	pass
	
	
	
	
