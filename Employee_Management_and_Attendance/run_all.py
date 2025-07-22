# run_all.py

import subprocess

scripts = [
    "schema.py",
    "popdata.py",
    "attendance.py",
    "report.py",
    "totalhours.py",
    "model.py",
    "query.py"
]

print("🚀 Running Employee Management System setup...\n")

for script in scripts:
    print(f"▶️ Running {script}...")
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script}: {e}")
    print("")

print("✅ All core modules executed.")
print("ℹ️ Note: test.py is intentionally detached. Run it separately to validate system integrity.")