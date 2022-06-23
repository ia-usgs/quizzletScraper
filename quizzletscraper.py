# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:55:05 2022

@author: irvin
"""

import requests
from bs4 import BeautifulSoup

#Input your quizzlet URL here
url = 'https://quizlet.com/63149831/c-midterm-flash-cards/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

for num, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
    print('QUESTION {}'.format(num))
    print()
    print(question.get_text(strip=True, separator='\n'))
    print()
    print('ANSWER:')
    print(answer.get_text(strip=True, separator='\n'))
    print('-' * 100)
    print('-' * 100)