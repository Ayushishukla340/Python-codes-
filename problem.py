# f = open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#   print("the word twinkle is present in the content")
# else:
#   print("the word twinkle is not presnt...............")  


# f.close()


f = open("poem.txt")

content = f.read()

if ("twinkle" in content):
    print("The word 'twinkle' is present in the content")
else:
    print("The word 'twinkle' is not present")

f.close()