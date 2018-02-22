#第一种实现方式  复用性太差
def fab1(max): 
   n, a, b = 0, 0, 1 
   while n < max: 
       print(b) 
       a, b = b, a + b 
       n = n + 1

#第二种实现方式 max过大时，耗内存
def fab2(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L

#第三种方式 利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class 太过繁琐
class fab3(object): 
 
   def __init__(self, max): 
       self.max = max 
       self.n, self.a, self.b = 0, 0, 1 
 
   def __iter__(self): 
       return self 
 
   def next(self): 
       if self.n < self.max: 
           r = self.b 
           self.a, self.b = self.b, self.a + self.b 
           self.n = self.n + 1 
           return r 
       raise StopIteration()

#第四种实现方式
def fab4(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b
        a, b = b, a + b 
        n = n + 1 

#yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
#在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
#而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。

for n in fab4(5): 
    print(n)


