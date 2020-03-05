# Room Wifi Service

_Demo POC using Cisco Meraki and a small web app to create and manage room wifi networks in an MDU environment._

---

This simple project was created to demonstrate an automated and/or semi-automated method to enable personal or room wifi networks for guests. The ideal consumer of this kind of service is a frequent traveler or long term guest that wants an easy way to onboard multiple wifi devices without configuring them.

By allowing a user to configure an SSID and PSK for her room, she can use configuration that may already be saved on all of her devices. This eliminates the need for guests to connect to wifi networks on each device they carry at each hotel, motel, apartment, inn, etc. they stay at.

Many devices like Apple TV or Chromecast use service discovery technologies like mDNS and using an automated process like in this POC would allow a provisioned wifi network to be tunneled to an MX firewall and homed to a guest DMZ. This improves service delivery to the customer and network security.

## Features

* Simple web interface
* Meraki Dashboard API integration


## Solution Components

The components used in this project:
* [Cisco Meraki cloud managed networking products](https://meraki.cisco.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/)
* [SQLite](https://www.sqlite.org/index.html)
* [SQLAlchemy ORM](https://www.sqlalchemy.org/)
* [Meraki Dashboard Python library](https://github.com/meraki/dashboard-api-python/)
* [Skeleton](http://getskeleton.com/)

### Cisco Products / Services

* Meraki MR
* Meraki MX
* Meraki Dashboard API


## Usage

### Adding a user
![](https://media.giphy.com/media/Pkjsl7dDRHaexqMNR1/giphy.gif)

### Registering a user (magic link could be send to user via email or sms)
![](https://media.giphy.com/media/j2G0ASq7TgqTKlqpB8/giphy.gif)

### Connecting to wifi
![](https://media.giphy.com/media/UvEcmr6jrPntI65FoA/giphy.gif)

### Deleting a user
![](https://media.giphy.com/media/VcvcsTlHBqfVi7Zz5m/giphy.gif)

## Installation
```
git clone https://github.com/CiscoSE/roomwifiservice
pip install -r requirements.txt
```
Set your Meraki organization name in config.py.

Create a virtual environment _(optional)_

```
python(3) -m venv .venv
source .venv/bin/activate
```
Run the flask app
```
python app.py
```
Browse to localhost or the hostname of the server

## Documentation

This demo was done in a few days, so no docs. :D