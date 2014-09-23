# to run the django project:

### install virtualenv:
apt-get install python-virtualenv

### then create a virtual environment for the project, we call it 'venv' as it is already omitted by git through the gitignore
to do so run
virtualenv --no-site-packages venv

### this creates a micro-system inside the new 'venv' folder
inside it we find familiar looking system files, thant enable a virtual python environment

### to launch the system run
source venv/bin/activate

the terminal indicates that we're now inside tu virtual environment with it's name in brackets before your system name
to deactivate, run 
deactivate

### once you've launched the venv, you're able to get all the project dependencies/requirements through pip;
pip install -r requirements.txt

### then, in the folder medor, copy the local_settings.example.py file onto local_settings.py
cd medor
cp local_settings.example.py local_settings.py

### edit the new file, and add in your SECRET_KEY where required, look this up in your favourite search engine if you don't have one yet

### if pip is done installing and the SECRET_KEY is at the right place in the local_settings.py, grab the database by running
python manage.py migrate

### off you go then, launch the server:
python manage.py runserver

### head over to localhost:8000 (if you've not changed the default port settings) and get to work!

