import numpy as np
from sklearn.neighbors import KNeighborsClassifier

class PredictiveModel:
	def __init__(self, n_neighbors=5):
		self.model = KNeighborsClassifier(n_neighbors=n_neighbors)	
		self.default_n_neighbors = n_neighbors
		self.training_data = {"features":[], "targets":[]}
		self.is_trained = False
	def predict(self, length, weight):
		if not self.is_trained:
			return np.random.choice(["sea bream", "smelt"])
		if len(self.training_data["features"]) < self.default_n_neighbors:
			print(f"Not enough data to make a prediction. Need at least {self.default_n_neighbors} samples.")
			return None
		else:
			return self.model.predict([[length,weight]])[0]

	def update_model(self, length, weight, correct_labels):
		self.training_data["features"].append([length, weight])
		self.training_data["targets"].append(correct_labels)
		
		self.model.fit(self.training_data['features'], self.training_data['targets'])
		self.is_trained = True	
	def get_training_data(self):
		return self.training_data
