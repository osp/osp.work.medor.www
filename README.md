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

### when pip is done and if you're starting from scratch grab the database by running
python managa.py migrate
