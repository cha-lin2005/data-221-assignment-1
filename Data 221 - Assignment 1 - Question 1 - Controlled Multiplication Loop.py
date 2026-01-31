# Question 1: Write a Python program that multiplies consecutive integers starting from 1 until the product first
# becomes greater than a given threshold value.

threshold_number = 100
product_value = 1
currentNumber_multiplier = 1

while product_value <= threshold_number:
    product_value = product_value * currentNumber_multiplier

    if product_value > threshold_number:
        break
    
    currentNumber_multiplier +=1

print(f"The final product value is : {product_value}")
print(f"The integer that caused the product to exceed the threshold is: {currentNumber_multiplier}")