extends CharacterBody2D


const SPEED = 300.0
const JUMP_VELOCITY = -400.0

var orient = "down"



func _physics_process(delta: float) -> void:
	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction = Input.get_vector("k_Left", "k_Right","k_Up","k_Down" )
	velocity = direction * 600
	match direction:
		"k_Left":
			orient = "left"
		"k_Right":
			orient = "right"
		"K_Up":
			orient = "up"
		"K_Down":
			orient = "down"
	
	if Input.is_action_pressed("k_X"):
		velocity *= 2
	

	move_and_slide()
