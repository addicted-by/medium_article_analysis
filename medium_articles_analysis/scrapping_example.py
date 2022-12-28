from medium_scrapper import scrap_articles_async_list, get_desired_options
from selenium.webdriver.edge.options import Options
import pandas as pd

links = ['https://medium.com/swlh/handling-exceptions-in-python-a-cleaner-way-using-decorators-fae22aa0abec',
         'https://medium.com/codex/say-goodbye-to-loops-in-python-and-welcome-vectorization-e4df66615a52',
         'https://medium.com/geekculture/hey-chatgpt-solve-these-coding-tasks-using-python-b2e7482f2c18',
         'https://medium.com/@markwschaefer/20-entertaining-uses-of-chatgpt-you-never-knew-were-possible-3bc2644d4507',
         'https://medium.com/bitsrc/i-asked-chat-gpt-to-build-a-to-do-app-have-we-finally-met-our-replacement-ad347ad74c51'            
]

options = get_desired_options()


scrap_articles_async_list(links, options, path="./check.csv")