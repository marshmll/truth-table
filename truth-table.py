from os import system, name

def main():
    print("***TABELA VERDADE***")

    amountOfVariables = int(input('Digite a quantidade de variáveis para calcular a tabela verdade: '))
    truthTable = []

    connectives = {
        1: "and",
        2: "or",
        3: "implication",
        4: "biconditional",
    }

    match amountOfVariables:
        case 1:
            truthTable = [True, False]
        case 2:
            print("CONECTIVOS\n")
            print("[1] - ∧")
            print("[2] - v")
            print("[3] - →")
            print("[4] - ↔ \n")

            connectiveNumber = int(input("Digite o conectivo que você deseja (A _ B): "))

            connective = ''

            if connectiveNumber >= 1 and connectiveNumber <= 4:
                connective = connectives[connectiveNumber]
            
            for i in range (0, 2 ** amountOfVariables):
                
                if i < (2 ** amountOfVariables) / 2:
                    A = True;
                else:
                    A = False
                
                if i % 2 == 0:
                    B = True
                else:
                    B = False
                
                result = calculateLogicResult(A, B, connective)
                truthTable.append(result)
        
        case 3:
            print("CONECTIVOS\n")
            print("[1] - ∧")
            print("[2] - v")
            print("[3] - →")
            print("[4] - ↔ \n")

            firstConnectiveNumber = int(input("Digite o primeiro conectivo que você deseja (A _ B): "))
            firstConnective = ''

            if firstConnectiveNumber >= 1 and firstConnectiveNumber <= 4:
                firstConnective = connectives[firstConnectiveNumber]
            
            secondConnectiveNumber = int(input("Digite o segundo conectivo que você deseja (...) _ C: "))
            secondConnective = ''

            if secondConnectiveNumber >= 1 and secondConnectiveNumber <= 4:
                secondConnective = connectives[secondConnectiveNumber]
            
            for i in range (0, 2 ** amountOfVariables):
                
                if i < (2 ** amountOfVariables) / 2:
                    A = True
                else:
                    A = False

                if i % 4 == 0 or i % 4 == 1:
                    B = True
                else:
                    B = False
                
                if i % 2 == 0:
                    C = True
                else:
                    C = False
                
                firstResult = calculateLogicResult(A, B, firstConnective)
                finalResult = calculateLogicResult(firstResult, C, secondConnective)

                truthTable.append(finalResult)
                
    system("cls" if name == 'nt' else "clear")
    print("TABELA VERDADE\n")
    printTruthTable(truthTable)                

def calculateLogicResult(A, B, connective):
    if connective == 'and':
        return A and B
    elif connective == 'or':
        return A or B
    elif connective == 'implication':
        return (not A) or B
    elif connective == 'biconditional':
        return (not A or B) and (not B or A)
    
def printTruthTable(table):
    for row in table:
        print(" " * 5, end="")
        print("V" if row == True else "F")

main()