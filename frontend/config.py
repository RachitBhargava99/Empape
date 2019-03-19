import os


class Config:
    SECRET_KEY = '0917b13a9091915d54b6336f45909539cce452b3661b21f386418a257883b30a'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_URL = 'https://www.twilio.com/company/jobs'
    TWILIO_EMP_URL = 'https://api.greenhouse.io/v1/boards/twilio/offices'
    AIRBNB_URL = 'https://careers.airbnb.com/positions/'
    AIRBNB_EMP_URL = 'https://careers.airbnb.com/wp-admin/admin-ajax.php?action=fetch_greenhouse_jobs&which-board=airbnb&strip-empty=true'
    YEXT_URL = 'https://www.yext.com/careers/open-positions/'
    YEXT_EMP_URL = 'https://api.greenhouse.io/v1/boards/yext/embed/departments'
