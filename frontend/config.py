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
    SQUARESPACE_URL = 'https://www.squarespace.com/about/careers'
    SQUARESPACE_EMP_URL = 'https://api.greenhouse.io/v1/boards/squarespace/offices/'
    HUBSPOT_URL = 'https://www.hubspot.com/jobs/search'
    HUBSPOT_EMP_URL = 'https://hs-greenhouse.herokuapp.com/search'
    PINTEREST_URL = 'https://careers.pinterest.com/careers'
    PINTEREST_EMP_URL = 'https://api.greenhouse.io/v1/boards/pinterest/offices/'
    JDPOWER_URL = 'https://www.jdpower.com/business/careers/open-positions'
    JDPOWER_EMP_URL = 'https://api.greenhouse.io/v1/boards/jdpower/offices/'
    THETRADEDESK_URL = 'https://www.thetradedesk.com/'
    THETRADEDESK_EMP_URL = 'https://api.greenhouse.io/v1/boards/thetradedesk/offices/'
    HARRYS_URL = 'https://www.harrys.com/en/us/careers'
    HARRYS_EMP_URL = 'https://api.greenhouse.io/v1/boards/harrys/offices/'
    SUPPORTED = ['Twilio', 'Airbnb', 'Yext', 'SquareSpace', 'HubSpot', 'Pinterest', 'JDPower', 'theTradeDesk', 'Harrys']
