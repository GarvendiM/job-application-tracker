from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection
import json

app = Flask(__name__)

# --- DASHBOARD ---
@app.route('/')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("""
        SELECT 
            (SELECT COUNT(*) FROM companies) AS total_companies,
            (SELECT COUNT(*) FROM jobs) AS total_jobs,
            (SELECT COUNT(*) FROM applications) AS total_applications,
            (SELECT COUNT(*) FROM applications WHERE status = 'Interview') AS active_interviews
    """)
    stats = cursor.fetchone()
    
    cursor.execute("""
        SELECT a.application_id, a.application_date, a.status, j.job_title, c.company_name
        FROM applications a
        JOIN jobs j ON a.job_id = j.job_id
        JOIN companies c ON j.company_id = c.company_id
        ORDER BY a.application_date DESC LIMIT 5
    """)
    recent_apps = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('dashboard.html', stats=stats, recent_apps=recent_apps)

# --- COMPANIES CRUD ---
@app.route('/companies')
def list_companies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM companies ORDER BY company_name ASC")
    companies = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('companies.html', companies=companies)

@app.route('/companies/add', methods=['POST'])
def add_company():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO companies (company_name, industry, website, city, state, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        request.form['company_name'],
        request.form.get('industry'),
        request.form.get('website'),
        request.form.get('city'),
        request.form.get('state'),
        request.form.get('notes')
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_companies'))

@app.route('/companies/edit/<int:id>', methods=['POST'])
def update_company(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE companies 
        SET company_name = %s, industry = %s, website = %s, city = %s, state = %s, notes = %s
        WHERE company_id = %s
    """, (
        request.form['company_name'],
        request.form.get('industry'),
        request.form.get('website'),
        request.form.get('city'),
        request.form.get('state'),
        request.form.get('notes'),
        id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_companies'))

@app.route('/companies/delete/<int:id>', methods=['POST'])
def delete_company(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM companies WHERE company_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_companies'))

# --- JOBS CRUD ---
@app.route('/jobs')
def list_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch all jobs (with company names joined)
    cursor.execute("""
        SELECT j.*, c.company_name 
        FROM jobs j 
        JOIN companies c ON j.company_id = c.company_id
    """)
    jobs = cursor.fetchall()
    
    # Fetch all companies to populate the dropdown
    cursor.execute("SELECT company_id, company_name FROM companies")
    companies = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('jobs.html', jobs=jobs, companies=companies)

@app.route('/jobs/add', methods=['POST'])
def add_job():
    raw_reqs = request.form.get('requirements', '{"skills": []}')
    try:
        requirements_json = json.dumps(json.loads(raw_reqs))
    except json.JSONDecodeError:
        requirements_json = json.dumps({"skills": []})

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jobs (company_id, job_title, salary_min, salary_max, job_type, job_url, date_posted, requirements)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        request.form['company_id'],
        request.form['job_title'],
        request.form.get('salary_min') or None,
        request.form.get('salary_max') or None,
        request.form['job_type'],
        request.form.get('job_url'),
        request.form['date_posted'],
        requirements_json
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_jobs'))

@app.route('/jobs/edit/<int:id>', methods=['POST'])
def update_job(id):
    raw_reqs = request.form.get('requirements', '{"skills": []}')
    try:
        requirements_json = json.dumps(json.loads(raw_reqs))
    except json.JSONDecodeError:
        requirements_json = json.dumps({"skills": []})

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE jobs 
        SET company_id = %s, job_title = %s, salary_min = %s, salary_max = %s, 
            job_type = %s, job_url = %s, date_posted = %s, requirements = %s
        WHERE job_id = %s
    """, (
        request.form['company_id'],
        request.form['job_title'],
        request.form.get('salary_min') or None,
        request.form.get('salary_max') or None,
        request.form['job_type'],
        request.form.get('job_url'),
        request.form['date_posted'],
        requirements_json,
        id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_jobs'))

@app.route('/jobs/delete/<int:id>', methods=['POST'])
def delete_job(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE job_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_jobs'))

# --- APPLICATIONS CRUD ---
@app.route('/applications')
def list_applications():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch all applications joined with jobs and companies
    cursor.execute("""
        SELECT a.*, j.job_title, c.company_name 
        FROM applications a
        JOIN jobs j ON a.job_id = j.job_id
        JOIN companies c ON j.company_id = c.company_id
        ORDER BY a.application_date DESC
    """)
    applications = cursor.fetchall()
    
    # Fetch jobs so the dropdown can populate in the form
    cursor.execute("""
        SELECT j.job_id, j.job_title, c.company_name 
        FROM jobs j
        JOIN companies c ON j.company_id = c.company_id
    """)
    jobs = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('applications.html', applications=applications, jobs=jobs)

@app.route('/applications/add', methods=['POST'])
def add_application():
    job_id = request.form.get('job_id')
    application_date = request.form.get('application_date')
    status = request.form.get('status')
    resume_version = request.form.get('resume_version')
    
    # Checkboxes only send a value if checked; otherwise, they are omitted
    cover_letter_sent = 1 if request.form.get('cover_letter_sent') == '1' else 0
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO applications (job_id, application_date, status, resume_version, cover_letter_sent)
        VALUES (%s, %s, %s, %s, %s)
    """, (job_id, application_date, status, resume_version, cover_letter_sent))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('list_applications'))

@app.route('/applications/edit/<int:id>', methods=['POST'])
def update_application(id):
    cover_letter = 1 if 'cover_letter_sent' in request.form else 0
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE applications 
        SET job_id = %s, application_date = %s, status = %s, resume_version = %s, cover_letter_sent = %s
        WHERE application_id = %s
    """, (
        request.form['job_id'],
        request.form['application_date'],
        request.form['status'],
        request.form.get('resume_version'),
        cover_letter,
        id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_applications'))

@app.route('/applications/delete/<int:id>', methods=['POST'])
def delete_application(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM applications WHERE application_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_applications'))

# --- CONTACTS CRUD ---
@app.route('/contacts')
def list_contacts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT co.*, c.company_name 
        FROM contacts co
        JOIN companies c ON co.company_id = c.company_id
        ORDER BY co.contact_name ASC
    """)
    contacts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('contacts.html', contacts=contacts)

@app.route('/contacts/add', methods=['POST'])
def add_contact():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (company_id, contact_name, title, email, phone, linkedin_url, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        request.form['company_id'],
        request.form['contact_name'],
        request.form.get('title'),
        request.form.get('email'),
        request.form.get('phone'),
        request.form.get('linkedin_url'),
        request.form.get('notes')
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_contacts'))

@app.route('/contacts/edit/<int:id>', methods=['POST'])
def update_contact(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE contacts 
        SET company_id = %s, contact_name = %s, title = %s, email = %s, phone = %s, linkedin_url = %s, notes = %s
        WHERE contact_id = %s
    """, (
        request.form['company_id'],
        request.form['contact_name'],
        request.form.get('title'),
        request.form.get('email'),
        request.form.get('phone'),
        request.form.get('linkedin_url'),
        request.form.get('notes'),
        id
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_contacts'))

@app.route('/contacts/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE contact_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('list_contacts'))

# --- JOB MATCH ---
@app.route('/job-match', methods=['GET'])
def job_match():
    matched_jobs = []
    search_skill = request.args.get('skill', '').strip()
    
    if search_skill:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT j.*, c.company_name 
            FROM jobs j
            JOIN companies c ON j.company_id = c.company_id
            WHERE JSON_CONTAINS(j.requirements, %s, '$.skills')
        """, (json.dumps(search_skill),))
        matched_jobs = cursor.fetchall()
        cursor.close()
        conn.close()
        
    return render_template('job_match.html', matched_jobs=matched_jobs, search_skill=search_skill)

if __name__ == '__main__':
    app.run(debug=True)
