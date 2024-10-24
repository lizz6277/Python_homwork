#CH6 17.
#試設計一函數 make_dict(keys, values)函數
#可以依據給定的keys和values來建立並傳回一個字典
#其中keys和values是長度相等的串列。若values省略則所有keys對應的values皆為0


def make_dict(keys, values=None):
  if values is None:
    return {key: 0 for key in keys}
  else:
    return {keys[i]: values[i] for i in range(len(keys))}


#例如 make_dict([0, 1, 2],[32,43,55]) 可傳回 {0:32,1:43,2:55}
print(make_dict([0, 1, 2],[32,43,55]))

#而make_dict([0,1,2]) 則傳回{0:0.1:0,2:0}
print(make_dict([0,1,2]))
