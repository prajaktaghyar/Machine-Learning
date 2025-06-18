import tkinter as tk
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Create GUI
def predict_species():
    sl = float(entry1.get())
    sw = float(entry2.get())
    pl = float(entry3.get())
    pw = float(entry4.get())
    prediction = model.predict([[sl, sw, pl, pw]])
    result_label.config(text=f"Predicted Species: {iris.target_names[prediction][0]}")

root = tk.Tk()
root.title("Iris Flower Prediction")
root.geometry("300x300")

tk.Label(root, text="Sepal Length").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Sepal Width").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Petal Length").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Label(root, text="Petal Width").pack()
entry4 = tk.Entry(root)
entry4.pack()

tk.Button(root, text="Predict", command=predict_species).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

