#CH7 5.試接續上題的Sphere類別,然後作答下列各題
#(a)在Sphere類別裡定義repr()函數,當Sphere 類別的物件被查詢時,會顯示出"Sphere object,rad=r"字串。其中r為rad屬性的值。
#(b)在Sphere類別裡定義str()函數,當以print()函數印出 Sphere 類別的的物件時,會顯示出“Sphere object,rad=r,volume =v, surface_area=s”,其中v和s分別為物件的體積和表面積,並顯示到小數點以下兩位。

import math

class Sphere:
    def __init__(self, r):
        self.rad = r

    #(a)
    def __repr__(self):
        return f"Sphere object,rad={self.rad}"
    
    #(b)
    def __str__(self):
        return f"Sphere object,rad={self.rad},volume={(4/3) * math.pi * self.rad**3:.2f}, surface_area={4 * math.pi * self.rad**2:.2f}"


s1 = Sphere(2)
print(s1.__repr__())
print(s1.__str__())