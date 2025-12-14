# slizzai_setup_check.py
import sys
import os
import subprocess

def check_python_installation():
    print("🔍 Checking Python installation...")
    print(f"🧠 Python executable: {sys.executable}")
    print(f"🧪 Python version: {sys.version.split()[0]}")
    print("✅ Python is installed and accessible.\n")

def test_script_execution():
    print("🚀 Testing script execution...")
    try:
        subprocess.run(["python", "-c", "print('✨ SlizzAi-4 script executed successfully.')"], check=True)
        print("✅ Python scripts can run on this system.\n")
    except Exception as e:
        print(f"⚠️ Script execution failed: {e}")
        print("❌ Please check your PATH or Python installation.\n")

def check_path_association():
    print("🔗 Checking .py file association...")
    ext = ".py"
    associated = subprocess.run(["assoc", ext], capture_output=True, text=True)
    if "Python.File" in associated.stdout:
        print("✅ .py files are associated with Python.\n")
    else:
        print("⚠️ .py files may not be properly associated.")
        print("You can fix this by reinstalling Python and checking 'Add to PATH'.\n")

def run_setup_check():
    print("🌌 SlizzAi-4 Setup Ritual Initiated\n")
    check_python_installation()
    test_script_execution()
    check_path_association()
    print("🌠 Setup check complete. You are ready to summon SlizzAi-4.\n")

if __name__ == "__main__":
    run_setup_check()