sp_configure 'external scripts enabled', 1;
RECONFIGURE WITH OVERRIDE

----restart and run
EXEC sp_configure 'external scripts enabled'


----Test 1
EXECUTE sp_execute_external_script
@language = N'Python',
@script = N'
a = 1
b = 2
c = a+b
print ("Example instruction on Python")
print("Result =", c)';
