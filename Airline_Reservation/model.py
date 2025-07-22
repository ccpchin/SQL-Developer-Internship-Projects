import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import warnings

warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv("flights.csv")

# Data cleanup
df.dropna(subset=["Date_of_Journey", "Dep_Time", "Duration", "Total_Stops", "Price"], inplace=True)
df = df[df["Price"].apply(lambda x: isinstance(x, (int, float)))]

# Feature engineering
df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'], errors='coerce')
df['Journey_day'] = df['Date_of_Journey'].dt.day
df['Journey_month'] = df['Date_of_Journey'].dt.month
df['Dep_hour'] = pd.to_datetime(df['Dep_Time'], format='%H:%M', errors='coerce').dt.hour

# Convert Duration to minutes
def duration_to_minutes(duration):
    h, m = 0, 0
    parts = duration.strip().split()
    for part in parts:
        if 'h' in part:
            h = int(part.replace('h', ''))
        if 'm' in part:
            m = int(part.replace('m', ''))
    return h * 60 + m

df['Duration_mins'] = df['Duration'].apply(duration_to_minutes)

# Encode categorical variables
categoricals = ['Airline', 'Source', 'Destination', 'Total_Stops']
for col in categoricals:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

# Simulated label (for example purposes)
df['no_show'] = (df['Price'] < df['Price'].median()).astype(int)

# Final features
features = ['Airline', 'Source', 'Destination', 'Journey_day', 'Journey_month',
            'Dep_hour', 'Duration_mins', 'Total_Stops', 'Price']
X = df[features]
y = df['no_show']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Evaluation
acc = accuracy_score(y_test, y_pred)
print("✅ Model trained.")
print("🔍 Accuracy:", round(acc * 100, 2), "%")
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Predict on a sample
sample = X_test.iloc[[0]]
prediction = pipeline.predict(sample)[0]
print("🔮 Predicted no-show:", "Yes" if prediction else "No")