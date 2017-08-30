mkdir ~/certs
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/certs/nginx-selfsigned.key -out ~/certs/nginx-selfsigned.crt
sudo openssl dhparam -out ~/certs/dhparam.pem 2048

