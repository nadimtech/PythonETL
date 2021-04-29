
EXECUTE sp_execute_external_script
@language = N'Python',
@script = N'
a = 1
b = 2
c = a+b
print ("Example instruction on Python")
print("Result =", c)';
