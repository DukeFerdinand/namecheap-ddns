## Namecheap DDNS
Leverage Namecheap's DDNS to do run things like web servers at home.

### Quickstart
- Use the [docker image](https://hub.docker.com/repository/docker/dougflynndev/namecheap-ddns/general)
(images are provided for arm64 machines like the Raspberry Pi 4 - and amd64 computers)
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
  