import math

def extract_nature():
    numbers= []
    for i in range(3,1000):
        if (i % 3 ==0 or i% 5 == 0):
            numbers.append(i)
            i = i +1
    return(numbers)
def main():
    num = extract_nature()  
    print(sum(num))

if __name__ =="__main__":
    main()