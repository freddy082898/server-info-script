Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import psutil
... 
... # Get the memory usage information
... memory = psutil.virtual_memory()
... 
... # Print the memory usage details
... print("Total Memory: {:.2f} GB".format(memory.total / (1024 ** 3)))
... print("Available Memory: {:.2f} GB".format(memory.available / (1024 ** 3)))
... print("Used Memory: {:.2f} GB".format(memory.available / (1024 ** 3)))
... print("Memory Percent: {:.2f}%".format(memory.percent))
