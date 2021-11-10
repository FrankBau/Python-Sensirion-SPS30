# Python script for Sensirion SPS30
Python script to save data from Sensirion SPS30 particulate matter sensor



Use on Raspi serial port (with PL011 UART):



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

