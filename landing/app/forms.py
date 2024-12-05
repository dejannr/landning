from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
    email = StringField('Email Address', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email Address"})
    phone = StringField('Phone Number', validators=[Optional()], render_kw={"placeholder": "Phone Number"})
    company = StringField('Company Name', validators=[Optional()], render_kw={"placeholder": "Company Name"})
    job_title = StringField('Job Title', validators=[Optional()], render_kw={"placeholder": "Job Title"})
    dietary_preferences = StringField('Dietary Preferences', validators=[Optional()], render_kw={"placeholder": "e.g., vegetarian, vegan, gluten-free"})
    topics_of_interest = TextAreaField('Topics of Interest', validators=[Optional()], render_kw={"placeholder": "Tell us what you'd like to learn about"})
    comments = TextAreaField('Additional Comments or Questions', validators=[Optional()], render_kw={"placeholder": "Any additional comments or questions"})
    submit = SubmitField('Submit')
