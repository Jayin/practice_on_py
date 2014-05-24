#coding=utf-8
import requests
from tc import Test
import re
from bs4 import BeautifulSoup
#see QuickStart https://github.com/kennethreitz/requests/blob/master/docs/user/quickstart.rst

regex = r'charset=([a-zA-Z0-9-]+)?'
pattern = re.compile(regex, re.IGNORECASE)


@Test
def test():
    response = requests.get('https://github.com/timeline.json')
    r = response
    # for parame in response.__dict__:
    #     print
    #     print parame, ":"
    #     print response.__dict__.get(parame)
    print r.text


def wyu_news(page):
    url = 'http://www.wyu.cn/news/default.asp'
    params = {'page': page}
    r = requests.get(url, params=params)
    encoding = pattern.findall(r.content)[0]
    return r.content.decode(encoding)  #Binary Response Content


def get_table(tag):
    try:
        if (tag.attrs['border'] == '0' and tag.attrs['cellspacing'] == '3' and tag.attrs['width'] == '100%' and
                    tag.attrs['cellpadding'] == '2'):
            return True

    except KeyError:
        pass
    return False


def get_a(tag):
    if tag.has_attr('href') and tag.has_attr('target'):
        if 'http://' in tag.attrs['href'] :
            return False
        return True
    return False


@Test
def main():
    res = wyu_news(1)
    soup = BeautifulSoup(res, from_encoding='utf-8')
    tds = soup.find_all(get_a)
    for x in tds:
        print ''.join(('http://www.wyu.cn/news/',x.attrs['href']))
        print x.string
    print len(tds)


main()