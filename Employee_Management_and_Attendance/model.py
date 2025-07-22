import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
le = LabelEncoder()

df['Attrition'] = le.fit_transform(df['Attrition'])
df['OverTime'] = le.fit_transform(df['OverTime'])
df['BusinessTravel'] = le.fit_transform(df['BusinessTravel'])
df['Gender'] = le.fit_transform(df['Gender'])
df['JobRole'] = le.fit_transform(df['JobRole'])
df['MaritalStatus'] = le.fit_transform(df['MaritalStatus'])

features = ['Age', 'MonthlyIncome', 'JobLevel', 'DistanceFromHome', 'OverTime', 'YearsAtCompany']
X = df[features]
y = df['Attrition']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("🧠 Attrition Prediction Report:")
print(classification_report(y_test, y_pred))