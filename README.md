

# Zabbix API bulk import

## Codes for use Zabbix API
   
## Installation

You need lib zabbix-api progressbar and  pip


 apt-get install python-pip git

pip install zabbix-api
pip install lib
pip install progressbar


## How to use - examples

#### bulkimport.py

>Structure hosts.csv file (csv file must be in smae directory as script)

```sh
hostname;ipaddress;macaddress
hostname;ipaddress;macaddress
hostname;ipaddress;macaddress
hostname;ipaddress;macaddress
hostname;ipaddress;macaddress
Host001;0.0.0.0;000000000000

```

>then run 

```sh
python bulkimport.py
```


