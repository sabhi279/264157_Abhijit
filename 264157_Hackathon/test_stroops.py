Microsoft Windows [Version 10.0.26100.3476]
(c) Microsoft Corporation. All rights reserved.

(testenv) C:\Users\264157\Desktop\python_training>pip insrall .
ERROR: unknown command "insrall" - maybe you meant "install"

(testenv) C:\Users\264157\Desktop\python_training>cd C:\Users\264157\Desktop\python_training\28_march\Mini_Project

(testenv) C:\Users\264157\Desktop\python_training\28_march\Mini_Project>pip install .
Processing c:\users\264157\desktop\python_training\28_march\mini_project
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for minipack, since package 'wheel' is not installed.
Installing collected packages: minipack
  Attempting uninstall: minipack
    Found existing installation: minipack 1.0.0
    Uninstalling minipack-1.0.0:
      Successfully uninstalled minipack-1.0.0
  Running setup.py install for minipack ... done
Successfully installed minipack-1.0.0
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))) - skipping

(testenv) C:\Users\264157\Desktop\python_training\28_march\Mini_Project>python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import minipack
...............................................................welcome to new world.........................................
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 1
enter the string: mississippie
enter the substring: ss
[2, [(2, 4), (5, 7)]]
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s) 
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 2
Enter the word : abhijit
tijihba
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 3
Enter the word : hjl*&hj
hjlhj
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 4
Enter the word : abhijit mandal how are you
4
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 5
Enter the word : abhijit
7
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 6
Enter the word : abhijit how are you
Abhijit How Are You
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 7
Enter the word : abhijit   how     are    you
abhijit how are you
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : abhijitMandal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\264157\Desktop\python_training\28_march\Mini_Project\minipack\__init__.py", line 1, in <module>
    from .stroops import plaGame
  File "C:\Users\264157\Desktop\python_training\28_march\Mini_Project\minipack\stroops.py", line 123, in <module>
    plaGame()
  File "C:\Users\264157\Desktop\python_training\28_march\Mini_Project\minipack\stroops.py", line 90, in plaGame
    p=int(input(" please select the number : "))
ValueError: invalid literal for int() with base 10: 'abhijitMandal'
>>> import minipack
...............................................................welcome to new world.........................................
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 8
Enter the word : abHiji
ABhIJI
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 9
Enter the word : abcd
({'dbac', 'dacb', 'bcad', 'acbd', 'badc', 'bcda', 'adbc', 'dabc', 'dbca', 'cdba', 'bacd', 'acdb', 'abdc', 'bdac', 'cdab', 'adcb', 'cbda', 'dcba', 'dcab', 'cbad', 'cadb', 'abcd', 'bdca', 'cabd'}, '    total words are : 24')
1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s)
 5.charecterMap(s) 6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit
 please select the number : 10