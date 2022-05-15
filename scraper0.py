from ast import Return
from selenium import webdriver
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")

driver = webdriver.Chrome("c:/src/chromedriver.exe",options=opts)
url ="https://www.amazon.ca/s?me=A2HFA2QNCUMBI8&marketplaceID=A2EUQ1WTGCTBG2" #str(input("Url: "))


driver.get(url)
asins = []
sayfa = 2
for i in range(99**999):
    lnks=driver.find_elements_by_class_name("a-link-normal")

    # traverse list
    
    for lnk in lnks:
        # get_attribute() to get all href
        link = lnk.get_attribute("href")
        if "dp" in link:
            p = link.split("/")
            asin = p[5]
            #print(asin)

            asins.append(asin)

        else:
            pass

    new = list(set(asins))
    print(new)
    save = open("asins.txt","a")
    
    for item in new:
        save.write(str(item)+"\n")
        print(item)
    save.close()
    #driver.find_element_by_xpath("/html/body/div[1]/div[1]/span[3]/div[2]/div[18]/div/div/div/ul/li[2]/a").click()
    
    driver.get(url+"&page="+str(sayfa))
    asins = []
    print("işlemdeki sayfa: "+str(sayfa))
    sayfa = sayfa + 1

driver.quit()
save.close()
