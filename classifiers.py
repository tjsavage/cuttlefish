import random 

class BaseClassifier(object):
	def friends(self, pair):
		raise Exception("should have implemented this")

class RandomClassifier(object):
	def friends(self, pair):
		return random.random() > 0.5


classifiers = {
	"random": RandomClassifier()
}

def get(classifier_name):
	return classifiers[classifier_name]