import pprint

dict_ = []
for i in range(16):
    dict_.append({'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)})

pprint.pprint(dict_)