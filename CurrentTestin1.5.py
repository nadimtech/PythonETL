import pandas as pd

excel_file = pd.ExcelFile('stack.xlsx')
type(excel_file)
excel_file.sheet_names

excel_df = excel_file.parse()
type(excel_df)
excel_df.head()
excel_df

posts_excel = pd.read_excel('stack-one.xlsx')
type(posts_excel)
dir(posts_excel)
posts_excel.columns
posts_excel.head()
pd.read_excel('stack-one.xlsx', usecols=[0, 3]).columns
pd.read_excel('stack-one.xlsx', usecols='A:C').columns
pd.read_excel('stack-one.xlsx', usecols='A,C').columns

excel_file.sheet_names
posts_dict = pd.read_excel('stack.xlsx',sheet_name=None)
type(posts_dict)
posts_dict.keys()
posts_dict['Posts'].head()

posts_dict['Users'].head()
pd.read_excel('stack.xlsx',sheet_name='Users').head()
pd.read_excel('stack.xlsx',sheet_name='Users', usecols=range(1,9)).head()
pd.read_excel('stack.xlsx',sheet_name=2).head()
pd.read_excel('stack.xlsx',sheet_name='Users', usecols=range(1,9)).head()
pd.read_excel('stack.xlsx',sheet_name='Users', usecols=range(1,9),skiprows=4).head()
pd.read_excel('stack.xlsx',sheet_name='Users', usecols=range(1,9),nrows=2).head()
pd.read_excel('stack.xlsx',sheet_name='Users', usecols=range(1,9)).dtypes
pd.read_excel('stack.xlsx',sheet_name='Users', usecols=range(1,9), dtype={'PostTypeId': str}).dtypes
pd.read_excel('stack.xlsx',sheet_name='Users', converters={'Id': lambda x: x + 1000}).head()
pd.read_excel('stack.xlsx',sheet_name='Count', usecols=[0,7,8]).head()
pd.read_excel('stack.xlsx',sheet_name='Count', usecols=[0,7,8], keep_default_na=False).head()

# Import data with Psycopg2
# sql
# \l
# \d
import psycopg2
stack_connection = psycopg2.connect("dbname=importing_postgres user=xavier host=localhost")
so_cursor = stack_connection.cursor()

so_cursor.execute("select * from total")
first_row = so_cursor.fetchone()
first_row
type(first_row)
rows = so_cursor.fetchall()
rows
type(rows)

stack_connection.commit()
stack_connection.close()


# show databases;
# show tables;
posts = pd.read_sql_table('posts', engine, index_col='Id')
type(posts)
posts.columns 
posts.head()

posts = pd.read_sql_table('posts', engine, columns=['Id', 'CreationDate', 'Tags'])
posts.head()
type(posts.iloc(1)[1])
posts = pd.read_sql_table('posts', engine, columns=['Id', 'CreationDate', 'Tags'], parse_dates={'CreationDate': {'format': '%Y-%m-%dT%H:%M:%S.%f'}})
type(posts.iloc(1)[1])


from sql2019 import create_engine
engine = create_engine('sqlite:///importing_sqlite.db')
type(engine)
dir(engine)
engine.table_names()
engine.url
engine.dialect
engine.driver

engine_sqlite = create_engine('sqlite:///importing_sqlite.db')
engine_sqlite = create_engine('sqlite:///importing_sqlite.db')

EXEC sp_execute_external_script
@language = N'python',
@script =
N'import pyodbc
import pandas as pa
 
if includes != "%":
    WhereClause = " AND name IN (''" + includes.replace(",","'',''") + "'')"
elif excludes != "%":
    WhereClause = " AND name NOT IN (''" + excludes.replace(",","'',''") + "'')"
else:
    WhereClause = ""
 
query = query + WhereClause
 
SourceConnection = pyodbc.connect(sourceConnectionString)
SourceLogins = pa.read_sql(query,SourceConnection)
 
DestinationConnection = pyodbc.connect(destinationConnectionString)
DestinationLogins = pa.read_sql(query,DestinationConnection)
 

    for counter in range(len(MismatchingLogins.index)):
        Statement = "DROP LOGIN [" + MismatchingLogins.values[counter][0] + "]"
        DropLoginCursor = DestinationConnection.cursor()
        DropLoginCursor.execute(Statement)
        DropLoginCursor.commit()
 
counter = 0
 
for counter in range(len(MissingLogins.index)):
    if MissingLogins.values[counter][0].find("\\") >= 0:
        Statement = "CREATE LOGIN [" + MissingLogins.values[counter][0] + "] FROM WINDOWS"
    else:
        Statement = "CREATE LOGIN [" + MissingLogins.values[counter][0] + "] WITH PASSWORD = 0x" + MissingLogins.values[counter][2].hex() + '' HASHED, SID = 0x'' + MissingLogins.values[counter][1].hex()
    NewLoginCursor = DestinationConnection.cursor()
    print(Statement)
    NewLoginCursor.execute(Statement)
    NewLoginCursor.commit()
 
OutputDataSet = MissingLogins
',
@params = N'@query VARCHAR(MAX),@includes VARCHAR(4000), @excludes VARCHAR(4000), @destinationConnectionString VARCHAR(4000), @sourceConnectionString VARCHAR(4000), @RecreateOnSIDMismatch BIT',
@includes = '%',
@excludes = '%',
@destinationConnectionString = 'DRIVER={SQL Server};SERVER=laptop-fowlerd\sql2017;UID=PythonUser;PWD=P4ssw0rd',
@sourceConnectionString = 'DRIVER={SQL Server};SERVER=laptop-fowlerd\sql2016;UID=PythonUser;PWD=P4ssw0rd',
@RecreateOnSIDMismatch = 0,
@query = 'select name, CAST(sid AS VARBINARY(256)) AS sid, ISNULL(CAST(LOGINPROPERTY(name,''PasswordHash'') AS VARBINARY(256)),0x0) AS PasswordHash FROM sys.syslogins WHERE name NOT LIKE ''NT AUTHORITY%'' AND name NOT LIKE ''NT SERVICE%'' AND name NOT LIKE ''sa'' AND name NOT LIKE ''#%##'''
WITH RESULT SETS UNDEFINED
