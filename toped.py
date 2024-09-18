from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

url='https://www.tokopedia.com/search?st=product&q=intisolar&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='

driver= webdriver.Chrome()
driver.get(url)

data=[]
for i in range(2):

    WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#zeus-root")))
    time.sleep(2)
    #Driver ditunggu 5s sampai selectornya (zeus-root) muncul, baru di sleep - untuk scroll window. tp kalo nggak pake scrolling window. tidak perlu syntax ini
    #Baru di sleep 2s dengan tujuan bahwa page nya benar2 terbuka

    for _ in range(20):
        driver.execute_script('window.scrollBy(0,250)')   ### Scroll window chrome ke bwh
        time.sleep(1)

    driver.execute_script('window.scrollBy(50,0)') ### untuk scroll ke kanan (jd pada saat akhir supaya bisa melihat jumlah page)
    time.sleep(1)

    soup=BeautifulSoup(driver.page_source,"html.parser")
    for i in soup.findAll('div', class_='css-974ipl'):
        nama=i.find('div', class_='prd_link-product-name css-3um8ox').text
        harga=i.find('div',class_='prd_link-product-price css-1ksb19c').text
        trj=i.findAll('span', class_='prd_label-integrity css-1duhs3e')
        if len(trj)>0:
            terjual=i.find('span', class_='prd_label-integrity css-1duhs3e').text
        else:
            terjual =''
        for j in soup.findAll('div', class_='css-1rn0irl'):
            lokasi=j.find('span', class_='prd_link-shop-loc css-1kdc32b flip').text
            toko=j.find('span', class_='prd_link-shop-name css-1kdc32b flip').text
        data.append((nama,harga,terjual,lokasi, toko))
        # print(nama)
        # print(harga)
        # print(terjual)
        # print(lokasi)
        # print(toko)
        # print('---------------------------------------------')

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
    time.sleep(3)

import pandas as pd
df=pd.DataFrame(data, columns=['Nama', 'Harga', 'Terjual', 'Lokasi', 'Toko'])
print(df)


driver.close()