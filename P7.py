#CH7 7.
#(a) 試定義一個函數salary(),可接收工作時數hr和索引bonus,並以payRate裡索引為bonus的值做為給付比率,然後計算應給付的金額(取整數)。
#例如，如果baseSalary=160, hr=10, bouns=1,則給付金額為 160x10X1.2=1920 其中1.2是串列payRate中,索引為bonus=1的元素。
#(b) 試定義一個類別函數set_payRate(),可以接收一個串列new_payRate,然後將類別屬性payRate 修改為new_payRate。
#(c) 試定義一個靜態函數estimate(),可輸入基本時薪bs、工作時數hr和給付比例rate，然後估算可獲得的薪資(取整數)。
#例如estimate(160,10,1.25)的計算結果為2000。


#設Employee 類別定義如下,其中的類別屬性 payRate 是員工(Employee)時薪給付的比率(為一串列),baseSalary 是員工的基本時薪:
class Employee:
  payRate=[1, 1.2, 1.5]   #給付的比率
  def __init__(self,base):
    self.baseSalary=base


  #(a)
  def salary(self,hr,bonus):
    return int(self.baseSalary*hr*self.payRate[bonus])


  @classmethod
  def set_payRate(cls,new_payRate):
    cls.payRate=new_payRate
  

  @staticmethod
  def estimate(bs,hr,rate):
    return int(bs*hr*rate)


tom=Employee(160)
print(tom.salary(10,1)) # 1920
Employee.set_payRate([1,1.3,1.5])
print(tom.salary(10,1)) # 2080
print(Employee.estimate(160,10,1.25)) # 2000