import codecs, json
import numpy as np
import sys


a = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])

b = a.tolist()
file_path = sys.path[0] + "/config1.json"
json.dump(b, codecs.open(file_path, "w", encoding= "utf-8"), separators= (",",":"), sort_keys= True, indent=4)



x = np.random.randint(2, size=(50,50))

y = x.tolist()
file_path = sys.path[0] + "/config2.json"
json.dump(y, codecs.open(file_path, "w", encoding= "utf-8"), separators= (",",":"), sort_keys= True, indent=4)