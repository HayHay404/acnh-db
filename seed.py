from app import app
from models import db, Villager, User, Image
import requests
import json

db.drop_all()
db.create_all()

BASE_URL = 'http://acnhapi.com/v1/villagers'

# TODO: Replace range to range(1, 391)
for idx in range(1, 5):
    resp = requests.get(f"{BASE_URL}/{idx}")
    data = json.loads(resp.text)
    name = data["name"]["name-USen"]
    image_url = data["image_uri"]

    new_villager = Villager(name = name, image_url = image_url)

    db.session.add(new_villager)

new_usr = User.signup(email="hayhay@hayhay.link", password="password",username="HayHay")
new_usr.bio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse hendrerit dui in dapibus luctus. Aenean ut porttitor lorem. Ut ac leo condimentum, fermentum tellus a, viverra dui. Aliquam at tortor justo. Integer ante ligula, fermentum vel maximus mattis, consectetur sed turpis."
new_usr.friend_code = "123456789012"
new_usr.dream_code = "123456789012"

db.session.add(new_usr)
db.session.commit()

new_img_1 = Image(user_id = 1, image_url = "https://ik.imagekit.io/u2glwyhen/island-images/Island_Image_FPRPuXFKg")
new_img_2 = Image(user_id = 1, image_url = "https://ik.imagekit.io/u2glwyhen/island-images/Island_Image_FPRPuXFKg")
new_img_3 = Image(user_id = 1, image_url = "https://ik.imagekit.io/u2glwyhen/island-images/Island_Image_FPRPuXFKg")

db.session.add_all([new_img_1, new_img_2, new_img_3])
db.session.commit()