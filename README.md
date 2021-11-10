# Python script for Sensirion SPS30
Python script to save data from Sensirion SPS30 particulate matter sensor

Use with USB serial adapter (/dev/ttyUSB0)
==

This is recommended as it leaves the serial port on the Raspi header for serial login

Autostart on boot
==
Suppose the repo was cloned into folder /home/pi/Python-Sensirion-SPS30/ by using 
```
pi@raspberrypi:~ $ cd ~
pi@raspberrypi:~ $ git clone https://github.com/FrankBau/Python-Sensirion-SPS30.git
```
Create & edit a new file 
```
pi@raspberrypi:~ $ sudo nano /etc/systemd/system/sps30.service
```
with content
```
[Unit]
Description=sps30 particle matter sensor
After=multi-user.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Python-Sensirion-SPS30
ExecStart=/usr/bin/python3 /home/pi/Python-Sensirion-SPS30/log_1_sec.py
StandardOutput=null
#Restart=always
#RestartSec=5
StartLimitBurst=5
StartLimitInterval=1m
StartLimitAction=reboot

[Install]
WantedBy=multi-user.target
```

Test with
```
pi@raspberrypi:~ $sudo systemctl start sps30.service
pi@raspberrypi:~ $ journalctl -b -u sps30.service
pi@raspberrypi:~ $sudo systemctl stop sps30.service
```

If it works as expected, make the service run automatically after boot:
```
pi@raspberrypi:~ $sudo systemctl enable sps30.service
```
If you want to undo that later:
```
pi@raspberrypi:~ $sudo systemctl disable sps30.service
```

Use with Raspi header serial port (with PL011 UART):
==
Advanced method because you cannot login via that serial port anymore!

disable Bluetooth:
```
sudo vi /boot/config.txt
```
add a new line
```
dtoverlay = disable-bt
```
disable serial console on serial0 
```
sudo vi /boot/cmdline.txt
```
remove
```
console=serial0,115200
```
finally
```
sudo reboot
```
see https://di-marco.net/blog/it/2020-06-06-raspberry_pi_3_4_and_0_w_serial_port_usage/

