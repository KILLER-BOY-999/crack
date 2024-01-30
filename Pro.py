import os, sys
try:
    __import__("pro").main()
except Exception as e:
    exit(str(e))
