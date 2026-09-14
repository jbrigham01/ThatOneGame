extends Node2D
class_name battleManager

var player: battlePlayer
var battlefield: battleField
var enemy: battleEnemy
var playerMove = null
var enemyMove = null




var dir = {
	"up": Vector2i(0, -1),
	"down": Vector2i(0, 1),
	"left": Vector2i(-1, 0),
	"right": Vector2i(1, 0)
}

func updateEnemyStrategyInfo(enemy: battleEnemy):
	enemy.playerinFront = player.position[0] < enemy.position[0]
	enemy.playerBehind = player.position[0] > enemy.position[0]
	enemy.playerAbove  = player.position[1] < enemy.position[1]
	enemy.playerBelow  = player.position[1] > enemy.position[1]
	enemy.distanceFromPlayer = abs(player.position[0] - enemy.position[1])
	


func _ready() -> void:
	player = get_node("Player")
	enemy = get_node("Enemy")
	battlefield = %battleField
	var battleFinished = false
	initBattle(player, enemy)
	#while not battleFinished:
	#	updateBattleField()
	#	updateEnemyStrategyInfo(enemy)
	#	player.strategy()
	#	enemy.strategy()
		
		#updateInfo
	#	pass
		
	
	# Replace with function body.

func checkValidAndAssign(player, newPos):
	if newPos[0] > battlefield.width || newPos[0] < 0 or newPos[1] > battlefield.height or newPos[1] < 0:
		return
	#are we zero indexing?
	var tile = battlefield.tiles[newPos[0]-1][newPos[1]-1]
	if tile.isBroken or tile.isOccupied:
		return
	player.currentPos = newPos
	moveCharacter(player)
	
	

func checkForEvent():
	pass
	
	
func handleDamageTiles():
	for x in battlefield.tiles:
		for tile in x:
			if tile.damage:
				tile.damageTick()
func updateBattleField():
	handleDamageTiles()
	var pNewPos = null
	var eNewPos = null
	if playerMove:
		pNewPos = player.currentPos + dir[playerMove]
	if enemyMove:
		eNewPos = enemy.currentPos + dir[enemyMove]
	if pNewPos == eNewPos:
		pNewPos = player.currentPos #cant collide with enemy
	if pNewPos:
		checkValidAndAssign(player, pNewPos)
		playerMove = null
	if eNewPos:
		checkValidAndAssign(enemy, eNewPos)
		enemyMove = null
	
		
	
		
	
	
	
	
	
func initBattle(player: Node, enemy: Node) -> void:
	print(player.currentPos)
	player.position = battlefield.tiles[player.currentPos[0]-1][player.currentPos[1]-1].position
	player.position.y -= (player.get_rect().size.y * 1.5)
	
func moveCharacter(player: Node):
	#need to set character
	player.position = battlefield.tiles[player.currentPos[0]-1][player.currentPos[1]-1].position
	player.position.y -= (player.get_rect().size.y * 1.5)
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	checkForEvent()
	updateBattleField()
	pass
