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
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

phone='''+91 8679045673",
"+91 8679045673",
"+9 67845673",
"+1 8679045673",
"+91 8076529423",
"+91 86790456730",
"+91 86790456673",
"+910 86790456 73",
"+971 867904 5673",
"+9152 8679 045673",
+91 7076529423'''

# Task
# Given a string with a lot of indian phone numbers starting from +91

patt=re.compile(r".+91 \d{10}")

matches = patt.finditer(phone)
for match in matches:
    print(match)


"""


"""
