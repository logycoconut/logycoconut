import requests
from lxml import etree

text = requests.get('https://logycoco.xyz/posts/').text
html = etree.HTML(text)

with open('README.md', 'w') as f:
    f.write(r'''
            ```
    __                                              __ 
   / /___  ____ ___  ___________  _________  __  __/ /_
  / / __ \/ __ `/ / / / ___/ __ \/ ___/ __ \/ / / / __/
 / / /_/ / /_/ / /_/ / /__/ /_/ / /__/ / / / /_/ / /_  
/_/\____/\__, /\__, /\___/\____/\___/_/ /_/\__,_/\__/  
        /____//____/                                                                    
            ```
            ## Latest blog posts
            ''')

    items = html.xpath("//article[@class='archive-item']")

    for item in items :
        title = item.xpath("a/text()")[0]
        href = item.xpath("a/@href")[0]
        date = item.xpath("span/text()")[0]
        
        f.write('[{}]({}) - {}\n'.format(title, href, date))

    f.write('''
    [>>> More blog posts](https://logycoco.xyz/posts/)
    ## Statistics
    ![Stats](https://github-readme-stats.vercel.app/api?username=logycoconut)
    ![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=logycoconut&hide=html&layout=compact)
    ''')