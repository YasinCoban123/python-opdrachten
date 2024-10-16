sfind = set('orihme')
schar = set('ichgo')
print("Step 1:")
for i in sfind:
   if i in schar:
       print(i)
#
print("Step 2:")
schar.update(sfind)
for i in schar:
   print(i)