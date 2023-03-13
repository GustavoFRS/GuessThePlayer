from bs4 import BeautifulSoup
from lxml import html
from multi_key_dict import multi_key_dict
import requests
import pandas as pd

#Sofifa homepage was chosen due to it being short & dynamic (changes daily with transfer gossip, performance, etc.)
url = 'https://sofifa.com/players?type=all&lg%5B0%5D=13&offset=180'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, features='lxml')
player_table = soup.select('tbody.list')[0]

a_tags = player_table.find_all('a')
img_tags = player_table.find_all('img')
div_tags = player_table.find_all('div')

nicknames = [el.text for el in a_tags if '/player/' in el.get('href')]
names = [x.get('aria-label') for x in a_tags if '/player/' in x.get('href')]
club = [el.text for el in a_tags if '/team/' in el.get('href')]
country = [el.get('title') for el in img_tags if 'flag' in el.get('class')]

#Logic for getting position is diffrent because most can play multiple positions, but the first one is his main.    
posicao = []
for x in soup.select('td.col-name'):
    tags = x.find_all('span')
    vals = [y.text for y in tags]
    if vals != [] and vals != ['On Loan']:
        posicao.append(vals[0])    
        
zipped = list(zip(nicknames, country, posicao, club))
df = pd.DataFrame(zipped, columns=['Name', 'Country', 'Position', 'Club'])

#Changing from specific to general positions to make the game harder
general_positions = multi_key_dict()
general_positions['ST', 'CF'] = 'Striker'
general_positions['LM', 'LW', 'RM', 'RW'] = 'Winger'
general_positions['CDM', 'CM', 'CAM'] = 'Midfielder'
general_positions['CB', 'GK'] = 'Defender/Goalkeeper'
general_positions['RB', 'RWB', 'LB', 'LWB'] = 'Fullback'


for position in df['Position']:
    df['Position'] = df['Position'].replace([position], general_positions[position])

