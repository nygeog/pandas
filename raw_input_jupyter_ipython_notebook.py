# Python 3 compat
import sys
if sys.version_info[0] >= 3:
    raw_input = input

name = raw_input("What is your name? ")
name

#https://github.com/ipython/ipython-in-depth/blob/master/examples/IPython%20Kernel/Raw%20Input%20in%20the%20Notebook.ipynb