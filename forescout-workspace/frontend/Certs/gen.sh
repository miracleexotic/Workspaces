# https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl
# https://stackoverflow.com/questions/44574399/create-react-app-how-to-use-https-instead-of-http

openssl req -config gen.conf -new -x509 -sha256 -newkey rsa:2048 -nodes -keyout key.pem -days 365 -out cert.pem
