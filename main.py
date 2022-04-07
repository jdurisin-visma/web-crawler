from flask import request, flash, url_for, redirect, render_template

import app.web as web
from app import create_app, db
from app.models import ScrapeModel


app = create_app()
app.app_context().push()


@app.route('/')
def show_all():
    return render_template('show_all.html', records=ScrapeModel.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['url'] or not request.form['keyword']:
            flash('Please enter all the fields', 'error')
        else:
            s = ScrapeModel(*web.Web().scrape(request.form['url'], request.form['keyword']))

            db.session.add(s)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
