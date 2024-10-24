#CH6 14.
#試設計一函數add_n(lst,n)
#可將串列lst裡的每一個元素加上n，並傳回加上n之後的串列
#如果沒有傳入n，則n預設為0


lst=[10,20,30,40,50]
n=5

def add_n(lst,n):
  return [i+n for i in lst]

print(add_n(lst,n))