# Regex Email Extractor

import re
mystr="Hello my name is sonia and my " \
      "email is soniarai10030@gamil.com" \
      "next is me suhani raj and my" \
      "email is suhaniraj1678@gmail.com" \
      " yoo!! this is me priyanka and " \
      "my email is priyankakuma4563r@gmail.com" \
      "bye now see you next time "

emails=re.compile(r'[\w]+@[\w]+.com').findall(mystr)
l=[]
for email in emails:
    l.append(email)
    st=str(l)
with open("Email Extractor.txt","w") as f:
         f.writelines(st.split())

with open("Email Extractor.txt") as f:
        s = f.readlines()
        for i in s:
            print(i)
