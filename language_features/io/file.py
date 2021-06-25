# create a file
f= open("python.txt","w+") # w flag for write operation, + is to create file if doesn't exist

# write to file
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

f.write("END")

# close the file
f.close()
