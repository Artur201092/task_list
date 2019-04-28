Install Python PIP

    sudo apt-get install python-pip

Install virtualenvwrapper

    sudo pip3 install virtualenvwrapper
    sudo pip3 install --upgrade virtualenv


Create www directory where project sites and environment dir

    mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin


Add these to your bashrc virutualenvwrapper work

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    source /usr/local/bin/virtualenvwrapper.sh

Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 tasks_list
    
Install requirements for a project.

    cd /var/www/task_list && pip install -r requirements.txt

##Database creation
###For psql

    sudo su - postgres
    psql
    CREATE DATABASE task_list;
    CREATE USER task_list_user WITH password 'root';
    GRANT ALL privileges ON DATABASE task_list TO task_list_user;
    

For run project

    python3 manage.py runserver


For Mamble team

    Sorry about ui and stiles :)
        
