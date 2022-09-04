
import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiin'''

# findall, search, split, sub, finditer

# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai*')
# patt = re.compile(r'ai{2}')
patt = re.compile(r'(ai){2}')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[448:452])

'''\A:         the resultant is a match if the input characters are at the beginning of the string                
\b          the resultant is a match whether the input characters are at the beginning or the end of a word                               
\d          the resultant is a match if the string contains any digits  
\s           the resultant is a match if the string contains a white space character
There are many metacharacters supported by the re module. Some characters with their working are the following:

‘.’: Matches any single character except newline
‘$’: Anchors a match at the end of a string
‘*’: Matches zero or more repetitions
‘+':Matches one or more repetitions
‘{}’: Matches an explicitly specified number of repetitions
‘[]’: Specifies a character class
To explore more about the re module, check the https://docs.python.org/3/library/re.html python documentation.

 
Re.txt file as described in the video!

Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r” ain\b.”
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string

'''