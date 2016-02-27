# esp8266-cmd
===
Easy Command sender for esp8266.

Instead of sending the AT commands one by one, I made this script to read a file where the commands are listed (one per line)

#### Installing

This script has been devellop with python2. I will work on it to make it python3 accepted.

There is a depedency on ```pyserial```. If you don't use the setup file, you will need to install it manually or install it with pip

	pip install pyserial

Otherwise just run the setup file. Everything will be took care automaticly.

	python2 setup.py install

#### How to use

Create a file containing those lines:
	
	AT
	AT+CWMODE=1
	AT+CWLAP
	AT+CIFSR

Once the file save, you just have to run:
	
	espcmd commandfile

#### Things to be done

- Add the possibility to give in parameters the port and baudrate
- Make a better error handling. Right now, if it somethings goes wrong, it will crash yeak!
- Has error handling, do something if one of the AT command return an ```ERROR```
- Make the script accept to be run with python3. 