import time
import speedtest


st = speedtest.Speedtest()


while True:
    down = st.download()
    up = st.upload()
    print(down, up)
    print('------------'*3)
    time.sleep(60)