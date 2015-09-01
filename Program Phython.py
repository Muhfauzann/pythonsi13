Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> print hello word
SyntaxError: invalid syntax
>>> print "hello word"
hello word
>>> print 1
1
>>> a=2
>>> print a
2
>>> a = raw_input("input sebuah kata : ")
input sebuah kata : kata
>>> print a
kata
>>> nama = raw_input("masukkan nama : ")
masukkan nama : M Fauzan
>>> a
'kata'
>>> print a
kata
>>> nama
'M Fauzan'
>>> print "nama saya()".format(nama)
nama saya()
>>> print "nama saya(0)".format(nama)
nama saya(0)
>>> print "nama saya{}".format(nama)
nama sayaM Fauzan
>>> print "nama saya{} ".format(nama)
nama sayaM Fauzan 
>>> print "nama saya{}". format(nama)
nama sayaM Fauzan
>>> print "nama saya {}".format(nama)
nama saya M Fauzan
>>> for i in range (12)
SyntaxError: invalid syntax
>>> for i in range (12) :
	print i,

	
0 1 2 3 4 5 6 7 8 9 10 11
>>> ================================ RESTART ================================
>>> 
selamat datang :)
masukkan nama anda: M Fauzan
masukkan umur anda: 20
haii M Fauzan dan umur saya 20 tahun
>>> ================================ RESTART ================================
>>> 
selamat datang :)
masukkan alas anda: 2
masukkan tinggi anda: 3
luas segitiga adalah 6
>>> ================================ RESTART ================================
>>> 
selamat datang :)
masukkan alas anda: 2
masukkan tinggi anda: 4
luas segitiga adalah 4
>>> for i in range (12)
SyntaxError: invalid syntax
>>> 
>>> 
>>> for i in range :
	print i,

	

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    for i in range :
TypeError: 'builtin_function_or_method' object is not iterable
>>> for i in range (9):
	print i,

	
0 1 2 3 4 5 6 7 8
>>> 
