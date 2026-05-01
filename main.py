from src.data_preprocessing import load_data, preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate
from src.evaluate_model import feature_importance

# Load dataset
df = load_data("data/advertising.csv")

# Preprocess
X, y = preprocess_data(df)

# Train
model, X_test, y_test = train_model(X, y)

# Evaluate
evaluate(model, X_test, y_test)

feature_importance(model, X)