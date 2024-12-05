from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import SignUpForm
from app.models import SignUp

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignUpForm()
    if form.validate_on_submit():
        # Check if the email already exists
        existing_signup = SignUp.query.filter_by(email=form.email.data).first()
        if existing_signup:
            flash('This email is already registered. Please use a different email.', 'danger')
        else:
            # Add the new signup record
            signup = SignUp(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                phone=form.phone.data,
                company=form.company.data,
                job_title=form.job_title.data,
                dietary_preferences=form.dietary_preferences.data,
                topics_of_interest=form.topics_of_interest.data,
                comments=form.comments.data
            )
            db.session.add(signup)
            db.session.commit()
            flash('Thank you for signing up! We will contact you soon.', 'success')
            return redirect(url_for('index'))
    return render_template('index.html', form=form)
