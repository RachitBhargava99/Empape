from flask import Blueprint, render_template, current_app
import requests
from titlecase import titlecase

dash = Blueprint('dash', __name__)


@dash.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@dash.route('/emp/<website>', methods=['GET'])
def show_emp(website):
    website = website.upper()
    if website == "TWILIO":
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
                        'location': location['name'],
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
    else:
        return render_template('all_emp.html', data=[], company=titlecase(website))
