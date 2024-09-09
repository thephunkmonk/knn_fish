from model import PredictiveModel
from data_handler import DataHandler

def main():
    model = PredictiveModel()
    data_handler = DataHandler()

    while True:
        print("\nEnter length and weight data for prediction (or type 'exit' to quit):")
        length = input("Length: ")
        weight = input("Weight: ")
        
        if length == 'exit' or weight == 'exit':
            break
        
        try:
            length = float(length)
            weight = float(weight)
        except ValueError:
            print("Please enter valid numbers.")
            continue
        
        # Make a prediction
        predicted_value = model.predict(length, weight)
        print(f"Predicted label: {predicted_value}")
        
        # Ask for user feedback
        correct = input("Is the prediction correct? (yes/no): ").lower()
        
        if correct == 'no':
                correct_label = input("Enter the correct label (sea bream/smelt): ").strip().lower()
                model.update_model(length, weight, correct_label)
        
        # Save data to persist between sessions
        data_handler.save_data(model.get_training_data())
        
if __name__ == "__main__":
    main()
