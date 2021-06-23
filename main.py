from collections import Counter
import re
import sys
import logging
import configparser

#Configuration-file
config = configparser.ConfigParser()
configFilePath = 'config'
config.read(configFilePath)

#Getting Configuration files
path = config.get('input-config', 'infile')
path2=config.get('output-config','outfile')


#Setting basic-config
logging.basicConfig(filename='logfile.log',level=logging.DEBUG,format="%(asctime)s:%(levelname)s:%(message)s")

#Parent Class
class files(object):
    def __init__(self,file,output):
        self.file= file
        self.output=output

    def reads(self):
        file=open(self.file,'r')
        reading= file.read().split()
        return reading

    def write(self):
        op = open(self.output, "a")
        return op

#Sub Class inheriting the Sub Class
class pre_suf(files):
    def prefix_suffix(self):

            n=-1
            suffixcount=0
            inital=0
            prefixcount=0
            reading_file=files.reads(self)


            for i in reading_file:
                if(i[n-2]=='i' and i[n-1]=='n' and i[n]=='g'):
                    suffixcount=suffixcount+ 1

                if(i[inital]=='T' and i[inital+1]=='o'):

                    prefixcount=prefixcount + 1

            self.printing('The number of words having ending with "ing" is',suffixcount)
            self.printing('The number of words having prefix "To" is ',prefixcount)


    def maximumword(self):
         reading_file=files.reads(self)
         maximum = Counter(reading_file)
         char = ''
         number=0

         for k in reading_file:
            if(maximum[k]>number):
                number=maximum[k]
                char=k

         self.printing('Maximum char is',char)


    def palindrome(self):
        reading_file = files.reads(self)
        for l in reading_file:
            if(l==l[::-1]):
             self.printing('The Palindrome is',l)

    def uniquelist(self):
        reading_file=files.reads(self)
        list = []
        for a in reading_file:
            list.append(a)
            self.printing('',list)
            list.remove(a)


    def dictonary(self):
        reading_file=files.reads(self)
        dict = {}

        for b in reading_file:
            dict[reading_file.index(b)]= b
        self.printing('',dict)

    def splitvowels(self):
        reading_file=files.reads(self)
        str = ''
        arr=[]
        for split in reading_file:
            res= re.split('a|e|i|o|u',split)
            self.printing('',res)
            for word in res:
                str=str+word
            arr.append(str)
            str=''
        self.printing('',arr)

        writing_file=files.write(self)

        for up in arr:
           if len(up)>3:
               writing_file.write(up[:2] + up[2].swapcase() + up[3:])

           elif len(up)==3:
             writing_file.write(up[:2] + up[2].swapcase())

           if len(up)>5:
               writing_file.write(up[:4] + up[4].swapcase() + up[5:])

           if up.isspace():
                writing_file.write(up.replace('-'))

           if up.isalnum():
                writing_file.write(up[::-1] + ';')

    def printing(self,a,b):
        print(a,b)
        logs='{}: {}'.format(a,b)
        logging.info(logs)

#Object Calling
a=pre_suf(path,path2)
a.prefix_suffix()
a.maximumword()
a.palindrome()
a.uniquelist()
a.palindrome()
a.dictonary()
a.splitvowels()


















