import csv

columns = [
	"f_gender", 
	"f_age", 
	"f_height", 
	"f_shoe_size*", 
	"f_number_of_pets*", 
	"f_platinum_albums*", 
	"f_weekly_workouts*", 
	"f_number_of_siblings*", 
	"f_pokemon_collected*", 
	"f_facebook_friends_count", 
	"f_facebook_photos_count", 
	"m_gender", 
	"m_age", 
	"m_height", 
	"m_shoe_size*", 
	"m_number_of_pets*", 
	"m_platinum_albums*", 
	"m_weekly_workouts*", 
	"m_number_of_siblings*", 
	"m_pokemon_collected*", 
	"m_facebook_friends_count", 
	"m_facebook_photos_count", 
	"members_became_friends"
]

class Pair(object):
	def __init__(self, data_vector):
		self.data_vector = data_vector
		self.data = {}
		for index, item in enumerate(self.data_vector):
			self.data[columns[index]] = item

	def are_friends(self):
		return self.data["members_became_friends"] == "TRUE"


def read_pairs(filename):
	pairs = []
	with open(filename, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			pairs.append(Pair(row))
	return pairs