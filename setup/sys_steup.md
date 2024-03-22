
update_os
```
sudo apt update
```

bluetooth_setup (debian)
```
sudo apt install bluez*
sudo apt install blueman
sudo apt install blueman (only if usb dongle to connect)
sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service
```

bluetooth-status (debian)
--checking bluetooth status
```
sudo apt update
sudo apt-get install bluez
sudo systemctl status bluetooth.service
sudo systemctl stop bluetooth.service
sudo systemctl start bluetooth.service
sudo systemctl status bluetooth.service
```

bluetooth-connection (debian)
--connecting devices and get raw data 

--hcitool (decripted)
```
sudo hcitool lescan

```
--using bluetoothctl
```
bluetoothctl
scan on
connect [mac-address]
help
menu gatt
help
list-attributes
select-attribute [attribute-id like 000180d-0000-1000-00805f9b34fb]
notify on
```
text-editor (debian)

```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```