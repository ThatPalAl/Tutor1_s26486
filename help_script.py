# help_script.py
import sys

def action():
    print("Help flag script")

if '--help' in sys.argv:
    action()
else:
    print("Script executed without the --help flag")
