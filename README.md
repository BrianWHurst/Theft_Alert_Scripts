# Theft_Alert_Scripts
security.sh and email.py components required for the localhost theft alert system

Dependencies:
python 2.7-3.0
pip
yagmail client

Installation Instructions:
**Edit security.sh and emailer.py
to reflect your applicable values!**

- Copy scripts to /usr/bin -

1. chmod 755 security.sh emailer.py
2. sudo chown root:root security.sh emailer.py
3. sudo cp -a security.sh emailer.py /usr/bin

- Install Python, pip, and yagmail -
(on Debian Jessie)
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install python
4. sudo apt-get install pip
5. sudo pip install yagmail

- Create a Systemd Unit -

sudo vim /etc/systemd/system/security.service

(This will be the configuration file that executes
security.sh)

EXAMPLE systemd Unit File:

# This unit file starts security.sh
# Added by Brian Hurst on 7/26/16

[Unit]
Description=security script for CIS240L
After=syslog.target
After=networking.target

[Service]
ExecStart=/usr/bin/security.sh

[Install]
WantedBy=multi-user.target

- Reload the systemctl daemon -

sudo systemctl daemon-reload

- enable security.service - 

sudo systemctl enable security.service

- DONE -
