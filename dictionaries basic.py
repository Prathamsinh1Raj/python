#key values pair

'''student = {'name': 'prathamsinh', 'age': 22, 'grade': 'A'}
print(student)'''

#Accessing, Adding, Updating, Deleting

'''student = {'name': 'prathamsinh', 'age': 22}
print(student['name'])           
student['grade'] = 'A'            
student['age'] = 22               

# Delete a key
del student['grade']
print(student)'''

#dictionary method

'''d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('b'))         
print(d.keys())            
print(d.values())          
print(d.items())       
print(d.pop('c'))        
print(d)'''

#nested dictionaries

'''students = {
    '101': {'name': 'prathamsinh', 'grade': 'A'},
    '102': {'name': 'rachit', 'grade': 'B'}
}
print(students['102']['name'])'''