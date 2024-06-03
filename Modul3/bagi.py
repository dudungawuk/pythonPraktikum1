bil1 = float(input("masukan bilangan pembagi : "))
bil2 = float(input("masukan bilangan yang akan dibagi : "))
if(bil2 == 0):
    print("pembagi tidak boleh 0")
else:
    bagi = float(bil1 / bil2)
    print(f"hasil bagi {bagi}")