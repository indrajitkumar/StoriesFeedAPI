# StoriesFeedAPI
A web services for feeding Stories with image and text content. These APIs with perform add, update and delete the stories into the server.
It contains, User authentication and permission to add feed with image by authenticated user.<br><br>
This can be helpful to learn the Rest API implementation in Python Django-rest Framework. 

Setup project and run with following steps<br>
## Install virtual environment
sudo apt install python-virtualenv

## Setup virtual environment with python 3.6+<br>
virtualenv venv -p python3

## Install python dependencies<br>
pip install -r requirements.txt

## Migrate database<br>
``python manage.py makemigrations stories_api `` <br>
``python manage.py migrate``<br>
If Sync reuired,then use 
`` python manage.py migrate --run-syncdb
``


## Run server</b>
python manage.py runserver 0.0.0.0:5000

## Test on browser<br>
http://localhost:5000

##To run on EC2 instance
ssh ubuntu@ec2-3-6-41-100.ap-south-1.compute.amazonaws.com

#### Install all required dependencies in EC2 instance by 
curl -sL https://raw.githubusercontent.com/indrajitkumar/StoriesFeedAPI/master/deploy/setup.sh | sudo bash -
 
 You can see project in EC2 instance:<br>
 `cd /usr/local/apps`
 then 
 `sudo sh ./deploy/update.sh` for updating the changes from git and restart the server after migration of database.

