import pyodbc as po

# Connection string
cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
        server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()
 
# Fetch data into a cursor
cursor.execute("SELECT TOP (10) PersonID, FullName, PhoneNumber, \
    EmailAddress FROM Test ORDER BY PersonID DESC;")
 
# iterate the cursor
row = cursor.fetchone()
while row:
    # Print the row
    print(str(row[0]) + ", " + str(row[1] or '') + ", " + str(row[2] or '') + ", " + str(row[3] or ''))
    row = cursor.fetchone()
 
# Close the cursor and delete it
cursor.close()
del cursor
 
# Close the database connection
cnxn.close()



