base_dir=$(pwd)
echo INSTALLING NODEJS...
cd ~
curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
sudo bash /tmp/nodesource_setup.sh
sudo apt install -y nodejs
echo ENABLING YARN...
sudo corepack enable
echo INSTALLING PYTHON3...
sudo apt install -y python3 python3.10-venv python3-pip
echo INSTALLING DEPENDENCIES
cd ${base_dir}
source api/venv/bin/activate
pip install -r api/requirements.txt
echo FINISHED

