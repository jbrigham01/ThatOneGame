extends Node

#Single Responsibility Principle (each class should do ONE thing
#Open/Close principle (each class should open for extension, but closed for modficionation)
#Liskov substituion principle (each subclass should be treatable as super class)
#Inteagration segregation principles? lol idk
#Dependency inversino (dont overrely on dependencies)

class playerData:
	#game will hold all the relevant player data.
	#This will be loaded from save files.
	var items = []
	var party = []
	var player = []
	var stats = []
	var currentArea = ""

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	print("Loaded player info!")
	pass # Replace with function body.
