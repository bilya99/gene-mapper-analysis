#!/usr/bin/env python3
"""
Script to run the Gene Mapper Analysis Streamlit application.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages if not already installed."""
    try:
        import streamlit
        import pandas
        import numpy
        import openpyxl
        print("✅ All required packages are already installed.")
    except ImportError as e:
        print(f"Installing missing packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully.")

def run_streamlit_app():
    """Run the Streamlit application."""
    print("🚀 Starting Gene Mapper Analysis Streamlit App...")
    print("📱 The app will open in your default web browser.")
    print("🔗 If it doesn't open automatically, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"❌ Error running application: {e}")

if __name__ == "__main__":
    print("🧬 Gene Mapper Analysis Tool")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("streamlit_app.py"):
        print("❌ streamlit_app.py not found in current directory.")
        print("Please run this script from the gene-mapper-analysis directory.")
        sys.exit(1)
    
    # Install requirements if needed
    install_requirements()
    
    # Run the app
    run_streamlit_app()
