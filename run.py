import os
import subprocess
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))

exe_path = os.path.join(base_dir, "dist", "main.exe")

if not os.path.isfile(exe_path):
    print(f"❌ File main.exe tidak ditemukan di {exe_path}")
    sys.exit(1)
    
try:
    subprocess.run([exe_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"❌ Gagal menjalankan main.exe: {e}")
    sys.exit(e.returncode)
