## Namecheap DDNS
Leverage Namecheap's DDNS to do run things like web servers at home.

### Quickstart
- Use the docker image
```shell
docker run \
    -e PASSWORD=ADDYOURPASSWORDHERE \
    -e DOMAIN=mydomain.com \
    -e SUB_DOMAINS=www,api \
    -it dougflynn/namecheap-ddns
```

### OR Manually run source code
- First, `git clone` the repo,
- Then, `cp .env.example .env` and populate your secrets
- Then pick a way to run

#### Docker (recommended)
- Run `docker build -t namecheap-ddns .`
- Then run:
```shell
docker run \
    -e PASSWORD=ADDYOURPASSWORDHERE \
    -e DOMAIN=mydomain.com \
    -e SUB_DOMAINS=www,api \
    -it namecheap-ddns
```

#### Raw Python
- Run `python -m venv venv`
- Then `source ./venv/bin/activate`
- Install deps `pip install -r requirements.txt`
- Finally `python -u main.py`
  