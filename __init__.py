import sys, os.path

paths = [
    '/',
]

for path in paths:
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '/'))
    sys.path.append(directory)