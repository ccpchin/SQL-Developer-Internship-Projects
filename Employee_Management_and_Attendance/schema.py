from dbengine import get_connection
conn = get_connection()
cur = conn.cursor()
cur.execute("""
DROP TABLE IF EXISTS Attendance CASCADE;
DROP TABLE IF EXISTS Employees CASCADE;
DROP TABLE IF EXISTS Roles CASCADE;
DROP TABLE IF EXISTS Departments CASCADE;
""")
cur.execute("""
CREATE TABLE Departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT UNIQUE NOT NULL
);
CREATE TABLE Roles (
    role_id SERIAL PRIMARY KEY,
    role_name TEXT NOT NULL,
    department_id INT REFERENCES Departments(department_id)
);
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT,
    department TEXT,
    job_role TEXT,
    education INT,
    gender TEXT,
    marital_status TEXT,
    years_at_company INT,
    monthly_income INT,
    over_time TEXT,
    attrition TEXT
);
CREATE TABLE Attendance (
    attendance_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES Employees(employee_id),
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    check_in TIME,
    check_out TIME,
    status TEXT CHECK(status IN ('Present', 'Absent', 'Late')) DEFAULT 'Present'
);
""")
cur.execute("""
CREATE OR REPLACE FUNCTION set_default_status()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.status IS NULL THEN
        NEW.status := 'Present';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
""")
cur.execute("""
DROP TRIGGER IF EXISTS trg_default_status ON Attendance;

CREATE TRIGGER trg_default_status
BEFORE INSERT ON Attendance
FOR EACH ROW
EXECUTE FUNCTION set_default_status();
""")
conn.commit()
conn.close()
print("✅ PostgreSQL schema and trigger initialized successfully.")