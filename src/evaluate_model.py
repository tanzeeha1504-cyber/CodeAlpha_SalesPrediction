from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)

    print("MAE:", mean_absolute_error(y_test, predictions))
    print("MSE:", mean_squared_error(y_test, predictions))
    print("R2 Score:", r2_score(y_test, predictions))

    # Plot Actual vs Predicted
    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual vs Predicted Sales")
    plt.savefig("outputs/plots/sales_vs_ads.png")
    plt.show()

def feature_importance(model, X):
    importance = pd.Series(model.coef_, index=X.columns)
    print("\nFeature Impact:\n", importance)

    importance.plot(kind='bar', title="Advertising Impact on Sales")
    plt.savefig("outputs/plots/feature_importance.png")
    plt.show()