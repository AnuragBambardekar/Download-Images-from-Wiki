import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

r = requests.get(url=url, headers=headers)
# print(r)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)

soup.find('caption')
caption = soup.find('caption')
table = caption.parent
# print(table)

rows = table.find_all('tr')
# print(len(rows))

for row in rows[2:]:
    # print(row)
    src = row.th.span.img['src']
    # print(src)

    part = src.split('.svg')[0]
    # print(part)

    cleaned = part.replace('thumb/','')
    # print(cleaned)

    stripped = cleaned.strip('//')
    # print(stripped)

    img = "https://{}.svg".format(stripped)
    # print(img)

    # create a filename
    filename = img.split('/')[-1]
    # print(filename)

    # downlaod data [images]
    flag = requests.get(img, headers=headers)
    # print(flag.status_code)

    if flag.status_code != 200:
        print('Error getting {}'.format(filename))
    else:
        with open(filename, 'wb') as f:
            noop = f.write(flag.content)
            print('Saved {}'.format(filename))

# print(row.th.span.img['src']) # the last flag's link is returned