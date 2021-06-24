"""Import statements"""  #pylint: disable=pointless-string-statement
import configparser  #pylint: disable=wrong-import-position

"""Importing logging"""  #pylint: disable=pointless-string-statement
import logging    #pylint: disable=wrong-import-position

"""Importing counter"""  #pylint: disable=pointless-string-statement
from collections import Counter #pylint: disable=wrong-import-position

"""Importing regular-expression""" #pylint: disable=pointless-string-statement
import re   #pylint: disable=wrong-import-position


"""Using configparser"""  #pylint: disable=pointless-string-statement
config = configparser.ConfigParser()
CONFIG_FILE_PATH = 'config'
config.read(CONFIG_FILE_PATH)

"""Getting config path files"""  #pylint: disable=pointless-string-statement
path = config.get('input-config', 'infile')
path2 = config.get('output-config', 'outfile')

"""Setting basic-config"""  #pylint: disable=pointless-string-statement

logging.basicConfig(filename='logfile.log', level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

"""Parent class"""
class Files():
    """Defining constructor"""  #pylint: disable=pointless-string-statement

    def __init__(self, file, output):
        self.file = file
        self.output = output

    """Reading the file"""  #pylint: disable=pointless-string-statement
    def reads(self):
        file = open(self.file, 'r')  # pylint:disable=consider-using-with
        reading = file.read().split()
        return reading

    """Writing the File"""
    def write(self):
        output_file = open(self.output, "a")  # pylint:disable=consider-using-with
        return output_file

"""Sub Class inheriting the Sub Class"""
class Presuf(Files):

    def prefix_suffix(self):
        last_no = -1
        suffixcount = 0
        inital = 0
        prefixcount = 0
        reading_file = Files.reads(self)

        for i in reading_file:
            if (i[last_no - 2] == 'i' and i[last_no - 1] == 'n' and i[last_no] == 'g'):
                suffixcount = suffixcount + 1

            if (i[inital] == 'T' and i[inital + 1] == 'o'):
                prefixcount = prefixcount + 1

        self.printing('The number of words having ending with "ing" is', suffixcount)
        self.printing('The number of words having prefix "To" is ', prefixcount)
        return prefixcount,suffixcount

    def maximumword(self):
        reading_file = Files.reads(self)
        maximum = Counter(reading_file)
        char = ''
        number = 0

        for k in reading_file:
            if maximum[k] > number:
                number = maximum[k]
                char = k
        self.printing('Maximum char is', char)
        return char


    def palindrome(self):
        reading_file = Files.reads(self)
        for l in reading_file:  # pylint:disable=invalid-name
            if l == l[::-1]:
                self.printing('The Palindrome is', l)
                return l

    def uniquelist(self):
        reading_file = Files.reads(self)
        empty_array = []
        for value in reading_file:
            empty_array.append(value)
            self.printing('', empty_array)
            empty_array.remove(value)
            return empty_array

    def dictonary(self):
        reading_file = Files.reads(self)
        dict = {}  # pylint: disable=redefined-builtin

        for words in reading_file:
            dict[reading_file.index(words)] = words
        self.printing('', dict)
        return dict

    def splitvowels(self):
        reading_file = Files.reads(self)
        empty_string = ''
        arr = []
        for split in reading_file:
            res = re.split('a|e|i|o|u', split)
            self.printing('', res)
            for word in res:
                empty_string = empty_string + word
            arr.append(empty_string)
            empty_string = ''
        self.printing('', arr)

        writing_file = Files.write(self)

        for upper in arr:  # pylink:disable=invalid-name
            if len(upper) > 3:
                writing_file.write(upper[:2] + upper[2].swapcase() + upper[3:])

            elif len(upper) == 3:
                writing_file.write(upper[:2] + upper[2].swapcase())

            if len(upper) > 5:
                writing_file.write(upper[:4] + upper[4].swapcase() + upper[5:])

            if upper.isalnum():
                writing_file.write(upper[::-1] + ';')

    """Printing function"""
    def printing(self, strings, statement):  # pylint: disable=no-self-use
        print(strings, statement)
        logs = '{}: {}'.format(strings, statement)
        logging.info(logs)


"""Object calling"""
obj = Presuf(path, path2)
obj.prefix_suffix()
obj.maximumword()
obj.palindrome()
obj.uniquelist()
obj.palindrome()
obj.dictonary()
obj.splitvowels()
