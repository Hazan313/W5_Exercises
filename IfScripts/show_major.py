#   Exercise 4b Lab 5:

#   1. Create a script named show_major.py that defines two variables for a student:
#   student_name and student_major. The student_major variable will contain a
#   code for the student’s major (e.g. ENG).

#   2. Use the following table to create lookup logic to display the name of the major and
#   location of the department’s office based on the major code:

# List all variables:

student_name = ''                                   # Contains student name
student_major = ''                                  # Contains code for student major
major_nado= {'Biology': 'Science Bldg, Room 310', 
              'Computer': 'Sheppard Hall, Room 314',
              'English' : 'Kerr Hall, Room 201',
              'History': "Kerr Hall, Room 114",
              'Marketing': 'Westly Hall, Room 310'} # major name and department office = major_nado

m_c = str(input('Enter Major Code:')).upper()       # makes all input UPPERCASE VALUES
m_k = ' '                                           # major key used to access and transform dict to list.
#m_cbiol = (f"{}")
# Formulate all processes:

if m_c == 'BIOL' or m_c == 'biol' or m_c=='bio':
    m_k = list(major_nado.keys())[0]
    print(f"Name of Major is {m_k} and Department Office is located at {major_nado['Biology']}")
    
elif m_c == 'CSCI' or m_c == 'csci' or m_c == 'comp':
    m_k = list(major_nado.keys())[1]
    print(f"Name of Major is {m_k} and Department Office is located at {major_nado['Computer']}")
    
elif m_c == 'ENG' or m_c == 'eng' or m_c == 'en':
    m_k = list(major_nado.keys())[2]
    print(f"Name of Major is {m_k} and Department Office is located at {major_nado['English']}")
    
elif m_c == 'HIST' or m_c == 'hist' or m_c == 'hs':
    m_k = list(major_nado.keys())[3]
    print(f"Name of Major is {m_k} and Department Office is located at {major_nado['History']}")
    
elif m_c == 'MKT' or m_c == 'mkt' or m_c == 'mk':
    m_k = list(major_nado.keys())[4]
    print(f"Name of Major is {m_k} and Department Office is located at {major_nado['Marketing']}")
    
else :  
    print(f"unknown code {m_c}, therefore unknown location. Please enter valid code ")
    


# Print all results:
   