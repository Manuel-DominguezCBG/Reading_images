"""
A script that imports all of the modules we will need. If this script says you don't have something, you will need to install it using the given command.
"""

try:
    import numpy
except:
    print("Numpy was not found.")
    print("Install it by doing: python -m pip install numpy ")

try:
    import matplotlib
except:
    print("Matplotlib not found, please run:")
    print("python -m pip install matplotlib")

try:
    import jupyter
except:
    print("jupyter not found, please run:")
    print("python -m pip install jupyter")


try:
    import pytesseract
except:
    print("jupyter not found, please run:")
    print("python -m pip install pytesseractr")

try:
    import PIL
except:
    print("jupyter not found, please run:")
    print("python -m pip install Pillow")


