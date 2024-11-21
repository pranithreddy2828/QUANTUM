from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample job listings data - in a real app, this would come from a database
jobs = [
    {
        'id': 1,
        'title': 'FULLSTACK PYTHON DEVELOPER',
        'location': 'NAGOLE, HYDERABAD',
        'department': 'Engineering',
        'description': 'Join our engineering team to build next-generation solutions.'
    },
    {
        'id': 2,
        'title': 'DATA SCIENTIST',
        'location': 'CHAITANYAPURI, HYDERABAD',
        'department': 'Analytics',
        'description': 'Help us derive insights from complex datasets.'
    },
    {
        'id': 3,
        'title': 'UX DESINER',
        'location': 'HYDERABAD, HYDERABAD',
        'department': 'Design',
        'description': 'Create beautiful and intuitive user experiences.'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/careers')
def careers():
    return render_template('careers.html', jobs=jobs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/culture')
def culture():
    return render_template('culture.html')

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job:
        return render_template('job_detail.html', job=job)
    return redirect(url_for('careers'))

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        # Handle application submission (in a real app, save to database)
        return render_template('application_success.html')
    return render_template('apply.html')

# Added new routes for career sections
@app.route('/careers/why-join')
def why_join():
    return render_template('why_join.html')

@app.route('/careers/life-at-quantumquill')
def life_at_quantumquill():
    return render_template('life_at_quantumquill.html')

@app.route('/careers/meet-our-people')
def meet_our_people():
    return render_template('meet_our_people.html')

@app.route('/careers/career-paths')
def career_paths():
    return render_template('career_paths.html')

@app.route('/careers/join-us')
def join_us():
    return render_template('join_us.html')
@app.route('/about/who-we-are')
def who_we_are():
    company_info = {
        "name": "QuantumQuill",
        "mission": "To empower innovation through technology and create a positive impact on the world.",
        "vision": "We aim to be a leader in the tech industry by fostering a culture of creativity, collaboration, and continuous improvement."
    }
    return render_template('who_we_are.html', company_info=company_info)

@app.route('/about/management-and-governance')
def management_and_governance():
    return render_template('management_and_governance.html')

@app.route('/about/environment-social-governance')
def environment_social_governance():
    return render_template('environment_social_governance.html')

@app.route('/about/corporate-social-responsibility')
def corporate_social_responsibility():
    return render_template('corporate_social_responsibility.html')

@app.route('/about/transforming-sports')
def transforming_sports():
    return render_template('transforming_sports.html')

@app.route('/about/technology-partners')
def technology_partners():
    return render_template('technology_partners.html')

@app.route('/about/locations')
def locations():
    return render_template('locations.html')

if __name__ == '__main__':
    app.run(debug=True)
