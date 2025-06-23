import joblib

mind = joblib.load("marks_predictor.model")

hrs = float(input("Enter number of hours of Study: "))

finalscore = mind.predict([[hrs]])
print("Predicted Marks: ", finalscore)