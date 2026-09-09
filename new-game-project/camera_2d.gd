extends Camera2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	var tileLayer = get_node("%TileMapLayer")
	var map = get_node("%AreaHolder")
	var mapHolder = map.get_child(0);
	var currmap = mapHolder.get_child(0);
	var bounds = currmap.get_used_rect()
	var tile_size = tileLayer.tile_set.tile_size
	self.limit_top = 0
	self.limit_left = 0
	self.limit_right = (bounds.position.x + bounds.size.x) * tile_size.x * 2
	self.limit_bottom = (bounds.position.y + bounds.size.y) * tile_size.y * 2
	


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
