class Fraction:
    def __init__(self,Numerator,Denominator):
        self.n=Numerator
        self.d=Denominator
    def __str__(self) -> str:
        return f"{self.n}/{self.d}"
    def plus(self,other):
        new_n=self.n*other.d+other.n*self.d
        new_d=self.d*other.d
        for i in range(min(abs(new_n),abs(new_d)),1,-1):
            if not new_n%i and not new_d%i:
                new_n//=i
                new_d//=i
                break
        return Fraction(new_n,new_d)
    def minus(self,other):
        new_n=self.n*other.d-other.n*self.d
        new_d=self.d*other.d
        for i in range(min(abs(new_n),abs(new_d)),1,-1):
            if not new_n%i and not new_d%i:
                new_n//=i
                new_d//=i
                break
        return Fraction(new_n,new_d)
    def multiple(self,other):
        new_n=self.n*other.n
        new_d=self.d*other.d
        for i in range(min(abs(new_n),abs(new_d)),1,-1):
            if not new_n%i and not new_d%i:
                new_n//=i
                new_d//=i
                break
        return Fraction(new_n,new_d)
    def divide(self,other):
        new_n=self.n*other.d
        new_d=self.d*other.n
        for i in range(min(abs(new_n),abs(new_d)),1,-1):
            if not new_n%i and not new_d%i:
                new_n//=i
                new_d//=i
                break
        return Fraction(new_n,new_d)
fraction1=Fraction(1,2)
fraction2=Fraction(3,4)
sum_fraction=fraction1.plus(fraction2)
print(f"Qo'shish {sum_fraction}")

sum_fraction=fraction1.minus(fraction2)
print(f"Ayirish {sum_fraction}")

sum_fraction=fraction1.multiple(fraction2)
print(f"Ko'paytirish {sum_fraction}")

sum_fraction=fraction1.divide(fraction2)
print(f"Bo'lish {(sum_fraction)}")
    
    

