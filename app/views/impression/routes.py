from flask import Blueprint, render_template, redirect
from flask_login import current_user, login_required
from os import path, getcwd , sep , pardir
from app.views.impression.forms import ImpressionForm
from werkzeug.utils import secure_filename
from app.models.user import User
import random
import string


impression_blueprint = Blueprint("impression", __name__, template_folder="templates")


@impression_blueprint.route("/impression", methods=["GET", "POST"])
@login_required
def image():
    form = ImpressionForm()

    data = [[user.username,user.img_name] for user in User.query.all() if user.img_name !="0"]
    print(data)



    if form.validate_on_submit():
        
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits

        def random_name():
            return  ''.join(random.choice(letters) for i in range(10))


        filename = secure_filename(form.impression_image.data.filename)
        file_type = filename.split(".")[1]

        
        new_filename = random_name() + "." + file_type

        

        if current_user.img_name == "0":

            location = path.realpath(path.join(getcwd(), path.dirname(__file__) + sep + pardir+ sep + pardir))
            
            file_path = path.join(location, "static/uploaded_files", new_filename)
            
            form.impression_image.data.save(file_path)

            user_img = User.query.filter_by(id = current_user.id).first()

            user_img.img_name = new_filename
            user_img.save()
        
                
        return render_template("impressions/impression.html", imperssion_form = form, data=data)
    return render_template("impressions/impression.html", imperssion_form = form, data=data)