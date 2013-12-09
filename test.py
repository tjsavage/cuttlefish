import sys
import classifiers
import models
import csv
import random

def test(classifier, pairs):
	total = len(pairs)
	correct = 0

	for pair in pairs:
		guess = classifier.friends(pair)
		if guess == pair.are_friends():
			correct += 1

	return 1.0 * correct / total

def sample(population, percent):
	pop_size = len(population)
	sample_size = int(percent * pop_size)
	return random.sample(population, sample_size)


if __name__ == '__main__':
	classifier_name = sys.argv[1]
	classifier = classifiers.get(classifier_name)
	pairs = models.read_pairs("training_data.csv")
	testing_sample = sample(pairs, 0.5)

	percent = test(classifier, testing_sample)
	print "Accuracy: %f" % percent