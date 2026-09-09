extends Control


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	size = get_viewport().get_visible_rect().size
	var start =  %Button
	start.pressed.connect(_beginGame)
	
	
func _beginGame() -> void:
	get_tree().change_scene_to_file("res://overworld.tscn")


# Called every frame. 'delta' is the elapsed time since the previous frame.
