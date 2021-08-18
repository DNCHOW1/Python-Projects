from bs4 import BeautifulSoup
import requests, re, os, time, json, selenium
#from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
login_url = 'https://www.x2vol.com/post'
opp_url = 'https://www.x2vol.com/Opportunities/1511380/FindOpportunities/'

login = {"button":"SignIn","UserName":"***","Password":"***","LoginFrom":"sample"}

head = {'Cookie': 'cook'}
head2 = {'Content-Type': 'text/html; charset=utf-8'}

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

with requests.Session() as session:
    r = session.post(login_url, cookies=head)
    print(r.url)


def execute():
    with requests.Session() as session:
        #print('t')
        r = session.post(login_url, cookies=head)
        print(r.text)
        #print(r.content)
        t = session.get(opp_url)
        #print(t.url)
        soup = BeautifulSoup(t.content, 'html.parser')

    current_opps = []
    past_ = []

    p = soup.find('h2').text
    #current_opps.append(p[-3:].strip())

    for i in soup.find_all('a', class_='blueHedline'):
        current_opps.append((i.text).lstrip().rstrip())

    #print(current_opps)
    txt_path = os.path.join(os.getcwd(), 'past_opportunities.txt')
    with open(txt_path, 'r') as f:
        for i in f:
            past_.append(i.rstrip('\n'))

    def display_opps(path_, list1, list2):
        x = []
        if path_ == 1:
            for i in list1:
                if i not in list2:
                    x.append(i)
        if len(x) > 0:
            print('New Opportunities:')
            for i in range(len(x)):
                print('{}) '.format(i + 1) + x[i])

    past_.pop(0)
    if len(current_opps) >= len(past_):
        display_opps(1, current_opps, past_) # Because the current opportunities exceeds past
    with open(txt_path, 'w') as f:
        f.write(p + '\n')
        for i in current_opps:
            f.write(i + '\n')

#execute()

'''while True:
    scheduler = BackgroundScheduler()
    scheduler.add_job(execute, 'interval', seconds=3)
    scheduler.start()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()'''
