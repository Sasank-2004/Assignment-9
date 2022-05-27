def f(p):
    return (1*(1/18.0)) + ((1-p)*(17/18.0))
p=18/35.0
e=10**(-8)
if(abs(f(p)-p)<e) :  print("Correct")