def __getDecDigit(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
              'A', 'B', 'C', 'D', 'E', 'F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x
			
def hexToDec(hexNum):
    isNegative = False
    if hexNum[0] == '-':
        isNegative = True
        hexNum = hexNum[1:]
    decNum = 0
    power = 0
    for digit in range(len(hexNum), 0, -1):
        decNum = decNum + 16 ** power * __getDecDigit(hexNum[digit-1])
        power += 1
    if 	isNegative != False:
        print("Decimal: -" + str(decNum))
    elif isNegative != True:
        print("Decimal: " + str(decNum))



def main():
    hexToDec(input("Hex: "))
	

    
if __name__ == "__main__":
    main()
