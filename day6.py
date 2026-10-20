tpl=()
brothers=("jojo","oved","Gold")
sisters=("mimi","mimi2")
siblings=brothers+sisters
print(len(siblings))
family_Members=list(siblings)
family_Members.append("Eduardo")
family_Members.append("Simone")
family_Members=tuple(family_Members)
print(family_Members)
family_Members=list(family_Members)
first,*all,last=family_Members
print(first,*all,last)
fruits_Tp=("Apple","Banana")
vegetables_Tp=("Corn","Lettuce")
animals_Tp=("Fish","Meat")
food_stuff_tp=fruits_Tp+vegetables_Tp+animals_Tp
food_stuff_it=list(food_stuff_tp)
middle=food_stuff_it[2:4]
first=food_stuff_it[0:2]
last=food_stuff_it[4:]
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
