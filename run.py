import os
import subprocess
import sys

# Dapatkan direktori saat ini (folder script ini)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Path lengkap ke main.exe di dalam folder dist/
exe_path = os.path.join(base_dir, "dist", "main.exe")

# Cek apakah file main.exe ada
if not os.path.isfile(exe_path):
    print(f"❌ File main.exe tidak ditemukan di {exe_path}")
    sys.exit(1)

# Jalankan main.exe
try:
    subprocess.run([exe_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"❌ Gagal menjalankan main.exe: {e}")
    sys.exit(e.returncode)
