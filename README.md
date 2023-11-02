Once you open this folder in an editor(VScode): 
i.  Open a shell in the current folder and install pipenv using
```
    pip install pipenv
```

ii. Once the install is done, start a virtual environment for the project using
```
    pipenv shell
```
iii. Activate the virtual environment, then, You can now install project dependencies. Do so by running 

    ```
    pipenv install -r requirements.txt
    ```

iv. If everything is set, run 
```
python3 manage.py runserver 8000
```
 to start a development server 
    on http://localhost:8000. (You can use this link)

v.  Open a browser to eplore the webpages.

vi. You may need to run 
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
in that order to ensure that everything works fine.
# coms-ltd
