from Experiments.firstToast.generator import Object


class Constraint:
	def __init__(self, object: Object = None, type: str = ""):
		self.object = object
		self.type = type

	def __str__(self):
		return object + " " + type
