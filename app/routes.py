from werkzeug.utils import redirect
from app import app
from flask import render_template, flash, url_for
from app.forms import UsuarioForm
from app.models import *


@app.route('/templates/listar')
def usuario():
    usuario = User.query.all()
    return render_template('listar.html', usuario=usuario)


@app.route('/templates/crear', methods=['POST', 'GET'])
def create():
    form = UsuarioForm()
    if form.validate_on_submit():
        user = User(nombre=form.nombre.data,
                            apellido=form.apellido.data)
        db.session.add(user)
        db.session.commit()
        flash('Ingresado!')
        return redirect(url_for('usuario'))
    return render_template('/registrar.html', form=form)


@app.route('/templates/crear/<int:usuario_id>', methods=['POST', 'GET'])
def edit(usuario_id):
    edit_usuario = User.query.filter_by(id=usuario_id).first_or_404()
    form = UsuarioForm()
    if form.validate_on_submit():
        edit_usuario.nombre = form.nombre.data
        edit_usuario.apellido = form.apellido.data
        db.session.add(edit_usuario)
        db.session.commit()
        flash('Usuario Editado')
        return redirect(url_for('usuario'))
    form.nombre.data = edit_usuario.nombre
    form.apellido.data = edit_usuario.apellido
    return render_template('/editar.html', form=form, edit_usuario=edit_usuario)


@app.route('/templates/crear/<int:usuario_id>/delete', methods=['GET'])
def delete(usuario_id):
    edit_usuario = User.query.filter_by(id=usuario_id).first_or_404()
    db.session.delete(edit_usuario)
    db.session.commit()
    flash('Usuario eliminado')
    return redirect(url_for('usuario'))





