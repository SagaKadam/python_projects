quality = "Sagar is a good person"
print(quality)
print(quality[0:5])  #string slicing
print(len(quality))
print(quality[0:78])
print(quality[0:5:2])
print(quality[-4:-2])  #negative slicing
print(quality[18:20])

print(quality.isalnum())
print(quality.endswith("person"))
print(quality.count("o"))
print(quality.capitalize())
print(quality.find("is"))
print(quality.upper())
print(quality.replace("Sagar", "Omkar"))