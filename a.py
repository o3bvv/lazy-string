from lazy_string import LazyString


print("{}".format(LazyString(lambda x: x, '233')))
