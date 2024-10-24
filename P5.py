#CH6 33.
#試撰寫一個產生器gen(n)
#可以產生所有小於等於n的整數中
#可以被3整除但不能被5整除的數。


def gen(n):
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 != 0:
      yield i


for x in gen(10):
  print(x)
