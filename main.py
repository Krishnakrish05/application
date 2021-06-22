from collections import Counter
import re



def filehandling(file,ofile):
    opening_file= open(file,'r')
    reading_file=opening_file.read().split()
    print(reading_file)


# Print the number of words having prefix with “To” in the input file.
#Print the number of words ending with “ing” in the input file.
    n=-1
    suffixcount=0
    inital=0
    prefixcount=0



    for i in reading_file:
        if(i[n-2]=='i' and i[n-1]=='n' and i[n]=='g'):
            suffixcount=suffixcount+ 1


        if(i[inital]=='T' and i[inital+1]=='o'):

            prefixcount=prefixcount + 1

    print('The number of words having ending with "ing" is',suffixcount)
    print('The number of words having prefix "To" is ',prefixcount)



    #Print the word that was repeated maximum number of times.

    maximum=Counter(reading_file)
    print(maximum)
    char=''
    number=0

    for k in reading_file:
        if(maximum[k]>number):
            number=maximum[k]
            char=k

    print('Maximum char is',char)






#Finding the Palindrome in the file

    for l in reading_file:
       if(l==l[::-1]):
           print('The Palindrome is ',l)


#Convert all words into unique list and print in command line

    list=[]
    for a in reading_file:
        list.append(a)
        print(list)
        list.remove(a)


#Creating a Word dict with Key as counter index and value as the words present in file and print them on screen

    dict ={}

    for b in reading_file:
        dict[reading_file.index(b)]= b
    print(dict)



#Spliting the File based on Vowels
    str=''
    arr=[]
    for split in reading_file:
        res= re.split('a|e|i|o|u',split)
        print(res)
        for word in res:
            str=str+word

        arr.append(str)
        str=''
    print(arr)


 #Creating a following actions and writing it in new file

    op = open(ofile, "a")

    for up in arr:
        if len(up)>3:

          op.write(up[:2] + up[2].swapcase() + up[3:])

        elif len(up)==3:
         op.write(up[:2] + up[2].swapcase())

        if len(up)>5:
           op.write(up[:4] + up[4].swapcase() + up[5:])

        if up.isspace():
            op.write(up.replace('-'))

        if up.isalnum():
            op.write(up[::-1] + ';')



filehandling('file.txt','output.txt')





