#!/bin/bash

sed -i 's/dc=example,dc=com/dc=eip,dc=local/g' /etc/phpldapadmin/config.php

sed -i "s/127.0.0.1/$HNAME/g" /etc/phpldapadmin/config.php
/usr/local/bin/apache2-foreground

