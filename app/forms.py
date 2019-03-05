from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, length


class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre :', validators=[DataRequired(), length(min=5, max=20)])
    apellido = StringField('Apellido :', validators=[DataRequired(), length(min=5, max=20)])
    submit = SubmitField('Ingresar')

