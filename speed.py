import time
import i2clcd
import speedtest


def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n] + "B"


def limit_float(f, limit):
    s = ""
    if f > 10:
        s = f"{int(f)}"
    else:
        s = f"{int(f)}.{int((f*10)%10)}"
    return s[:limit]


lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x3F, lcd_width=16)
lcd.init()
lcd.print_line("Scanning started", line=0)
lcd.print_line("by Prodigy.by", align="RIGHT", line=1)
st = speedtest.Speedtest()

try:
    while True:
        down = st.download()
        up = st.upload()

        down_speed, down_postfix = format_bytes(down)
        up_speed, up_postfix = format_bytes(up)
        down_speed = limit_float(down_speed, 2)
        up_speed = limit_float(up_speed, 2)

        lcd.print_line(f"U:{up_speed}{up_postfix} D:{down_speed}{down_postfix}", line=0)
        time.sleep(60)

except KeyboardInterrupt:
    lcd.print_line("Scanning stopped", line=0)
