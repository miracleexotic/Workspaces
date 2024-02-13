## Install Ansible in Control-Node

Install Ansible Software

```sh
$ sudo apt-add-repository ppa:ansible/ansible && sudo apt update && sudo apt install ansible && ansible --version
```

Git clone Ubuntu22.04 branch

```sh
$ git clone -b Ubuntu22.04 --single-branch https://github.com/miracleexotic/Workspaces.git
```

Install Docker, Docker-compose

```sh
$ cd ~/Workspaces && sudo ansible-playbook -f install.yaml
```

## Configuration

Generate Self-Certification

```sh
$ cd ~/Workspaces/forescout-workspace/frontend/Certs && ./gen.sh
```

Run Docker-compose

```sh
$ cd ~/Workspaces/forescout-workspace
$ docker-compose -f docker-compose.yml up -d --build
```
