from bs4 import BeautifulSoup

with open ('a.html') as f:
    html_content=f.read()

soup=BeautifulSoup(html_content,'html.parser')
result=soup.find_all('label')
initial_info=soup.find('form').find('div').find_all('input')#form's first div contains 3 very important parameters to be sent.
# in theory soup.find('form').find_all('input') can be used to get all parameters and set some to zero based on file presence
#BUT thats hectic we need to ignore a few stuff that is better when sorted and split at '_'
#SO we will make a separate list for them which will be dealt with logic and if it needs to be included it will be given 1
#else it will be given 0 but some 0 ones will be kept in record cuz they are important markers for week
#like "item_topic_2" tells week 2 resouces. so make a csv out of the list aswell for debugging as well as week tracking

params=[]#will eventually contain all params when other list is merged
for info in initial_info:#iterates through form tag's first div's 3 input tags cuz they have 3 params whose name and value are recorded
    params.append(info.get('name'))
    params.append(info.get('value'))

print(params)


idlist=[]#contains id of all resources and extra week folder
for label in result:
    # html does contain label tags that are not related to resources/ files we wanna download. they contain links and stuff
    # label tags with input tag inside them are ONLY in the form tag and those are the ONLYYY ones related to resources
    #there is no other label tag with an input tag which is not part of download list(file/folder/extra folder for week(part of params basically))
    if label.find('input')!=None:
        print(label.find('input').get('id'))
        idlist.append(label.find('input').get('id'))
        print(label.find('span').get_text())
idlist.sort()
print(len(idlist))
print(idlist)
#now make func to add thesese to params list but with conditions which ill decide and tune use spli at "_"



"""initial_info=soup.find('form').find_all('input')
params=[]
for info in initial_info:
    params.append(info.get('name'))
    params.append(info.get('value'))
print(params)   it gives allllllll parameters and 1 extra"""




"""label.find('input').get('id').split('_')[2]+'_'+label.find('input').get('id').split('_')[3]"""
"""print(result[1].prettify())
print(result[1].find('input'))
print(result[1].find('span'))"""


"""#result[8] has the links for subjects in <li> tags
# getting those links and text of link
a_tag=result[8].find_all('a')
#dictionary with links(link.get("href)) and their names (link.get_text()) flag keeps track of whether we are managing or not
links_and_names={'flag':[],'name':[],'links':[],'payload':[]}
"""