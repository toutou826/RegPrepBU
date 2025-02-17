import requests
from bs4 import BeautifulSoup


#Find teacher id
def findTeacher(aTeacher):
    url = "https://www.ratemyprofessors.com/search.jsp?query="

    name = '+'.join(aTeacher.lower().split(' '))

    sauce = requests.get(url+name)

    soup = BeautifulSoup(sauce.text, "html.parser")

    #Find the teacher id if the teacher searched is from BU
    link = None
    for li in soup.find_all('li',class_= 'listing PROFESSOR'):
        for uni in li.find('span',class_='sub'):
            if uni.split(',')[0] == "Boston University":
                link = li.find('a').get('href')
                break
    return link


# a = findTeacher("Dora Erdos")
# print(a)

#Use the teacher id found to find teacher Rating
def findRating(aLink):
    base_url = 'https://www.ratemyprofessors.com'

    sauce = requests.get(base_url+aLink)

    soup = BeautifulSoup(sauce.text, "html.parser")

    grades = soup.find_all('div', class_='grade')

    result = f'Quality: {grades[0].get_text().strip()}\nWould Take Again: {grades[1].get_text().strip()}\nDifficulty: {grades[2].get_text().strip()}\n'

    return result

# findRating(findTeacher("Dora Erdos"))