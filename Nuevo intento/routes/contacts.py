from flask import Blueprint, render_template, request, redirect, abort, url_for, flash
from models.contacts import Contact
from utils.db import db

# Blueprint me permite manejar de manera mas dinamica las rutas
contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route("/create", methods=["POST"])
def createContact():
    # datos captados por el metodo POST
    fullName = request.form["fullName"]
    email = request.form["email"]
    phone = request.form["phone"]

    newContact = Contact(
        fullName, email, phone
    )  # crea una instancia del modelo Contact con parametros del metodo constructor
    db.session.add(newContact)  # Prepara los datos a guardar
    db.session.commit()  # Confirmar los datos a guardar

    flash(" Contacto guardado satisfactoriamente!") #mensaje flash despues de guardar la info
    #Podriamos realizar mas validaciones para que cuando todo este correcto, nos lance el mensaje
    return redirect("/")


@contacts.route("/update/<id>", methods=["POST", "GET"])
def updateContact(id):
    contact = Contact.query.get(id)

    if request.method == "POST":
        contact.fullName = request.form["fullName"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]
        db.session.commit()  # Confirmar los datos a guardar

        flash(" Contacto actualizado satisfactoriamente!")


        return redirect(url_for("contacts.home"))

    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>")
def deleteContact(id):
    contact = Contact.query.get(id)
    if not contact:
        abort(404)
    db.session.delete(contact)
    db.session.commit()

    flash(" Contacto eliminado satisfactoriamente!")


    return redirect("/")


@contacts.route("/about")
def about():
    return render_template("about.html")
