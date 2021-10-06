from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

url = 'https://careers.google.com/jobs/results/92311815330898630-big-data-and-analytics-cloud-consultant-professional-services/?distance=50&has_remote=true&location=Washington,%20USA&q=certification'

driver.get(url)


all_text = driver.find_element_by_xpath("/html/body").text

jobdesc = all_text.split()


dict1 = {}
dict2 = {}
count1 = 0
count2 = 0
do_not_include = ['the','and','or','a','an','but','with','of','to','for','as','on',
                  'in','•','that','through','&','they','have','what','how','has','such',
                  'than','before','at','it','then','this','into','their','while']
wordcount = 0

file1 = open('resume.txt','r')
for line in file1:
    for word in line.split():
        wordcount +=1
        word = word.lower()
        if word not in do_not_include:
            dict1[word] = dict1.get(word,0)+ 1
            count1 +=1
print('Most common in resume:',sorted(dict1, key=dict1.get, reverse=True)[:10])

qual = 0    # flag that sets if we've hit the qualificaitons section
for word in jobdesc:
    word = word.lower()
    if qual == 0:
        if (word == "qualification") or (word == "qualifications"):
            qual = 1
    if qual == 1:
        if word == "job":
            qual = 0
        print(word)
        if word not in do_not_include:
            dict2[word] = dict2.get(word,0)+ 1
            count2+=1
print('Most common in job description:',sorted(dict2, key=dict2.get, reverse=True)[:10])


## Relevant information to print
#    total percentage of words in 2 also covered by 1
#    which words in 2 are not covered by 1, ranked by most common
#    most common words in both

for word in dict1:
    if word in dict2:
        dict2.pop(word)
covered = 100 - (100*len(dict2) / count2)

print('Word Count:',wordcount)
print(int(covered), '% covered')
print('Missing:',dict2)




driver.close()