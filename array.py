courses = ["MIT", "CYBER-SECURITY","DATASCIENCE"]
print(courses)

# accessing an element in array
print(courses[1])

# for looping an array
for course in courses:
    print(course)

    # adding annelement in array
courses.append("android development")
print(courses)

# removing an element in array
courses.remove("MIT")
print(courses)