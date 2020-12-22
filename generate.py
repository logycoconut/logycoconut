import requests
import time
from lxml import etree

root = 'https://logycoco.xyz'
resp = requests.get(root + '/posts')
resp.encoding = 'utf-8'
html = etree.HTML(resp.text)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(r'''
```
                        __                                              __ 
                       / /___  ____ ___  ___________  _________  __  __/ /_
                      / / __ \/ __ `/ / / / ___/ __ \/ ___/ __ \/ / / / __/
                     / / /_/ / /_/ / /_/ / /__/ /_/ / /__/ / / / /_/ / /_  
                    /_/\____/\__, /\__, /\___/\____/\___/_/ /_/\__,_/\__/  
                            /____//____/                                                                    
```


''')

    localtime = time.strftime(" %b %d %Y", time.localtime()) 
    f.write('## Latest ( Update On {} )\r\n'.format(localtime))

    items = html.xpath("//article[@class='archive-item']")[:5]

    for item in items:
        title = item.xpath("a/text()")[0]
        href = root + item.xpath("a/@href")[0]
        date = item.xpath("span/text()")[0].strip()

        f.write('* {} - [{}]({}) \r\n'.format(date, title, href))

    f.write('''
[>>> More](https://logycoco.xyz/posts/)
## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=logycoconut)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=logycoconut&hide=html&layout=compact)
''')
