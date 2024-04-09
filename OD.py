import os, sys
try:
    __import__("gd").menu()
except Exception as e:
    exit(str(e))
