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
		
class Hand:
	def __init__(self,side):
		self.fingers = 5
		self.side = side

class Arm:
	def __init__(self, side):
		self.side = side

class Leg:
	def __init__(self,side):
		self.side = side
	
class Feet:
	def __init__(self,side):
		self.side = side
		self.toes = 5

class Human:
	def __init__(self,name):
		self.name = name
		self.head = Head()
		self.torso = Torso()
		self.left_arm = Arm("left")
		self.right_arm = Arm("right")
		self.left_hand = Hand("left")
		self.right_hand = Hand("right")
		self.left_leg = Leg("left")
		self.right_leg = Leg("right")
		self.left_foot = Feet("left")
		self.right_foot = Feet("right")
	
#Main
person = Human("Didier")
print(f"Name:{person.name}")
print(f"Eyes:{person.head.eyes}")
print(f"Fingers Left Hand:{person.left_hand.fingers}")
print(f"Toes Right Foot:{person.right_foot.toes}")
print(f"Foot:{person.right_foot.side}")