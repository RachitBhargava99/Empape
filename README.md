# Empape
Welcome to Empape - time to see get in touch with the jobs at the companies you love without getting tracker!

Please note that some of the files in this repository are native to deploying on Google App Engine.
Feel free to ignore them.

Below mentioned are the endpoints that can be publicly called to get information or feed in the required information.

## Endpoints
### <pre>/home                  GET</pre>
Renders a basic homepage listing the companies currently supported by the application.
<hr>

### <pre>/emp/<company_name>    POST</pre>
Renders the list of jobs at the company you chose. Please note that the company_name field in URL is not case-sensitive.
In other words, it shall treat Empape and EMPAPE to be one and the same entity.
<hr>


## Google App Engine Requirements
This application was initially built to be deployed using Google App Engine.
As a result, there are several environment variables that were added to a <code>app.yaml</code> file.
Here are some that you might need to add while deploying this.
Also, please note that several are required for adding Google Cloud SQL support.
You may remove them if you are planning to use a different database.

<pre>
PROJECT_ID: enter_project_id
DATA_BACKEND: 'cloudsql'
CLOUDSQL_USER: enter_username
CLOUDSQL_PASSWORD: enter_password
CLOUDSQL_DATABASE: enter_database_name
CLOUDSQL_CONNECTION_NAME: enter_connection_name
</pre>
<hr>

## LocalHost Requirements
This application can also be deployed on localhost.
However, before you do that, you would need to install the packages listed in <code>requirements.txt</code> file.
Once done, run the <code>run.py</code> file
and browse to <code>http://127.0.0.1/</code> using your preferred web browser.

## Contact Info
In case of any queries, please feel free to contact Rachit Bhargava (developer) at rachitbhargava99@gmail.com.

## Third-Party Use
This application cannot be used for any unauthorized uses.
If you are interested in using the application for any purposes, please contact the developer for permissions.
