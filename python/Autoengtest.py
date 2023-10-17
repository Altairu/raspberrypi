import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service

def split_list(l, n):
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]

driver = webdriver.Chrome(executable_path="C:\\Users\\106no\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")#chromedriver のパス

driver.get("https://moodle2.maizuru-ct.ac.jp/moodle/mod/quiz/view.php?id=59604")#テスト URL

login_button = driver.find_element(by=By.NAME, value="username")
login_button.send_keys('s9123') #学籍番号
pass_button = driver.find_element(by=By.NAME, value="password")
pass_button.send_keys('Shion-1031') #パスワード
next = driver.find_element(by=By.ID, value="loginbtn")
next.click()

try:
    zyuken = driver.find_element(by=By.XPATH, value='//*[@id="region-main"]/div[1]/div[3]/div/form') 
    zyuken.click()
    kaisi = driver.find_element(by=By.ID, value="id_submitbutton") 
    kaisi.click()
except:
    tuduki = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div/section/div[1]/div[2]/div/form/button') 
    tuduki.click()


#csv 読み込み
with open('eigo.csv') as f:
    kaitou = list(csv.reader(f))


mondai = driver.find_elements(by=By.CLASS_NAME,value='qtext') 
sentaku = driver.find_elements(by=By.CSS_SELECTOR,value='.flex-fill.ml-1') 

sentakusi = []
for a in range(len(sentaku)):
    sentakusi.append(sentaku[a].text)#選択肢を webelement からテキスト化

yontaku = list(split_list(sentakusi,4))#選択肢を 4×n の配列に

for n in range(len(mondai)):#n 問解く
    print(mondai[n].text)
    for i in range(len(kaitou)):#問題の数だけ
        if mondai[n].text == kaitou[i][0]:
            print("問題一致")
        for j in range(4):
            if yontaku[n][j] == kaitou[i][1]: 
                #回答一致
                mark = driver.find_element(by=By.XPATH, 
value=f"/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[{n+1}]/div[2]/div/div[2]/div[1]/div[{j+1}]") 
                mark.click()
                break
            else:
                continue
            break
        else:
            continue

print("1 ページ終わり")
tugi = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[51]/input') 
tugi.click()

mondai2 = driver.find_elements(by=By.CLASS_NAME,value='qtext') #50 個
sentaku2 = driver.find_elements(by=By.CSS_SELECTOR,value='.flex-fill.ml-1') #200 個

sentakusi2 = []
for a2 in range(len(sentaku2)):
    sentakusi2.append(sentaku2[a2].text)

yontaku2 = list(split_list(sentakusi2,4))

for n2 in range(len(mondai2)):
    print(mondai2[n2].text)
    for i2 in range(len(kaitou)):
        if mondai2[n2].text == kaitou[i2][0]:
            print("問題一致")
            for j2 in range(4):
                if yontaku2[n2][j2] == kaitou[i2][1]:
                    xpath = f"/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[{n2+1}]/div[2]/div/div[2]/div[1]/div[{j2+1}]"
                    mark = driver.find_element(by=By.XPATH, value=xpath) 
                    mark.click()
                    break
                else:
                    continue
            break
        else:
            continue

syuryo = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div/section[1]/div[1]/form/div/div[51]/input[2]') 
syuryo.click()

sousin= driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div/section[1]/div[1]/div[3]/div/div/form/button') 
sousin.click()

time.sleep(2)
kakunin = driver.find_element(By.XPATH, value="/html/body/div[4]/div[3]/div/div[2]/div/div[2]/input[1]")kakunin.click()
