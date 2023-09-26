import re

sentence = 'Start a sentence and then bring it to an end'
# print(r'\tTab')
#print('\tTab')

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Haha

google.com
. ^ $ * + ? { } [ ] \ | ( )

321-555-4321
123.555.1234

H. M. Adil
'''
# pattern = re.compile('.\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W\s\W')
# matches = pattern.finditer(text_to_search)

# for match in matches:
    # print(match)

# --------------------------Q#1
# Write a regexp that will match any string that starts with “csc” and ends with “001” with any number of
# characters, including none, in between
# ○ Hint: consider using a wildcard character

text = 'csc is the end of 001'
print(re.match('csc',text))
end = re.compile('001$')
match_001 = end.finditer(text)

for matchend in match_001:
    print(matchend)

# --------------------------Q#2
# Write a regexp that will match name and extension of any Python (.py) file
# There must be at least one character (name of the file) before the “.” (file extension dot)
file_extension = 'file.py'
file = re.compile('\w\w\w\w\.\w\w')
match_file = file.finditer(file_extension)

for matchfile in match_file:
    print(matchfile)

# --------------------------Q#3
# Check using a regexp the following string contain a legal Python filename?
# String: “This contains two files, assignment1.py and ids.py”

legal_file = '''
assignment1.py
ids.py
'''
legal = re.compile('\w\w\w\w\w\w\w\w\w\w\w\.\w\w')
match_legal = legal.finditer(legal_file)

for matchlegal in match_legal:
    print(matchlegal)

# --------------------------Q#4
# Write a regexp which detects legal Microsoft Word file names in a string and make a list of them
# File names must end with “.doc” or “.docx”
# There must be at least one character before the . (file extension dot)
# Assume there are no spaces in the file names

legal_doc = '''
file.doc
file.xl
file.py
fil1.docx
file.docx
'''

legaldoc = re.compile('\w\w\w\D\.doc$')
legaldocx = re.compile('\w\w\w\D\.docx$')
matchlegaldoc = legaldoc.finditer(legal_doc)
matchlegaldocx = legaldocx.finditer(legal_doc)

for matchdoc in matchlegaldoc:
    print(matchdoc)

for matchdocx in matchlegaldocx:
    print(matchdocx)


# print(text_to_search[1:4])
# pattern = re.compile('.') macthes all characters except the new line
# pattern = re.compile('\d') (0-9)
# pattern = re.compile('\D') !(0-9)
# pattern = re.compile('\w') macthes (a-z,A-Z,0-9, _)
# pattern = re.compile('\W')  !(a-z,A-Z,0-9, _)
# pattern = re.compile('\s')  (space, tab,newline)
# pattern = re.compile('\S')  !(space, tab,newline)
# pattern = re.compile('\bha')  ha ha (1st and 2nd matche because they have a space in between)
# pattern = re.compile('\Bha')  ha (opposite to the \b)

# pattern = re.compile('^Start')
# matches = pattern.finditer(sentence) begginning of the string

# pattern = re.compile('^end')
# matches = pattern.finditer(sentence) end of the string


