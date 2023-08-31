from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

def get_user_input():
    # Get sepal and petal dimensions as input from the user
    print("Enter the dimensions of the new flower:")
    sepal_length = float(input("Sepal Length: "))
    sepal_width = float(input("Sepal Width: "))
    petal_length = float(input("Petal Length: "))
    petal_width = float(input("Petal Width: "))
    return [[sepal_length, sepal_width, petal_length, petal_width]]

def main():
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Get user input for the new flower
    new_flower = get_user_input()

    # Create and train the Decision Tree classifier
    dt_classifier = DecisionTreeClassifier().fit(X, y)

    # Predict the species of the new flower
    prediction = dt_classifier.predict(new_flower)

    species_mapping = ["setosa", "versicolor", "virginica"]
    predicted_species = species_mapping[prediction[0]]

    print(f"The species of the new flower is: {predicted_species}")

if __name__ == "__main__":
    main()
