from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from bs4 import BeautifulSoup as bs
from google_trans_new import google_translator

t = google_translator()

loginPage = 'https://tools.tracemyip.org/login/:-v-:rdMSID=NTIwMDkzNA==&lGou=1'
ipPage = 'https://tools.tracemyip.org/search--country/china:-v-:gTr=851&gNr=50'

driver = webdriver.Firefox()
#options = webdriver.FirefoxOptions()
#options.add('headless')

# Logging in
driver.get(loginPage)
login = driver.find_element_by_name('login_id')
login.send_keys('weichenslav@qq.com')
password = driver.find_element_by_name('password')
password.send_keys('Tp0d0tp0r')
btn = driver.find_element_by_name('button_id')
btn.click()

# Getting IPs
data = []
try:
    driver.get(ipPage)
    for i in range(0, 50):
        html = driver.page_source
        soup = bs(html, 'html.parser')
        table = soup.find('table', {'id':'tlzRDTIPv4'})
        tbody = table.find('tbody')
        rows = table.findAll('tr')
        rows.remove(rows[0])
        for row in rows:
            cells = row.findAll('td')
            ip = cells[1].text
            state = cells[4].text
            city = cells[5].text
            if state != '- - -' and city != '- - -':
                data.append(ip + ' ' +
                             t.translate(state[0].lower()+state[1:], 'zh') + ' ' +
                             t.translate(city[0].lower()+city[1:], 'zh') + '\n'
                             )
        print(str(i+1)+'/50 pages have been scraped')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        nxt = driver.find_element_by_name('pgBtnNextB')
        nxt.click()
except:
    print('Something went wrong')
finally:
    driver.close()
    file = open('ips.txt', 'w', encoding='utf-16')
    file.writelines(data)
    file.close()
