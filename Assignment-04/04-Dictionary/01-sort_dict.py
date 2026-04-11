d = {"b": 2, "a": 1, "c": 3}
a = dict(sorted(d.items(), key=lambda item: item[0]))
de = dict(sorted(d.items(), key=lambda item: item[0], reverse=True))
print("Ascending order: ", a)
print("Descending order: ", de)