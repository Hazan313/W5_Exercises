# Lab 3: Updating HR Document

# Step 1: Start with the provided list of employee data
hr_list = [ ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000') ]

# Step 2: Update Mark's last name to Blick-Hawley
for i, employee in enumerate(hr_list):
    
    if employee[2] == 'Mark Blick':# Check if the employee's name is Mark Blick
        
        hr_list[i] = (employee[0], employee[1], 'Mark Blick-Hawley', employee[3])# Create a new tuple with the updated name

# Step 3: Change Jim's department to CS and update his salary to 60000
for i, employee in enumerate(hr_list):
    # Check if the employee's name is Jim Smith
    if employee[2] == 'Jim Smith':
        # Create a new tuple with updated department and salary
        hr_list[i] = (employee[0], 'CS', employee[2], '60000')

# Step 4: Display the updated contents in the specified format
print("Employee# | DeptCode | Name | Salary")
for employee in hr_list:
    # Format the salary with a comma
    salary_with_commas = f"{int(employee[3]):,}"  # Convert salary to int and format with commas
    # Print the employee details separated by |
    print(f"{employee[0]} | {employee[1]} | {employee[2]} | {salary_with_commas}")
