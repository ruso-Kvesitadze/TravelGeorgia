from flask import Blueprint, render_template, redirect, flash
from app.models.tours import Tour
from app.views.filters.forms import ItemForm
from sqlalchemy import and_
filter_blueprint = Blueprint("filter", __name__, template_folder="templates")
from flask_login import current_user, login_required

@filter_blueprint.route("/Signagi", methods = ["POST", "GET"])
def signagi():
    form = ItemForm()
    Signagi = Tour.query.filter_by(location = "Signagi")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Signagi, itemform = form)

    return render_template("tours/tours.html", tours = Signagi, itemform = form)


@filter_blueprint.route("/Kazbegi", methods = ["POST", "GET"])
def kazbegi():
    form = ItemForm()
    Kazbegi = Tour.query.filter_by(location = "Kazbegi")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Kazbegi, itemform = form)

    return render_template("tours/tours.html", tours = Kazbegi, itemform = form)


@filter_blueprint.route("/Svaneti", methods = ["POST", "GET"])
def svaneti():
    form = ItemForm()
    Svaneti = Tour.query.filter_by(location = "Svaneti")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Svaneti, itemform = form)

    return render_template("tours/tours.html", tours = Svaneti, itemform = form)


@filter_blueprint.route("/Bakuriani", methods = ["POST", "GET"])
def bakuriani():
    form = ItemForm()
    Bakuriani = Tour.query.filter_by(location = "Bakuriani")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Bakuriani, itemform = form)

    return render_template("tours/tours.html", tours = Bakuriani, itemform = form)


@filter_blueprint.route("/Borjomi", methods = ["POST", "GET"])
def borjomi():
    form = ItemForm()
    Borjomi = Tour.query.filter_by(location = "Borjomi")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Borjomi, itemform = form)

    return render_template("tours/tours.html", tours = Borjomi, itemform = form)


@filter_blueprint.route("/Batumi", methods = ["POST", "GET"])
def batumi():
    form = ItemForm()
    Batumi = Tour.query.filter_by(location = "Batumi")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Batumi, itemform = form)

    return render_template("tours/tours.html", tours = Batumi, itemform = form)



@filter_blueprint.route("/Oneday", methods = ["POST", "GET"])
def oneday():
    form = ItemForm()
    Oneday = Tour.query.filter_by( duration= "1 Day")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Oneday, itemform = form)

    return render_template("tours/tours.html", tours = Oneday, itemform = form)


@filter_blueprint.route("/Twoday", methods = ["POST", "GET"])
def twoday():
    form = ItemForm()
    Twoday = Tour.query.filter_by( duration= "2 Days")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Twoday, itemform = form)

    return render_template("tours/tours.html", tours = Twoday, itemform = form)



@filter_blueprint.route("/Threeday", methods = ["POST", "GET"])
def threeday():
    form = ItemForm()
    Threeday = Tour.query.filter_by( duration= "3 Days")

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = Threeday, itemform = form)

    return render_template("tours/tours.html", tours = Threeday, itemform = form)




@filter_blueprint.route("/50-100", methods = ["POST", "GET"])
def price1():
    form = ItemForm()
    price1 = Tour.query.filter(and_(Tour.price>=50, Tour.price<=100))

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = price1, itemform = form)

    return render_template("tours/tours.html", tours = price1, itemform = form)


@filter_blueprint.route("/100-150", methods = ["POST", "GET"])
def price2():
    form = ItemForm()
    price2 = Tour.query.filter(and_(Tour.price>=100, Tour.price<=150))

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = price2, itemform = form)

    return render_template("tours/tours.html", tours = price2, itemform = form)



@filter_blueprint.route("/150-200", methods = ["POST", "GET"])
def price3():
    form = ItemForm()
    price3 = Tour.query.filter(and_(Tour.price>=150, Tour.price<=200))

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html", tours = price3, itemform = form)

    return render_template("tours/tours.html", tours = price3, itemform = form)



@filter_blueprint.route("/search", methods = ["POST", "GET"])
def search():
    form = ItemForm()
    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return redirect("/tours")
    return redirect("/tours")



@filter_blueprint.route("/buy/<int:prodact_id>", methods = ["POST", "GET"])
@login_required
def buy(prodact_id=None):
    tour = Tour.query.filter_by(id = prodact_id).first()
    print(tour.available_places)
    tour.available_places = int(tour.available_places) - 1 
    tour.save()
    print(tour.available_places)

    if tour.available_places == 0 :
        tour.delete()
        tour.save()



    flash("success")
    return redirect('/tours')