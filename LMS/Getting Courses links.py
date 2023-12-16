from bs4 import BeautifulSoup
import  pandas

with open ('files/courseslist.html') as f:
    html_content=f.read()

soup=BeautifulSoup(html_content,'html.parser')
result=soup.find_all('li', class_='contentnode')#result[8] has the links for subjects in <li> tags
# getting those links and text of link
a_tag=result[8].find_all('a')
#dictionary with links(link.get("href)) and their names (link.get_text()) flag keeps track of whether we are managing or not
links_and_names={'flag':[],'name':[],'links':[],'payload':[]}

#populating the dictionary with links name and flag set to zero

for link in a_tag:
    thelink = 'https://lms.nust.edu.pk/portal/course/view.php?id='
    courseid=''
    for i in range(len(link.get("href"))-5,len(link.get("href"))):
        courseid+=link.get("href")[i]
    thelink+=courseid
    print(thelink)
    links_and_names['links'].append(thelink)
    links_and_names['name'].append(link.get_text())
    links_and_names['payload'].append(courseid)
    #flag keeps track of hwther the download for that subject is matained by program or not
    links_and_names['flag'].append(0)

print(links_and_names)
#reversing to sort semester wise because our links got extracted in ascending order and less value means older semester
#makes it more convenient for user when i give him a menu to choose subjects he wants to mantain
links_and_names['links'].reverse()
links_and_names['name'].reverse()
links_and_names['flag'].reverse()
links_and_names['payload'].reverse()
print(links_and_names)
data=pandas.DataFrame(links_and_names)
data.to_csv("files/Links_to_courses.csv",index=False)
######################################Links to coourses noted##########################################









"""
soup=BeautifulSoup(str(result[8]),'html.parser')
print(soup.prettify())
links=soup.find_all('a')
print(links)"""
"""i=0
for r in result:
    print(r)
    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')"""