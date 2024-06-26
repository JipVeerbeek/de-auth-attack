# Installation
```
python3 -m venv env
source env/bin/activate
pip install requirements.txt
```
> Get network interface names     

`iwconfig`    

> Create .env based on .env.template and add your interface name   

# Start probe   
```
sudo airmon-ng start interface_name
sudo $(which python) catch_probe.py
```
# Stop probe   

`sudo airmon-ng stop interface_name` Add 'mon' at the end (no space)    
> Example:    

`sudo airmon-ng stop interface_namemon`   