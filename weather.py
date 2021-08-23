import sys, time, requests

while True:
    resp = ""
    if len(sys.argv) == 2:
        resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
    else: 
        resp = requests.get('https://wttr.in')
    print(resp.text)
    time.sleep(3600) #in secs