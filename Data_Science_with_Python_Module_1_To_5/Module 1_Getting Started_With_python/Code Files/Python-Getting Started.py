{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python-Getting Started"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assigning single value to a variable…"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "Victor\n",
      "2000.23\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "name = 'Victor'\n",
    "salary = 2000.23\n",
    "print (a)\n",
    "print (name)\n",
    "print (salary)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assigning multiple value to a variable…"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "a=b=c=10\n",
    "x,y,z=10,20,30\n",
    "print(y)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "String Literals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John\n",
      "James\n"
     ]
    }
   ],
   "source": [
    "name1=\"John\"\n",
    "name2='James'\n",
    "print(name1)\n",
    "print(name2)\n",
    "text1='hello\\\n",
    "World'\n",
    "text1\n",
    "multiline='''st1\n",
    "...st2\n",
    "...st3'''"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Special Literals: None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "val1 = 10\n",
    "val2 = None\n",
    "val1,val2\n",
    "print(val2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Operators"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Arithmetic Operator\n",
    "+, -, *, /, %"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "1+2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "1-2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "2%1"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assignment Operator =,+=, -=, *="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=10 \n",
    "a*=10 #a=10*10\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Comparison Operator <, >, <=, >=, !="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20 \n",
    "a > b"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Logical Operator: and, or , not "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "a=10<10 and 2>-1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Bitwise Operator &,|,>>,<<,~"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 | 5\n",
    "7 & 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Identity Operator is, is not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 10\n",
    "x is 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 10\n",
    "x is not 10"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Membership Operator in, not in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pets=['dog','cat','wolf']\n",
    "'lion' in pets\n",
    "'wolf' in pets\n",
    "'me' in 'appointment'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Datatypes in Python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Number "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'int'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "message = \"Hello World\"\n",
    "num = 1234\n",
    "pi = 13.6\n",
    "print(type(message)) #return a string\n",
    "print(type(num)) #return an integer\n",
    "print(type(pi)) #return a float"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H\n",
      "ytho\n"
     ]
    }
   ],
   "source": [
    "var1 = 'Hello-World!'\n",
    "var2 = 'PythonTutorial'\n",
    "\n",
    "print(var1[0]) # prints the first character in the string `H`\n",
    "print(var2[1:5]) # prints the substring 'ytho'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "find()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find() – Returns the position of the string\n",
    "str='Attachment'\n",
    "str.find('Me')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "replace()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Replacement'"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#replace() – Replaces one character/string with other\n",
    "str='Replacement'\n",
    "str.replace('ed','e')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['word1', 'word2', 'word3']"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#split() – Creates a split on the basis of a character\n",
    "str='word1,word2,word3'\n",
    "str.split(',')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Tuples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "myGroup = ('a', 'b', 'c', 'd')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "concatenation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a', 'b', 'c', 'd', 'f')\n"
     ]
    }
   ],
   "source": [
    "#Concatenation - Adds two string/character\n",
    "myGroup += ('f',)\n",
    "print(myGroup)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "repetation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('a', 'b', 'c', 'd', 'a', 'b', 'c', 'd')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Repetition -  Duplicate string/character by given number of times\n",
    "myGroup * 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'c'"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Indexing - Shows the indexed character/string\n",
    "myGroup = ('a', 'b', 'c', 'd', 'f')\n",
    "myGroup[2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('b', 'c', 'd')"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Slicing – Shows a specific set of indexed character/string\n",
    "myGroup = ('a', 'b', 'c', 'd', 'f')\n",
    "myGroup[1:4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "myGroup = ('a', 10, 7.12, 'data')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "concatenation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 1, 3.14, 'python', 'd']\n"
     ]
    }
   ],
   "source": [
    "#Concatenation – Add elements to the list\n",
    "myList = ['a', 1, 3.14, 'python']\n",
    "myList+=['d',]\n",
    "print(myList)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "repetation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 1, 3.14, 'python', 'a', 1, 3.14, 'python']"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Repetition\n",
    "myList = ['a', 1, 3.14, 'python']\n",
    "myList*2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3.14]"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Slicing\n",
    "myList = ['a', 1, 3.14, 'python']\n",
    "myList = myList[1:3]\n",
    "myList"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "append"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 1, 3.14, 'python', 'd']"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#append(value)\n",
    "myList = ['a', 1, 3.14, 'python']\n",
    "myList.append('d')\n",
    "myList"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "extend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 1, 3.14, 'python', 'c', 'd']"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#extend(list)\n",
    "myList = ['a', 1, 3.14, 'python']\n",
    "myList.extend (['c', 'd']) \n",
    "myList"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "insert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 1, 'd', 3.14, 'python']"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#insert(index, value)\n",
    "myList = ['a', 1, 3.14, 'python']\n",
    "myList.insert(2, 'd')\n",
    "myList"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "myDict = { 1: 'John' , 2: 'Bob', 3: 'Alice' }"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Empty dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "#empty dictionary \n",
    "myDict = {}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Integer keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dictionary with integer keys\n",
    "myDict = {1: 'apple', 2: 'ball'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dictionary with mixed keys\n",
    "myDict = {'name': 'John', 1: [2, 4, 3]}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "mixed keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dictionary with mixed keys\n",
    "myDict = {'name': 'John', 1: [2, 4, 3]}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#paring\n",
    "#from sequence having each item as a pair\n",
    "myDict = dict([(1,'apple'), (2,'ball')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#accessing dictionary\n",
    "myDict = {1: 'word1', 2: 'word2'}\n",
    "myDict[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#len()\n",
    "myDict = {1: ‘word1', 2: ‘word2’}\n",
    "len(myDict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#key()\n",
    "myDict = {1: 'apple', 2: 'ball'}\n",
    "myDict.key()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#values()\n",
    "myDict = {1: 'apple', 2: 'ball'}\n",
    "myDict.values()\n",
    "['apple', 'ball']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Sets"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet = {1, 2, 3}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Creating set\n",
    "mySet = {1, 2, 3, 3}\n",
    "print (mySet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Union\n",
    "myS1 = {1, 2, 'c'}\n",
    "myS2 = {1, 'b', 'c'}\n",
    "myS1 | myS2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Intersection\n",
    ">>>myS1 = {1, 2, 'c'}\n",
    ">>>myS2 = {1, 'b', 'c'}\n",
    ">>>myS1 & myS2\n",
    "{1, 'c'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Difference\n",
    ">>>myS1 = {1, 2, 'c'}\n",
    ">>>myS2 = {1, 'b', 'c'}\n",
    ">>>myS1 - myS2 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q1. What would be the output of the following code?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Fill the missing code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "thon\n"
     ]
    }
   ],
   "source": [
    "test1 = 'PythonProgramming'\n",
    "print(test1[2:6])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Flow Control"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# if-else"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nif (condition): \\n        statements 1 … \\nelse: \\n        statements 2 …\\n\\n'"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Syntax\n",
    "'''\n",
    "if (condition): \n",
    "        statements 1 … \n",
    "else: \n",
    "        statements 2 …\n",
    "\n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Nested if-else\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Syntax\n",
    "'''\n",
    "if (condition 1): \n",
    "        statements 1 … \n",
    "    elif (condition 2): \n",
    "        statements 2 …\n",
    "    else \n",
    "         statements 3 …\n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# for"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nfor iterating_var in sequence:               execute statements\\n'"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "for iterating_var in sequence:               execute statements\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in fruits:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# while"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nwhile (condition is True): \\n     statements1…\\n\\n'"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Syntax\n",
    "'''\n",
    "while (condition is True): \n",
    "     statements1…\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "a = 1\n",
    "while a<5:\n",
    "    print(a)\n",
    "    a+=2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 is odd\n",
      "2 is even\n",
      "3 is odd\n"
     ]
    }
   ],
   "source": [
    "a = 1\n",
    "while a<4:\n",
    "    if(a%2==0):\n",
    "        print(a, 'is even')\n",
    "    else:\n",
    "        print(a, 'is odd')\n",
    "    a+=1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Syntax\n",
    "'''\n",
    "def func_name (arg1, arg2, arg3, ….):\n",
    "\t\tstatements…\n",
    "\t\treturn [expression] \n",
    "'''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add (a,b):\n",
    "    sum = a + b\n",
    "    return sum"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Function Call"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pass by Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    ">>>a=10\n",
    ">>>def ChangeIt(b):\n",
    "… \t\tprint(“value of b is”, b)\n",
    "… \t\tb=100\n",
    "…\t\tprint(“New value of b is”, b)\n",
    "…\n",
    ">>>ChangeIt(a)\t\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Pass by Reference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value of d is [10, 20, 30]\n",
      "New value of d is [99, 98, 30]\n"
     ]
    }
   ],
   "source": [
    "c=[10,20,30]\n",
    "def ChangeThem(d):\n",
    "    print('value of d is', d)\n",
    "    d[0]=99\n",
    "    d[1]=98\n",
    "    print('New value of d is', d)\n",
    "ChangeThem(c)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q.2\n",
    "# Following function takes two parameters and print the first one. Fill the missing code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def my_function(fname, lname): \n",
    "print(…………………………………) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q.4\n",
    "# What is the output of .."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "fruits = (\"apple\", \"banana\", \"cherry\")\n",
    "if 'mango' in fruits:\n",
    "    print(3+4)\n",
    "else:\n",
    "    print(2*2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> # Lambda"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Syntax\n",
    "\n",
    "'''\n",
    "lambda arguments : expression\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n"
     ]
    }
   ],
   "source": [
    "x = lambda a : a + 10\n",
    "print(x(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Function vs Lambda Function\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function\n",
    "def multiply(x, y):\n",
    "    return x * y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Lambda Function\n",
    "r = lambda x, y: x * y\n",
    "r(12, 3)   # call the lambda function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Power of Lambda: Anonymous Function inside another function…\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Example\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n"
     ]
    }
   ],
   "source": [
    "def myfunc(n):\n",
    "  return lambda a : a + n\n",
    "mySum = myfunc(3)\n",
    "print(mySum(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q.5\n",
    "# Write a  lambda function that sums argument a, b, and c and print the result\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Q.6\n",
    "# What is the output of ..\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfunc(n):\n",
    "  return lambda a : a * n\n",
    "mydoubler = myfunc(2)\n",
    "print(mydoubler(11))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Storing in multiple variable\n",
    "car1 = \"Ford\";\n",
    "car2 = \"Volvo\";\n",
    "car3 = \"BMW\";\n",
    "#Using Array\n",
    "cars = [\"Ford\", \"Volvo\", \"BMW\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Accessing the element \n",
    "x = cars[0]\n",
    "#Modifying the element \n",
    "cars[0] = \"Honda\"\n",
    "print(cars[0])\n",
    "#Length of array\n",
    "x = len(cars)\n",
    "#Looping the Array\n",
    "for x in cars:\n",
    "  print(x)\n",
    "#Adding the element \n",
    "cars.append(\"Opel\")\n",
    "print(len(cars))\n",
    "#Removing one element \n",
    "cars.pop(1)\n",
    "#Removing specific element\n",
    "cars.remove(\"Volvo\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Classes/Object"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyClass:\n",
    "  x = 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "obj1 = MyClass()\n",
    "print(obj1.x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# File Handling"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Open"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Syntax\n",
    "f = open(\"path of file\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Example\n",
    "f = open(\"path of file\",\"rt\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Read"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Example\n",
    "f = open(\"demofile.txt\", \"r\")\n",
    "print(f.read())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading parts of file\n",
    "f = open(\"demofile.txt\", \"r\")\n",
    "print(f.read(5)) #Return the 5 first characters of the file\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading first line\n",
    "f = open(\"demofile.txt\", \"r\")\n",
    "print(f.readline()) #readline() is used to return one line\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading first line\n",
    "f = open(\"demofile.txt\", \"r\")\n",
    "print(f.readline()) \n",
    "print(f.readline()) # using readline() twice prints first two line\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loop through the file\n",
    "#Read the file line by line\n",
    "f = open(\"demofile.txt\", \"r\")\n",
    "for x in f:\n",
    "  print(x)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Write/Create"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Example: Append\n",
    "f = open(\"demofile.txt\", \"a\")\n",
    "f.write(\"Now the file has one more line!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "34"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Example: Overwrite\n",
    "f = open(\"demofile.txt\", \"w\")\n",
    "f.write(\"Woops! I have deleted the content!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a new file\n",
    "f = open(\"myfile.txt\", \"x\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Delete"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[WinError 2] The system cannot find the file specified: 'demofile.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-111-4566a23ffd32>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Deleting the file\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"demofile.txt\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [WinError 2] The system cannot find the file specified: 'demofile.txt'"
     ]
    }
   ],
   "source": [
    "# Deleting the file\n",
    "import os\n",
    "os.remove(\"demofile.txt\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
