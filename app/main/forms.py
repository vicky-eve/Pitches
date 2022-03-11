from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators =[InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Interview','Interview'),('Product','Product'),('Project','Project'),('Promotion','Promotion')],validators=[InputRequired()])
    word = TextAreaField('Make your pitch', validators=[InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add comment',validators=[InputRequired()])
    submit = SubmitField('Comment')