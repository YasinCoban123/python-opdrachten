def mod_rec(width, height):
    num = 0  
    for row in range(height):
        for col in range(width):
            print(num % 10, end=" ")
            num += 1  
        print() 

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

mod_rec(width, height)
