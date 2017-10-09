ADA-WEBSHOP
============

Carshop API with React frontend.

Set up the API
---------------

1. `cd webshop`
2. Create a Python virtual environment `env`
3. Install into the virtualenv: `env/bin/pip install -e ".[testing]`
4. Inialize the database `env/bin/initialize_webshop_db development.ini`
5. Run the project backend: `env/bin/pserve development.ini`
6. Make sure its running on port `http://localhost:6543`

Set up the Front End
--------------------
1. `cd frontend`
2. `nvm install && nvm use`
3. `npm install`
4. `npm run build`

