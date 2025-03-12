'''
    Dicionary
'''
#student Dictionay
student_data={"s001":[20,30,90],"s002":[89,65,93],"s003":[78,90,60]}

#Get values by writing key:
print(student_data["s001"])
print(student_data["s002"])
print(student_data["s003"])


#Add New Student data
student_data ["s004"]=[59,60,54]
print(student_data)


#Update marks for existing student
student_data["s001"][0]=45
print(student_data)

#Appending marks for existing student
student_data["s001"].append(70)
print(student_data)


# Dictionay key function
print(student_data.keys())

print(student_data.values())

print(student_data.items())

#Get Function
print()
d={"A":123,"B":124,"C":125}
v=d.get("A")
print(v)

#Return the value of D if available ortherwise return "Not Found" message.
v=d.get("D","Not Found")
print(v)

#It is also available in list
#Delete item

del d["A"]
print(d)


#Nested Dictionary
Students={
            "s001":{
                    "name":"Shaan",
                    "marks":[95,98,97]
                    },
            "s002":{
                    "name":"Ankita",
                    "marks":[85,88,87]
                    },
            "s003":{
                    "name":"Soniya",
                    "marks":[75,78,77]
                    }
    }

print(Students)
print(Students["s001"])
print(Students["s001"]["name"])
print(Students["s001"]["marks"])




















































































