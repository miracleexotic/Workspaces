## Install Ansible in Control-Node

Install Ansible Software

```sh
$ sudo apt-add-repository ppa:ansible/ansible && sudo apt update && sudo apt install ansible && ansible --version
```

Git clone Ubuntu22.04 branch

```sh
$ git clone -b develop --single-branch https://github.com/miracleexotic/Workspaces.git
```

Install Docker, Docker-compose
[Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Configuration

Generate Self-Certification

```sh
$ cd ~/Workspaces/forescout-workspace/frontend/Certs
$ ./gen.sh
```

Run Docker-compose

```sh
$ cd ~/Workspaces/forescout-workspace
$ docker-compose -f docker-compose.yaml up -d --build
```
