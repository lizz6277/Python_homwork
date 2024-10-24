#CH6 27.
#試撰寫lambda 函數,可以接收一個整數串列lst
#傳回值為這個串列裡,介於0到255之間的數
#例如lst=[-3,6,100,300],則傳回[6,100]。


lst = [-3, 6, 100, 300]

result = list(filter((lambda x: 0 <= x <= 255), lst))

print(result)