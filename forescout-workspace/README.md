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

```sh
$ cd ~/Workspaces/forescout-workspace
$ sudo ansible-playbook install.yaml
$ sudo su - $USER
```

## Configuration

Generate Self-Certification

```sh
$ cd ~/Workspaces/forescout-workspace/frontend/Certs
$ sudo sh ./gen.sh
```

Run Docker-compose

```sh
$ cd ~/Workspaces/forescout-workspace
$ docker-compose -f docker-compose.yaml up -d --build
```
