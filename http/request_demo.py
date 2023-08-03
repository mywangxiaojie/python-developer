import requests
import re

# login_url  = 'https://github.com/login'
# user = 'user'  
# password  = 'password'   
# user_headers = {
#     'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
#     'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding' : 'gzip',
#     'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
# }

# session  = requests.Session()
# response = session.get(login_url, headers = user_headers)
# pattern = re.compile(r'<input name="authenticity_token" type="hidden" value="(.*)" />')

# authenticity_token = pattern.findall(response.content)[0]

# login_data = {    
#     'commit' : 'Sign in',    
#     'utf8' : '%E2%9C%93',    
#     'authenticity_token' : authenticity_token,'login' : user,    
#     'password' : password
# }

# session_url  = 'https://github.com/session'
# response = session.post(session_url, headers = user_headers, data = login_data, cert=False)

# print(response.status_code)


# https://pixabay.com/zh/

proxies={
    'http':'127.0.0.1:7890',
    'https':'127.0.0.1:7890'
}


def test():
    res = requests.get('https://www.pexels.com/zh-cn/login/', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Host':'pexels.com'}, allow_redirects=True, proxies=proxies)
    print(res.status_code)
    # print(res.headers['content-type'])
    print(res.encoding)
    print(res.text)
    print(res.request.headers)

def test3():
    url = 'https://www.pexels.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Host':'pexels.com'} 
    loc = url
    seen = set()
    while True:
        r = requests.get(loc, headers=headers, allow_redirects=False)
        # print(r.headers)
        # print(r.status_code)
        # print(r.url)
        # print(r.history)
        # print(r.cookies)
        # print(r.encoding)
        # print(r.request.headers)
        # print(r.request.method)
        print( r.headers['location'])


        # if 'location' not in r.headers: break
        loc = r.headers['location']
        if loc in seen: break
        seen.add(loc)
        print(loc)

def test4():
    url = 'https://www.pexels.com/zh-cn/login/'
    s = requests.session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    s.headers['Host'] = 'pexels.com'
    s.headers['Referer'] = 'https://www.pexels.com/'
    r = s.get(url)
    print(r.status_code)
    print(r.text)


def test3():
    url = 'https://www.pexels.com/zh-cn/login/'
    s = requests.session()




def test2():
    url = 'http://www.amazon.in/b/ref=sa_menu_mobile_elec_all?ie=UTF8&node=976419031'
    loc = url
    seen = set()
    while True:
        r = requests.get(loc, allow_redirects=False)
        print(r.headers)
        loc = r.headers['location']
        if loc in seen: break
        seen.add(loc)
        print(loc)

def test1():
    res = requests.get('https://www.baidu.com/', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Host':'baidu.com'})
    print(res.status_code)
    print(res.headers['content-type'])
    print(res.encoding)
    print(res.text)

if __name__ == '__main__':
    test4()