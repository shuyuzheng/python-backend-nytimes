from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, SelectField

class SearchForm(FlaskForm):
    query = StringField('Key word')
    critics_pick = BooleanField("Only critics' pick")
    opening_start = DateField(format="%Y-%b-%d")
    opening_end = DateField(format="%Y-%b-%d")
    publication_start = DateField(format="%Y-%b-%d")
    publication_end = DateField(format="%Y-%b-%d")
    reviewer = StringField('Reviewer')
    order = SelectField('Order results by', choices=[('by-opening-date', 'Opening date'), ('by-publication-date', 'Publication date'), ('by-title', 'Title')])
    submit = SubmitField('Search')
