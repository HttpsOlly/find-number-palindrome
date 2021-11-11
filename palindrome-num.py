def compute(num):
    i = 1
    while i < 100:
        reversedNumber = str(num)[::-1]
        addedNum = num + int(reversedNumber)
        addedNum = str(addedNum)

        ans = isPalindrome(addedNum)
        output = "({num} + {reversedNumber} = {addedNum})".format(num = num, reversedNumber = reversedNumber, addedNum = addedNum)

        if ans:
            print("PALINDROME FOUND!", output)
            break
        else:
            print("None", output)
            num = addedNum
            reversedNumber = num[::-1]

            num = int(num)
            reversedNumber = int(reversedNumber)
            
            addedNum = num + reversedNumber
            i += 1
            
def isPalindrome(addedNum):
    return addedNum == addedNum[::-1]

compute(197)