string="a,b,c "     #multiply string into 3 times 
print(string*3)
                    # catenation operator
a= "my name " 
b="kartik and my age is "
c=21
print( a ,"is ", b , c)   
                         #isalnum method ( checking for alphabets or numeric in string 
name="kartik"
print(name.isalpha())
print(name.isalnum())
print(name.isdigit())
print(name.isspace())
print(name.islower())
print(name.isupper())
                                  # to print specific indexes 
a="pyhton programming"
print(a[1:14])
                                 # repalce string 
numbers="my name is kartik"
print(numbers.replace("kartik","ansh"))