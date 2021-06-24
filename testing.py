import pytest
from main import Presuf

ob=Presuf('file.txt','output.txt')



def test_prefixsuffix():
   assert ob.prefix_suffix()!=(0,0)

def test_maximumword():
   assert ob.maximumword() == ob.maximumword()

def test_palindrome():
   assert ob.palindrome() == ob.palindrome()[::-1]

def test_uniquelist():
   array=[]
   assert ob.uniquelist() == array

def test_dictonary():
   dicto={}
   assert bool(ob.dictonary()) != bool(dicto)

def test_read():
   array=[]

   assert ob.reads() != array


def test_write():
   file=open('output.py','a')
   assert ob.write() != file










