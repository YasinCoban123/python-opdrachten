#Sides: a=5, b=6, c=5

#print("value of the triangle length: ")
#a = int(input("a: "))
#b = int(input("b: "))
#c = int(input("c: "))



#if a==b or b==c or c==a:
 #  print("Isosceles triangle")
#else:
#   print("triangle")

sides=input("the measurement of the sides: a, b, c "  )
sides_of_shapes=(sides.split(','))
print(sides_of_shapes[0])
side_1=(sides_of_shapes[0].split('='))
triangle_side_1 = int(side_1[1])
print(triangle_side_1)
print(sides_of_shapes[1])
side_2=(sides_of_shapes[1].split('='))
triangle_side_2 = int(side_2[1])
print(triangle_side_2)
print(sides_of_shapes[2])
side_3 = (sides_of_shapes[2].split('='))
triangle_side_3 = int(side_3[1])
print(triangle_side_3)
print(side_1,side_2,side_3)
if triangle_side_1!=triangle_side_2 and triangle_side_2!=triangle_side_3 and triangle_side_3==side_1:
   print("Isosceles triangle")
elif triangle_side_1 == triangle_side_2 and triangle_side_2 == triangle_side_3 and triangle_side_3 == triangle_side_1:
   print("equilateral")
elif triangle_side_1< triangle_side_2 and triangle_side_2 < triangle_side_3 and triangle_side_1 < triangle_side_3:
   print("Scalene")
