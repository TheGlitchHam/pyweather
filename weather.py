import sys, time, requests

while True:
    resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
    print(resp.text)
    time.sleep(600) #in secs
    print("Restarting")