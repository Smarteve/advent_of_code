FILE ="input.txt"
with open(FILE,"r") as f:
    contents = [line.strip() for line in f.readlines()]  # by default .strip() remove all leading and trailing whitespace including new line character /n and /r 

def get_digits(line:str)->list[tuple[str,int]]:
    digits = []
    cur_str = ""
    is_accumulate =  False
    for i,ch in enumerate(line):
        if ch.isdigit():
            is_accumulate = True
            cur_str+=ch
                
        elif not ch.isdigit() and is_accumulate:
            digits.append((cur_str,i - len(cur_str)))
            cur_str = ""
            is_accumulate = False
    if cur_str:
        digits.append((cur_str,i-len(cur_str))) #need to take care of the last digit
    return digits

def is_valid_digit(digit,row,col,m,n):
    for r in range(row-1,row+2):  #get the rectangular 
        for c in range(col-1,col+len(digit)+1):
             if 0 <= r <m and 0 <= c <n:
                 if contents[r][c] not in ".0123456789":  
                    return True 
    return False 

def getting_sum(contents):
    total = 0 
    m = len(contents)
    n = len(contents[0])
   
    for i,line in enumerate(contents):
        row = i
        digits = get_digits(line)
        print(digits)
        for digit in digits:
            num = digit[0]
            col = digit[1]  # find only find the first occurrence
            if is_valid_digit(num,row,col,m,n):
                total += int(num)

    return total

print(getting_sum(contents))
        

        


