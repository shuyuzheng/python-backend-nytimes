from flask import render_template, flash, redirect
from app.forms import SearchForm
from app import app

@app.route('/')
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('success search!')
        return redirect('/search')
    return render_template('search.html', title='Search', form=form)
