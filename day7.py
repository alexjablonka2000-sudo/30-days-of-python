# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update("Nvidia","OpenAI","Antropic")
it_companies.discard("Twitter")
C=A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A
del B
set_age=set(age)
print(len(age) == len(set_age))
test="I am a teacher and I love to inspire and teach people."
print(len(test.split()))
print(len(test))
