def DiscPrint(p, r):
    print('Calculating Discount')
    p = p - (p * r/100)
    print(p)

DiscPrint(100, 10)

# 1. The function name should should follow snake_case convention
# 2. The name of the function should be verb_based and it should clearly tell what the function does
# 3. The argument name should be meaningful
# 4. Don't use print statements insied functions until and unless it is necessary
# 5. Instead of prints, use return
# 6. Don't modify the argument passed to the function, instead use local variables 
# 7. Provide hint of the data type for arguments and return parameter of the function
# 8. Inside function, use a doctype string to explain what the function does and you can also add informaion about parameters

def calculate_discount(price: float, rate: float) -> float:
    '''
    Calculate final price after deducing discount from the original price.
    Args:
        price(float): Original Product Price
        rate(float): Rate of discount in numbers (eg: 10 for 10%)
    Returns:
        final_product_price(float): Final price after deducing discount from the original price
    '''
    final_price = price - (rate/100 * price)
    return final_price



print(calculate_discount(100, 10))

# The hint of the data type for argument and return parameters is given using:
# function_name(argument1: hint, argument2: hint) -> return_hint: 
# Here, the hint are just suggestions for the data type. The hint cannot perform any typecasting.


# The doctype string is used to explain what the function does
# Doctype string is used inplace of comment because comments are ignored whereas the doctype string is kept inside function
# And the information inside the doctype string can be recalled using help function of .__doc__function
# You can also see this description if you hover over the function

print(calculate_discount.__doc__)
    # Calculate final price after deducing discount from the original price.
    # Args:
    #     price(float): Original Product Price
    #     rate(float): Rate of discount in numbers (eg: 10 for 10%)
    # Returns:
    #     final_product_price(float): Final price after deducing discount from the original price
# help(calculate_discount)
