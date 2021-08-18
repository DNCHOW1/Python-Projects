from bs4 import BeautifulSoup
import requests, re, os

with open('TextbookScraping.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

find_bad = re.compile(r'<strong>|TEKS')

p_list = []
real_list = []

for paragraph in soup.find_all('p'): # Narrows down to the text only
    p_list.append(paragraph)

for i in p_list: # Gets only the needed reading
    check_p = i.attrs.get('class', 0)
    if check_p == ['embedded-asset-media'] or check_p == 0:
        mo = find_bad.search(str(i))
        if mo == None and len(i.text) >= 20:
            #print(i, '\n')
            real_list.append(i.text)

print(len(real_list))
path = 'Chapter_11/Lesson1_all'

os.chdir('/Users/DienChau/PythonPractice/PersonalProjects/NLP_WPAPNOTES/Raw_Chapters') # Writes the paragraphs to page
with open(path, 'w') as f:
    for i in real_list:
        f.write(i + '\n\n')

with open(path, 'r') as f: # This searches for extra '\n', and removes it
    x = []
    for line in f:
        x.append(line)

    def file_recursion(samp, condition):
        for i, v in enumerate(samp):
            if i != len(samp) - 1:
                if (v == '\n' or v == '\xa0\n') and (samp[i + 1] == '\n' or samp[i + 1] == '\xa0\n'):
                    samp.pop(i)
                    new_condition = file_recursion(samp, condition)
                    if new_condition == 1:
                        break
            else:
                return 1

    file_recursion(x, 0)
    with open(path, 'w') as sf:
        for i in x:
            sf.write(i)
