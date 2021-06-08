import sys, time, requests

while True:
    resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
    print(resp.text)
    time.sleep(30000) #30000 = 30 sec, 600000 = 10 min