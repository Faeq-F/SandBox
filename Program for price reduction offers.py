
valueOfGoods = input("Please enter the value of the goods: ")
valueOfGoods = int(valueOfGoods)
if int(valueOfGoods) >= 200:
    print("Value of goods: ",
          valueOfGoods,"\nDiscount given: 10%\nAmount owed: "
          ,valueOfGoods-(valueOfGoods/10))
elif int(valueOfGoods) < 200 and int(valueOfGoods) > 100:
   print("Value of goods: ",
          valueOfGoods,"\nDiscount given: 5%\nAmount owed: "
          ,valueOfGoods-((valueOfGoods/10)/2))
else:
    print("Value of goods: ",
          valueOfGoods,"\nAmount owed: "
          ,valueOfGoods)

 
    
