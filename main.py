from selenium import webdriver
import csv

count = 0

with open('scraper.csv', 'wt', newline='') as neu:
    scraperfile = csv.writer(neu, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    url = ""
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/maps/place/Florida,+USA")

    while True:
        curl = driver.current_url
        dat = curl.split('/')
        if dat[5] != url:
            cat = dat[5].split(',')
            print(len(cat))
            print(cat)
            if len(cat) == 4:
                for x in range(len(cat)):
                    cat[x] = cat[x].replace('+', ' ')
                print(cat[0])
                scraperfile.writerow(cat)
                count += 1
                print(count)
            else:
                pass
            url = dat[5]
        else:
            pass
