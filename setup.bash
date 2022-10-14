echo INSTALLING NODEJS...
cd ~
curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
sudo bash /tmp/nodesource_setup.sh
sudo apt install nodejs
echo ENABLING YARN...
sudo corepack enable
echo INSTALLING PYTHON3...
sudo apt install python3
sudo apt install python3.10-venv
echo FINISHED

