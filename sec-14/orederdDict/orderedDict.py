from collections import OrderedDict

d = {"a": 1}
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = 5
for k,v in d.items():
      print(k,v)

d2 = OrderedDict()
d2["a"] = 1
d2["b"] = 2
d2["c"] = 3
d2["d"] = 4
d2["e"] = 5

for k,v in d2.items():
      print(k,v)