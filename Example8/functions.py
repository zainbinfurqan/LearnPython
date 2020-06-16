
def add():  # function with no args
    print("hye i am function")


# call function
# add()


def add_(value_1):  # function with one arg
    print(value_1+2)


# add_(2)


def operationsWithparams(value_1, value_2):  # function with 2 arg
    print(value_1+value_2)
    print(value_1-value_2)
    print(value_1*value_2)


# operationsWithparams(3, 4)


def funWithMultiParam(*params):
    print(params[0] + params[1])


# funWithMultiParam(1, 2)


def funWithPair(name, age):
    print('name is', name)
    print('age is', age)


# funWithPair(name='zain', age=20)


def funWithmultiPairs(**multiObj):
    print(multiObj)


# funWithmultiPairs(name="zain", age=24)

def funWithArry(array):
    for data in array:
        print(data)


list1 = [{"name": 'zain'}, {"name": 'faraz'}, {"name": 'omer'}]
# list2 =
funWithArry(list1)


def funcReturn(num1, num2):
    return num1+num2


result = funcReturn(1, 2)
# print(result)


# def tri_recursion(k):
#   if(k > 0):
#     print(k)
#     result = k + tri_recursion(k - 1)
#     print(result,"result",k)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# --------lamda function------------
def high_ord_func(x, func): return x + func(x)


high_ord_func(2, lambda x: x * x)


def div_zero(x): return x / 0


div_zero(2)
