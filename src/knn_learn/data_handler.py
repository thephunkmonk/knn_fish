import json

class DataHandler:
	def __init__(self, file_path="training_data.json"):
		self.file_path = file_path

	def save_data(self,data):
		with open(self.file_path, "w") as f:
			json.dump(data, f)

	def load_data(self):
		try:
			with open(self.file_path, "r") as f:
				return json.load(f)
		except FileNotFoundError:
			return {"features":[], "targets":[]}
		
