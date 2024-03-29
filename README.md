# Open Vehicle Tracking System

![OVTS](./images/banner.png)

[![Build Status](https://travis-ci.org/Open-VTS/OVTS-Server.svg?branch=master)](https://travis-ci.org/Open-VTS/OVTS-Server)
[![Coverage Status](https://coveralls.io/repos/github/Open-VTS/OVTS-Server/badge.svg?branch=master)](https://coveralls.io/github/Open-VTS/OVTS-Server?branch=master)

## OVTS Overview

[OVTS](https://github.com/Open-VTS) is an Open-source Vehicle Tracking System project based on GPS. It can track the device based on GPS data and send information to the main server (AKA Center). It can be mounted on a car or any other vehicles. The communication is over on GPRS and SMS. The device has other features like output relay, input voltage sensor, IMU sensor, etc. This project covers **Device-side**, **Server-side** and a **User Panel**.

This project is open source and is independent on **ANY ONLINE SERVICES**.

The project consists of four separate repositories:

* [OVTS-Device](https://github.com/Open-VTS/OVTS-Device)
* [OVTS-Server](https://github.com/Open-VTS/OVTS-Server)
* [OVTS-Panel](https://github.com/Open-VTS/OVTS-Panel)
* [OVTS-CenterApp](https://github.com/Open-VTS/OVTS-CenterApp)

## OVTS-Server

OVTS-Server is the Server (AKA Center) application of [OVTS](https://github.com/Open-VTS) project. This project is written with Python and based on the Django REST framework.

## OVTS-Server Features

* Fully written with **Python3.x**.
* Based on **Django 2.2**.
* Web API based on **Django Rest framework 3.10**.
* Built-in methods to communicate with Device and user panel.
  * Device Data
  * Center Commands
  * Device Reports
  * Add new Device
* Built-in testing for available methods.
* Separate Django Models for each method.
* Communicate with user panel app (in progress).
* Add SMS center app to receive Device SMS data.

## Usage

Clone the project and run below commands to start the server:

```shell
pip install -r requirements.txt
cd OVTS-Server
python manage.py migrate
python manage.py runserver
```

## TODO

* Add more secure protocols like HTTPS.
* Add device authentication.
* Complete User panel app communication methods to access device.
* Improve source code and documentation.

## Credits

* Masoud Rahimi: [masoudrahimi.com](http://masoudrahimi.com)
