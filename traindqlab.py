from xmlrpc.client import boolean


number1 = 20
number2 = 10    
print(number1 - number2)
print(number1 * number2)

real_price = 20000
discount = 2000
price_after_discount = real_price - discount
final_price = price_after_discount * 1.1
print(final_price)

number1, number2 = 10, 20
#Salam = "Selamat Pagi" , Malam = "Selamat Malam"
#print(Morning, number1, number2)

example_list = [1, 'two', 3, 4.0, 5]
print(example_list[0])
print(example_list[3])
example_list = [1, 'two', 3, 4.0, 5]
example_list[3] = 4
print(example_list[3])

#type data tuple
example_tuple  = ('January', 'February', 'March', 'April')
print(example_tuple[0])
#example_tuple = ('January', 'February', 'March', 'April')
#example_tuple[0] = 'December'

#Type data list
example_list = ['Dewi', 'Budi', 'Cici', 'Linda', 'Cici']
print(example_list)
#Type data set
example_set = {'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'}
print(example_set)
#Type data frozenset
example_frozen_set = ({'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'})
print(example_frozen_set)

#Type data maaping
person = {"name": "Michael", "Work": "Data Engineer"}   # dictionary
print(person['name'])
print(person['Work'])

#type data dictionary
shoes = {'name' : 'Niko Shoes', 'Price' :  150000, 'Discount' :  30000}
cloth = {'name' : 'Unikloh Cloth', 'Price' : 80000, 'Discount' : 8000}
pants = {'name' : 'Levis Pants', 'Price' : 200000, 'Discount' : 60000}
shoes_price = shoes['Price'] - shoes['Discount']
cloth_price = cloth['Price'] - cloth['Discount']
pants_price = pants['Price'] - pants['Discount']
total_price = shoes_price + cloth_price + pants_price
total_tax = total_price * 1.1
print(total_price + total_tax)

x = 10
print(type(x) is int)
x /= 3
print(type(x) is float)
x /= 3
print(type(x) is int)
#x /= 3
#print(type(x) is boolean)

#membership Operators
#in
x = ["apple", "banana", "cherry"]
y = "cherry"
z = "orange"
print(y in x) #True
print(z in x) #False

#not in
x = ["apple", "banana", "cherry"]
y = "cherry"
z = "orange"
print(y not in x) #False
print(z not in x) #True

#Value Priority Operators in Python
#begining code
total_price = 150000
discount_price = 0.3
tax = 0.1 #tax in percentage 1
pay_price = 1 - discount_price
pay_price *= total_price
pay_tax = pay_price * tax
pay_price += pay_tax
print("Begin_Code - Pay_Price=", pay_price)

total_price = 150000
discount_price = 0.3
tax = 0.1 #tax in percentage
pay_price = total_price - (total_price * discount_price)
pay_price += pay_price * tax 
print("Code Simplification - Pay_Price=", pay_price)
