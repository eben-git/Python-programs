the_file = open("jackst.txt", "r")
for word in the_file.readlines():
    print(word)

the_file.close()