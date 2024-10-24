import random
field_size=11

def mod(a,b):
    return (a%b +b)%b
def random_coefficients(no_of_variables):
    polynomial=[]
    for i in range(no_of_variables):
        polynomial.append(random.randint(1,field_size-1))
    return polynomial
class UOV:
    def __init__(self,no_of_variables,no_of_equations):
        self.no_of_variables=no_of_variables
        self.no_of_equations=no_of_equations
        self.private_key=[]
        self.public_key=[]
        self.generate_keys()
    def generate_keys(self):
        polynomial=[]
        for i in range(self.no_of_equations):
            polynomial=(random_coefficients(self.no_of_variables))
            self.private_key.append(polynomial)
        for i in self.private_key:
            mod_equation=[mod(coef,field_size) for coef in i]
            self.public_key.append(mod_equation)
    def sign(self,message):
        signature=[]
        for i in range(self.no_of_equations):
            result=0
            for j in range(self.no_of_variables):
                result=result+(message[j]*self.private_key[i][j])
            result=mod(result,field_size)
            signature.append(result)
        return signature
    def verify(self,signature,message):
        for index,equation in enumerate(self.public_key):
            result=0
            for i in range(self.no_of_variables):
                result=result+(message[i]*equation[i])
            result=mod(result,field_size)
            if result !=signature[index]:
                return False
        return True
no_of_variables=3
no_of_equations=3
uov=UOV(no_of_variables,no_of_equations)
message=[1,2,3]
signature =uov.sign(message)
print(signature)
print(uov.verify(signature,message))




