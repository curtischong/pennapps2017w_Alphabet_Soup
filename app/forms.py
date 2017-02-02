from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.widgets import TextArea
                                                                                                                                        
class CreateBook(FlaskForm):
  vent = StringField('vent', widget=TextArea())