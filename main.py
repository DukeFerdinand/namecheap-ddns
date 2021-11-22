import os

from requests import get
from dotenv import load_dotenv

load_dotenv()

print("Starting Namecheap DDNS updater")

ipDict = get('https://api.ipify.org?format=json')
ip = ipDict.json()['ip']

if ip is None:
    raise IOError('Could not get ip from ipify.org. Please check logs and firewall!')

password = os.environ['PASSWORD']
if not password or password == '':
    raise EnvironmentError("Cannot find PASSWORD in env!")

domain = os.environ['DOMAIN']
sub_domains = os.environ['SUB_DOMAINS'].split(',')
if len(sub_domains) == 0 or domain == '':
    raise EnvironmentError("Either DOMAIN or SUB_DOMAINS is empty or invalid!")
for sub in sub_domains:
    print(f"> Updating {sub}.{domain}")
    request = f'https://dynamicdns.park-your-domain.com/update?host={sub}&domain={domain}&password={password}&ip={ip}'
    res = get(request)

