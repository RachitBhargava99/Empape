from flask import Blueprint, render_template, current_app
import requests
from titlecase import titlecase

dash = Blueprint('dash', __name__)


@dash.route('/', methods=['GET'])
def home():
    return render_template('home.html', supported=current_app.config['SUPPORTED'])


@dash.route('/emp/<website>', methods=['GET'])
def show_emp(website):
    website = website.upper()
    if website == "TWILIO" or website == "SQUARESPACE" or website == "PINTEREST" or website == "JDPOWER"\
            or website == "THETRADEDESK" or website == "HARRYS":
        raw_data = requests.get(current_app.config[f'{website}_EMP_URL'])
        data = raw_data.json()
        final_list = []
        i = 1
        for location in data['offices']:
            for dept in location['departments']:
                for job in dept['jobs']:
                    final_list.append({
                        'id': i,
                        'title': job['title'],
                        'location': location['location'],
                        'department': dept['name'],
                        'url': job['absolute_url']
                    })
                    i += 1
        return render_template('all_emp.html', data=final_list, company=titlecase(website))
    elif website == "AIRBNB":
        raw_data = requests.get(current_app.config[f'{website}_EMP_URL'])
        data = raw_data.json()
        final_list = []
        departments = {}
        for dept in data['departments']:
            departments[dept['id']] = dept['name']
        i = 1
        for job in data['jobs']:
            final_list.append({
                'id': i,
                'title': job['title'],
                'location': job['location'],
                'department': departments[job['deptId']],
                'url': f"https://careers.airbnb.com/positions/{job['id']}"
            })
            i += 1
        return render_template('all_emp.html', data=final_list, company=titlecase(website))
    elif website == "YEXT":
        raw_data = requests.get(current_app.config[f'{website}_EMP_URL'])
        data = raw_data.json()
        final_list = []
        i = 1
        for dept in data['departments']:
            for job in dept['jobs']:
                final_list.append({
                    'id': i,
                    'title': job['title'],
                    'location': job['location']['name'],
                    'department': job['metadata'][0]['value'],
                    'url': job['absolute_url']
                })
                i += 1
        return render_template('all_emp.html', data=final_list, company=titlecase(website))
    elif website == "HUBSPOT":
        raw_data = requests.get(current_app.config[f'{website}_EMP_URL'])
        data = raw_data.json()
        final_list = []
        i = 1
        for job in data:
            final_list.append({
                'id': i,
                'title': job['title'],
                'location': job['offices'],
                'department': job['department'],
                'url': job['appUrl']
            })
            i += 1
        return render_template('all_emp.html', data=final_list, company=titlecase(website))
    else:
        return render_template('all_emp.html', data=[], company=titlecase(website))
