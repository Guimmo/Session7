text = "Hello World"
print(text)
text = 'Hello World 2' #single vs double
print(text)
print(text[4])
print(len(text)) #text length
text = ""
print(len(text))

text = "Bob"
print(text[-1])  #last character in string
print(text[-3])

#print(text[3]) # this is an error
print(text[6//3])


s1= "hello "
s2 = "bye"
print(s1+s2)
print(s1*4)

s1= "hello my name is bob"
for c in s1:
    print(c)

s1 = "i like to give high fives"
#print this string but replace "i" with "y"

for c in s1:
    if c == "i":
        print("y", end="")
    elif c == "I":
        print("Y",end="")
    else:
        print(c, end="")
print()



