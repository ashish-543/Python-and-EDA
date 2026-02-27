# Nested loops
# Loop inside another loop


# Print the cartesian product of (0,1,2), (0,1) and (0,1)

for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f'({x}, {y}, {z})')
# output:
# (0, 0, 0)
# (0, 0, 1)
# (0, 1, 0)
# (0, 1, 1)
# (1, 0, 0)
# (1, 0, 1)
# (1, 1, 0)
# (1, 1, 1)
# (2, 0, 0)
# (2, 0, 1)
# (2, 1, 0)
# (2, 1, 1)


# Applications of nested loop
# 1. To calculate the cartesian product of data i.e to check all the possible combinations of data


colors = ['red', 'purple', 'gold']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color}: Size-{size}')


# 2. To navigate the hierarchy
# For eg: to combine years with months and with days
# Print the names of files in the format report_y_m_d.csv. 
# Nested loop is used to generate the name of files that need to be generated daily, which is done by navigating the date hierarchy

years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 30)
for year in years:
    for month in months:
        for day in days:
            print(f'report_{year}_{month}_{day}.csv')
# output:
# report_2026_Jan_1.csv
# report_2026_Jan_2.csv
# report_2026_Jan_3.csv
# and so on..........


# 3. Navigating through tables columns and rows (an example of hierarchy navigation)
# Generate Sql query using nested loops for each tables
# Using nested loops to generate sql query automates task and prevents developer from writing thousands of query everytime

# select count(*) from customers where id is null;
# select count(*) from customers where create_date is null;
tables = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for table in tables:
    for column in columns:
        print(f'select count(*) from {table} where {column} is null;')
# output:
# select count(*) from customers where id is null;
# select count(*) from customers where create_date is null;
# select count(*) from orders where id is null;
# select count(*) from orders where create_date is null;
# and so on...................
