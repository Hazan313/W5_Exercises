# List all variables :
marketing_dept = {'1'  : 'Marketing',
                  '5'  : 'Human Resources',
                  '10' : 'Accounting',
                  '12' : 'Legal',
                  '18' : 'IT',
                  '20' : 'Customer Relations'}

dep_num = int(input('Which department number are you referring to?'))

# Formulate all processes :
if dep_num == 1:
    print(f"The department you are referring too is {marketing_dept.get('1')}")
elif dep_num == 5:
    print(f"The department you are referring too is {marketing_dept.get('5')}")
elif dep_num == 10:
    print(f'The department you are referring too is {marketing_dept.get('10')}')
elif dep_num == 12:
    print(f'The department you are referring too is {marketing_dept.get('12')}')
elif dep_num == 18:
    print(f'The department you are referring too is {marketing_dept.get('18')}')
elif dep_num == 20:
    print(f'The department you are referring too is {marketing_dept.get('20')}')


# Print the results: