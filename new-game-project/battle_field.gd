extends Node2D
class_name battleField
var tiles = []
var height = 4
var width = 8
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	for x in range(1, width+1):
		tiles.append([])
		for y in range(1, height+1):
			tiles[x-1].append(get_node("%s%s" % [x,y]))
	print(tiles)
	pass # Replace with function body.

func get_tile(index:Vector2i):
	#zero index i think?
	return tiles[index[0]-1][index[1]-1]
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
