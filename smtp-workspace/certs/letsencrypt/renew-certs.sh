# This will need access to port 443 from the internet, adjust your firewall if needed.
docker run --rm -it \
  -v "${PWD}/docker-data/certbot/certs/:/etc/letsencrypt/" \
  -v "${PWD}/docker-data/certbot/logs/:/var/log/letsencrypt/" \
  -p 80:80 \
  -p 443:443 \
  certbot/certbot renew
