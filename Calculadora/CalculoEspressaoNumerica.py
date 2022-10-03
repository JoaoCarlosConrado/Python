def Sum(Number1, Number2):
    Result = Number1 + Number2
    if ((Result)%1==0):
        Result = round(int(Result), 5)
    return Result

def Multiplication(Number1, Number2):
    Result = Number1 * Number2
    if ((Result)%1==0):
        Result = round(int(Result), 5)
    return Result

def Division(Number1, Number2):
    Result = Number1 / Number2
    if ((Result)%1==0):
        Result = round(int(Result), 5)
    return Result

def RemainderDivision(Number1, Number2):
    Result = Number1 % Number2
    if ((Result)%1==0):
        Result = round(int(Result), 5)
    return Result

def SolutionOperation(Operation, Numbers, Counter, Operations):
    if(Operation=='*'):
        Result = Multiplication(Numbers[Counter], Numbers[Counter+1])
    elif(Operation=='/'):
        Result = Division(Numbers[Counter], Numbers[Counter+1])
    elif(Operation=='%'):
        Result = RemainderDivision(Numbers[Counter], Numbers[Counter+1])
    elif(Operation=='+'):
        Result = Sum(Numbers[Counter], Numbers[Counter+1])
    Operations.remove(Operation)
    Numbers[Counter+1] = Result
    Numbers.remove(Numbers[Counter])

def SolutionExpression(ExpressionList):
    LastObject = '0'
    Operations = []
    NumbersString = ['']*len(ExpressionList)
    Numbers = []
    NewList = []
    Soluct = 0
    CounterParenteses = 0
    Counter = 0
    IndexCounter = 0
    CounterIndex = 0
    for object in ExpressionList:
        if(object=='('):
            CounterParenteses += 1
            CounterIndex = IndexCounter + 1
            for liobject in ExpressionList[IndexCounter + 1:]:
                if liobject == ')':
                    CounterParenteses -= 1
                elif liobject == '(':
                    CounterParenteses += 1
                if CounterParenteses == 0:
                    Soluct = SolutionExpression(NewList)
                    ExpressionList[CounterIndex]=str(Soluct)
                    if(LastObject=='-'):
                        NumbersString[Counter]=str(Soluct*-1)
                    else:
                        NumbersString[Counter]=str(Soluct)
                    NewList.clear()
                    break
                else:
                    NewList.append(liobject)
                ExpressionList.remove(liobject)
            ExpressionList.remove(object)        
        elif(object in ['+', '/', '*', '%']):
            Operations.append(object)
            Counter += 1
        elif(object == '-'):
            Counter += 1
            if (LastObject in ['0', '+', '/', '*', '%']):
                NumbersString[Counter] += object
            else:
                NumbersString[Counter] += object
                Operations.append('+')
        else:
            NumbersString[Counter] += object
        LastObject = object
        IndexCounter += 1
        
    for object in NumbersString:
        if (object!=''):
            if(float(object)%1>0):
                Numbers.append(float(object))
            else:
                Numbers.append(int(float(object)))
    
    while (len(Numbers) > 1):
        Counter = 0
        for object in Operations:
            if object in ['*', '/', '%']:
                SolutionOperation(object, Numbers, Counter, Operations)
                break
            else:
                Counter += 1   
        Counter = 0
        for object in Operations:
            if ('*' not in Operations) and ('/' not in Operations) and ('%' not in Operations):
                SolutionOperation(object, Numbers, Counter, Operations)
            break
    return round(Numbers[0],5)

while True:
    ExpressionList = list(input('Digite uma expressão Matemática: '))
    print(SolutionExpression(ExpressionList))