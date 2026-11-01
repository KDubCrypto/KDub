"""Rebuild Kyle White Links. Usage: python3 deploy.py, then commit and push links/index.html."""
import os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))
r = subprocess.run([sys.executable, os.path.join(D, 'build.py')])
sys.exit(r.returncode)
