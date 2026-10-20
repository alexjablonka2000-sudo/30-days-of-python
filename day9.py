user=int(input("Enter your age: "))
if user >= 18:
    print("You are old enough to dirve.")
else:
    print("You need",18-user,"years to learn to drive")
other= int(input("Enter my age: "))
if user > other:
    if user==other+1:
        print("You are 1 year older than me")
    else:
        print("You are",user-other,"years older than me")
if user==other:
    print("We have the same age")                    

one= int(input("Enter number one "))
two= int(input("Enter number two "))
if one>two:
    print(one,"is bigger than",two)
elif one<two:
    print(one,"is smaller than",two)
else:
    print(one,"is equal to",two) 

grade=int(input("Write your grade "))
if grade>=90 and grade<=100:
    print("A")
elif grade>=80 and grade<=89:
    print("B")
elif grade>=70 and grade<=79:
    print("C")
elif grade>=60 and grade<=69:
    print("D")
elif grade>100:
    print("error")
else:
    print("F")

fruits = ['banana', 'orange', 'mango', 'lemon']
new=str(input("Insert a new fruit "))
if new in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new)
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }   
if "skills" in person:
    print(person["skills"])
    if "python" in person["skills"]:
        print("python is one of the skills")
if len(person["skills"])==2 and "Java" in person["skills"] and "React" in person["skills"]:
    print("He is a front and developer")
if ("Node" and "Python" and "MongoDB") in person["skills"]:
    if"React" in person["skills"]:
        print ("He is a fullstack developer")
    else: print ("He is a backend developer")
else:
    print("unknown title")
if person["is_married"] and "Finland" in person["country"]:
    print (person["first_name"], "lives in ",person["country"],". He is married")    
       