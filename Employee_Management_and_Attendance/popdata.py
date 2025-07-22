import pandas as pd
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

from dbengine import get_connection
conn = get_connection()
cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("SELECT 1 FROM Employees WHERE employee_id = %s", (row["EmployeeNumber"],))
    if cur.fetchone():
        continue

    cur.execute('''
        INSERT INTO Employees (
            employee_id, name, age, department, job_role, education,
            gender, marital_status, years_at_company, monthly_income, over_time, attrition
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        row["EmployeeNumber"], "Emp_" + str(row["EmployeeNumber"]), row["Age"], row["Department"],
        row["JobRole"], row["Education"], row["Gender"], row["MaritalStatus"],
        row["YearsAtCompany"], row["MonthlyIncome"], row["OverTime"], row["Attrition"]
    ))

conn.commit()
conn.close()
print("✅ Employee data populated in PostgreSQL.")