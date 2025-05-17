import subprocess
import sys

def install_with_pip(package):
    try:
        print(f"🔧 Installing: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")

# Optional: Skip upgrading pip if it's causing issues
# print("🔧 Skipping pip upgrade to avoid timeout issues")

required_packages = [
    "uv",         # fast package installer (optional)c
    "streamlit",  # for building web apps
    "jupyterlab", # for interactive notebooks
    "click"       # example dependency already installed
]

for pkg in required_packages:
    install_with_pip(pkg)

print("✅ All packages attempted.")
