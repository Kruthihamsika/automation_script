import subprocess
import sys
import pkg_resources

def is_installed(package):
    """Check if the package is already installed."""
    try:
        pkg_resources.get_distribution(package)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def install_package(package):
    """Try installing the package with pip."""
    if is_installed(package):
        print(f"✅ {package} is already installed.")
    else:
        try:
            print(f"🔧 Installing: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")

required_packages = [
    "uv",         # optional, newer installer
    "streamlit",  # for web apps
    "jupyterlab", # for notebooks
    "click"       # CLI utility
]

for pkg in required_packages:
    install_package(pkg)

print("✅ Done installing required packages.")
