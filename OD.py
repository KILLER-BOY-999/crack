import os, sys
try:
    __import__("od").menu()
except Exception as e:
    exit(str(e))
