# container-cloudflare-tunnel
A Docker Compose container setup for a [Cloudflare tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/).

## Setup
### Requirements
- Docker
- Docker Compose
- this setup assumes that [Cloudflare](https://www.cloudflare.com/) is the DNS provider for your domain.

### Add environment variables

Add the missing information for the environment variables and host information:

```sh
$ nano .env
$ nano config/hosts
```

Mark the `.env` and `hosts` file so they will not be tracked by git:

```sh
$ git update-index --assume-unchanged .env
$ git update-index --assume-unchanged config/hosts
```
___
## Usage
### Start container
```sh
$ docker compose up -d
````

### Stop container
```sh
$ docker compose down
```
