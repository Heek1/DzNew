class Math:
    @staticmethod
    def plus(num1,num2):
        return num1 + num2

    @staticmethod
    def minus(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2

num1=int(input("Enter first number:\t"))
num2=int(input("Enter sec number:\t"))
print(Math.plus(num1,num2))
print(Math.minus(num1,num2))
print(Math.multiply(num1,num2))
print(Math.divide(num1,num2))



