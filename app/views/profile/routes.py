from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.models.user import User
from app.extensions import db
from app.views.authentication.forms import RegisterForm
from werkzeug.security import generate_password_hash
from flask import redirect

profile_blueprint = Blueprint("profile", __name__, template_folder="templates")


@profile_blueprint.route("/profile", methods=["GET", "POST"])
@login_required
def myaccount():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        mobile_number = form.mobile_number.data
        password = form.password.data
        new_password = form.confirm_password.data

        if current_user.check_password(password):
            User.query.filter_by(id=current_user.id).update({"username": username , "email": email, "mobile_number" : mobile_number, "password" : generate_password_hash(new_password)})
            db.session.commit()
            return render_template("profile/profile.html", register_form = form)


    return render_template("profile/profile.html", register_form = form)



    

