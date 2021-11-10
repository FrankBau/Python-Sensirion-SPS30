#! /usr/bin/python3

""" Program to read and save data from Sensirion SPS30 sensor

	by
	Szymon Jakubiak
	Twitter: @SzymonJakubiak
	LinkedIn: https://pl.linkedin.com/in/szymon-jakubiak

	MIT License

	Copyright (c) 2018 Szymon Jakubiak

	Permission is hereby granted, free of charge, to any person obtaining a copy of 
	this software and associated documentation files (the "Software"), to deal in the 
	Software without restriction, including without limitation the rights to use, copy, 
	modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
	and to permit persons to whom the Software is furnished to do so, subject to the 
	following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
	INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
	PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
	HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
	OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

	Units for measurements:
		PM1, PM2.5, PM4 and PM10 are in ug/m^3, numerical concentrations are in #/cm^3
"""
import sps30, time

from gpiozero import CPUTemperature

# Specify serial port name for sensor
# i.e. "COM10" for Windows or "/dev/ttyUSB0" for Linux
#device_port = "/dev/ttyAMA0"
device_port = "/dev/ttyUSB0"

sensor = sps30.SPS30(device_port)
sensor.start()
time.sleep(5)

try:
	while True:
		output = sensor.read_values()
		sensorData = ""
		for val in output:
			sensorData += f"{val:.2f}; "
		date = time.localtime()
		temp = CPUTemperature().temperature


		output_file = f"{date[0]:04d}-{date[1]:02d}-{date[2]:02d}.csv"
		output_data = f"{date[0]:04d}-{date[1]:02d}-{date[2]:02d} {date[3]:02d}:{date[4]:02d}:{date[5]:02d}; "
		output_data = output_data + f"{temp:.1f}; " + sensorData[:-1] # remove comma from the end

		file = open(output_file, "a")
		file.write(output_data + "\n")
		file.close()
		print(output_data)

		time.sleep(1)

except KeyboardInterrupt:
	sensor.stop()
	sensor.close_port()
	print("Data logging stopped")
