extends CharacterBody2D


const SPEED = 300.0
const JUMP_VELOCITY = -400.0

var orient = "down"
@onready var anims:AnimatedSprite2D = get_node("Sprite2D/AnimatedSprite2D")



func _ready() -> void:
	#on load function!
	var aHolder = %AreaHolder
	var pStart = aHolder.get_child(0).get_node("playerStart")
	self.position = pStart.position
	print("new pos: ", pStart.position)
	orient = pStart.get_meta("orient")

func _physics_process(delta: float) -> void:
	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	
	
	var direction = Input.get_vector("k_Left", "k_Right","k_Up","k_Down" )
	velocity = direction * 300
	
	
	match direction:
		Vector2.LEFT:
			orient = "left"
			anims.play("walkLeft")
		Vector2.RIGHT:
			orient = "right"
			anims.play("walkRight")
		Vector2.UP:
			orient = "up"
			anims.play("walkUp")
		Vector2.DOWN:
			orient = "down"
			anims.play("walkDown")
		
	if not direction:
		anims.stop()
	if Input.is_action_pressed("k_X"):
		#how to reduce coupling! emit is running signal
		velocity *= 2
	if Input.is_action_just_released("k_Enter"):
		print("actiavte menu")
		
		
		
	
	if direction:
		if move_and_slide():
			var col:KinematicCollision2D  = get_last_slide_collision()
			var collider = col.get_collider()
			#print(collider.get_meta_list())
			if collider.has_meta("newArea"):
				print("great")
				var root = get_parent().get_parent()
				root.loadNewLevel(collider.get_meta("newArea"))
				#lol reload self
				self._ready()
				
				
				
				#export or signal?!??!
				#should emit new area signal here.
			
				
