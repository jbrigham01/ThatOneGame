extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	
	
	pass # Replace with function body.

var inMenu = 0
@onready var MapLayer:TileMapLayer = get_node("TileMapLayer")
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	if Input.is_action_just_released("k_Enter"):
		if not inMenu:
			add_child(load("res://overworldMenu.tscn").instantiate())
			print("need to activate menu! called from top node")
			inMenu = 1
			MapLayer.process_mode = Node.PROCESS_MODE_DISABLED
			
		else:
			inMenu = 0
			print(get_children())
			
			get_node("CanvasLayer").queue_free()
			MapLayer.process_mode = Node.PROCESS_MODE_INHERIT
			
			
			
		
			
	pass
	
	

	
func loadNewLevel(newLevel: String) -> void:
	#this is the code to laod new levels!
	var holder = get_node("%AreaHolder")
	holder.get_child(0).queue_free()
	var scene = load("res://" + newLevel)
	var sc = scene.instantiate()
	holder.add_child(sc)
	
