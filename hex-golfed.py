d="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def t(s,b):
 s=s.strip().upper();v=0;p=1
 for c in s[::-1]:
  if c not in d[:b]:raise ValueError(f"'{c}' is not valid for base {b}")
  v+=d.index(c)*p;p*=b
 return v
def f(n,b):
 if n==0:return"0"
 r=""
 while n:
  n,rem=divmod(n,b);r=d[rem]+r
 return r
def main():
 print("Welcome to The Hexorcist. THE POWER OF MATH COMPELS YOU!\n")
 n=input("Enter the number you want to convert: ").strip()
 o=int(input("Enter the number's CURRENT base (2-36): ").strip())
 tb=int(input("Enter the NEW base you want (2-36): ").strip())
 print("\n...calculating with sticks and stones...\n")
 try:
  dec=t(n,o);cv=f(dec,tb)
  print(f"'{n}' (Base-{o}) is '{cv}' (Base-{tb}).")
 except ValueError as e:
  print("Error:",e)
if __name__=="__main__":main()
