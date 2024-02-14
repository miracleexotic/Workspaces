# https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl
# https://stackoverflow.com/questions/44574399/create-react-app-how-to-use-https-instead-of-http

cp init.conf gen.conf
IP=$(ip -o address | head -n 3 | tail -n 1 | cut -d ' ' -f 7 | cut -d '/' -f 1)
echo IP-ADDRESS: $IP
sed -i "s/<IP-ADDRESS>/$IP/g" gen.conf
# openssl req -config gen.conf -new -x509 -sha256 -newkey rsa:2048 -nodes -keyout key.pem -days 365 -out cert.pem
openssl req -config gen.conf -new -x509 -sha256 -newkey rsa:2048 -nodes -keyout cert.key -days 365 -out cert.crt
# openssl rsa -outform der -in key.pem -out cert.key
# openssl x509 -outform der -in cert.pem -out cert.crt
rm gen.conf
