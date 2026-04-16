class Head:
	def __init__(self):
		self.eyes = 2
		self.ears = 2
		self.nose = 1
		self.mounth = 1

class Torso:
	def __init__(self):
		self.head = Head()
		self.right_arm = Arm("right")
		self.left_arm = Arm("left")
		
class Arm:
	def __init__(self, side):
		self.side = side
		self.left_hand = Hand("left")
		self.right_hand = Hand("right")

class Hand:
	def __init__(self,side):
		self.fingers = 5
		self.side = side

class Leg:
	def __init__(self,side):
		self.side = side
		self.right_feet = Feet("right")
		self.left_feet = Feet("left")
	
class Feet:
	def __init__(self,side):
		self.side = side
		self.toes = 5

class Human:
	def __init__(self,name):
		self.name = name
		self.torso = Torso()
		self.left_leg = Leg("left")
		self.right_leg = Leg("right")
	
#Main
person = Human("Didier")
print(f"Name:{person.name}")
print(f"Eyes:{person.torso.head.eyes}")
print(f"Fingers Left Hand:{person.torso.left_arm.left_hand.fingers}")
print(f"Toes Right Foot:{person.right_leg.right_feet.toes}")
print(f"Right Foot:{person.right_leg.right_feet.side}")