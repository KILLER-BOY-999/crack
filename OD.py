import os, sys
try:
    __import__("odd").menu()
except Exception as e:
    exit(str(e))
