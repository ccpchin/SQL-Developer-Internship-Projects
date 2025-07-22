import subprocess

scripts = [
    "init.py",
    "popdb.py",
    "audit.py",
    "blo.py",
    "querylogic.py",
    "model.py",
    "summary.py"
]

print("🚀 Starting Airline Reservation System project setup...\n")

for script in scripts:
    print(f"▶️ Running {script}...")
    try:
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script}: {e}")
    print("")

print("✅ All scripts executed.")
print("ℹ️ Note: blo.py and querylogic.py define functions but do not perform visible actions unless used interactively.")