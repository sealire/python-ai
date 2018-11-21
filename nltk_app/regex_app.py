import re

text = "Please contact us at contact@qq.com for further information.visiting http://www.google.com." + \
       " You can also give feedbacl at feedback@yiibai.com. " + \
       "https://www.yiibai.com to learn further on a variety of subjects."

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(urls)
print(emails)
