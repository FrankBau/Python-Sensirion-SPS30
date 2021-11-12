# Python script for Sensirion SPS30
Python script to save data from Sensirion SPS30 particulate matter sensor

forked from szajakubiak/Python-Sensirion-SPS30

Use with USB serial adapter (/dev/ttyUSB0)
==

This is recommended as it leaves the serial port on the Raspi header for serial login. Just connect the USB-serial adapter to the sensor and the USB Port of the Raspi. A new serial device `/dev/ttyUSB0` should be present. As the serial communication with the sensor uses a dedicated protocol, the easiest way to test the sensor from the command line are the .py scripts:

Clone the repo into folder `/home/pi/Python-Sensirion-SPS30/` by 
```
pi@raspberrypi:~ $ cd ~
pi@raspberrypi:~ $ git clone https://github.com/FrankBau/Python-Sensirion-SPS30.git
```
Now you should be able to test the connected sensor:
```
pi@raspberrypi:~ $ cd ~/Python-Sensirion-SPS30
pi@raspberrypi:~ $ python3 log_1_sec.py
```
The script `log_1_sec.py` will output one line per second like
```
2021-11-12 11:10:07; 26.1; 16.74; 18.40; 18.95; 19.07; 110.67; 132.18; 133.59; 133.74; 133.78; 0.64;
2021-11-12 11:10:09; 25.6; 16.60; 18.24; 18.80; 18.91; 109.69; 131.03; 132.43; 132.59; 132.63; 0.63;
2021-11-12 11:10:10; 26.1; 16.61; 18.25; 18.81; 18.92; 109.75; 131.10; 132.50; 132.65; 132.69; 0.63;
...
```
The column headers are
```
yyyy-m-d h:m:s; CPU Temp.; PM1; PM2.5; PM4; PM10; 0.3÷0.5; 0.3÷1; 0.3÷2.5; 0.3÷4; 0.3÷10; typical size
```
Stop the output with Ctrl+C.

Note that the other script (log_interval) may be better suited for long-term measurements.

Autostart the script on boot
==
Suppose the repo was cloned as above.

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

