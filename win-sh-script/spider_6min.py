from requests_html import HTMLSession
session = HTMLSession()
# for index in ['http://www.en8848.com.cn/kouyu/brand/connect-with-english/index.html', 'http://www.en8848.com.cn/kouyu/brand/connect-with-english/index_2.html', 'http://www.en8848.com.cn/kouyu/brand/connect-with-english/index_3.html']:
#     r = session.get(index)
#     links = r.html.find('.ch_lii_left > a')
#     with open('foo.txt', 'a+') as f:
#         f.write('\n'.join([link.absolute_links.pop() for link in links]))
#
#
# with open('foo.txt', 'r') as f:
#     x = f.read()
#     a = [url for url in x.split('\n')]
# print(a)
#
# x = [f'http://mp3.en8848.com/kouyu/connect-with-english/{big}-{small}.mp3' for small in range(1, 4) for big in range(1, 49)]
# x.sort()
# print('\n'.join(x))

# r = session.get('http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/')
# with open('foo.txt', 'a+') as f:
#     x = '\n'.join([i for i in list(r.html.absolute_links) if i.startswith('http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-')])
#     f.write(x)

# with open('foo.txt', 'r') as f:
#     x = f.read()
#     yy = x.split('\n')
#     print(yy)
#     xx = sorted(x.split('\n'))
#     print(xx)
#     final = '\n'.join(sorted(x.split('\n')))
#
# with open('foo.txt', 'w+') as f:
#     f.write(final)

with open('foo.txt', 'r') as f:
    x = f.readline()

    r = session.get(x, headers={
        'Host': 'www.bbc.co.uk',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    })
    absolute_links = list(r.html.links)
    xx = []
    with open('foo.html', 'w+', encoding='utf-8') as f:
        f.write(r.html.full_text)
    # print('\n'.join(absolute_links))
    xx.append(r.html.find('div.widget-pagelink-download-inner.bbcle-download-linkparent-extension-pdf > a')[0].absolute_links.pop())
    xx.append(r.html.find('div.widget-pagelink-download-inner.bbcle-download-linkparent-extension-mp3 > a')[0].absolute_links.pop())
    # for link in absolute_links:
    #     if link.endswith('.pdf'):
    #         xx.append(link)

print(xx)
