import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def load_data(path):
    """Load raw CSV data."""
    return pd.read_csv(path)

def preprocess_data(df):
    """Clean and transform the churn data."""
    df = df.copy()

    # Drop unneeded columns
    df.drop(["CustomerId", "Surname", "RowNumber"], axis=1, inplace=True)

    # Encode Gender
    df["Gender"] = LabelEncoder().fit_transform(df["Gender"])

    # One-hot encode Geography
    df = pd.get_dummies(df, columns=["Geography"], drop_first=True)

    # Separate features and target
    X = df.drop("Exited", axis=1)
    y = df["Exited"]

    # Feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

def split_data(X, y, test_size=0.2, random_state=42):
    """Split data into training and test sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    """Train a simple Random Forest classifier."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Print classification report and accuracy."""
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    #usage example inside my notebook 
from script.churn_helpers import load_data, preprocess_data, split_data, train_model, evaluate_model

    df = load_data("data/Churn_Modelling.csv")
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
