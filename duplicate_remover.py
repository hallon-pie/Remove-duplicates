# Put this python file in the same directory as .txt file that is tobe modifyed or define path in place of (passwordlist.txt).

var = open('passwordlist.txt','r').readlines()

var1 = set(var)

# Here i am going to name the new file without duplicates as 'cleanPasswordlist.txt'

var2 = open('cleanPasswordlist.txt','w')

for line in var1:
    var2.write(line)
