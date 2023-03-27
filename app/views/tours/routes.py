from flask import Blueprint, render_template
from app.models.tours import Tour
from app.views.filters.forms import ItemForm
tour_blueprint = Blueprint("tours", __name__, template_folder="templates")


@tour_blueprint.route("/tours" , methods = ["POST", "GET"])
def choose_tour():
    form = ItemForm()
    tours = Tour.query.all()

    if form.validate_on_submit():
        data = form.search.data

        if len(data) >= 1:
            tour = Tour.query.\
            filter(Tour.location.contains(data)).all()
            return render_template ("tours/tours.html", itemform = form, tours = tour)
        return render_template("tours/tours.html",itemform = form, tours=tours)

    return render_template("tours/tours.html",itemform = form, tours=tours)
