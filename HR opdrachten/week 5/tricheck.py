
def check_triangle(kant_a: int, kant_b: int, kant_c: int) -> bool:

    if kant_a >= kant_b + kant_c or kant_b >= kant_a + kant_c or kant_c >= kant_a + kant_b:
        return False 
    
    return True  

if __name__ == "__main__":
    kant_a = int(input("Side A: "))
    kant_b = int(input("Side B: "))
    kant_c = int(input("Side C: "))
    
    result = check_triangle(kant_a, kant_b, kant_c)
    
    if result:
        print("Possible triangle")
    else:
        print("Impossible triangle")
