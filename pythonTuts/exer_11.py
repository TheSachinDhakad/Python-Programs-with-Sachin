import re

str = '''An email thread is an email message that includes a running list of all the succeeding replies 
starting with the original email. The replies are arranged visually near the original message, 
usually in chronological order from the first reply to the most recent. This order is useful for the 
readers following the conversation because it is arranged in some hierarchical structure and may be 
arranged from top to bottom or vice versa sachindhakad568@gmail.com
depending on the email client or email provider used. Usually, the topmost email is the latest one.'''

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str)
print(email)



