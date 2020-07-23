from clarifai.rest import ClarifaiApp
import json
import os
import shutil

# Access your application
clarifai_app = ClarifaiApp(api_key='3711556ad03d4e08a603b4ca0e25911b')
# This is the General model id
clarifai_model = clarifai_app.models.get(model_id='aaa03c23b3724a16a56b629203edc62c')

DIRECTORIES = ['puppy', 'tree', 'city', 'cream']
# Type out the full path to clarifai_images
clarifai_images_path = '/Users/kimberleyellars/github/image-sort2/clarifai_images'

image_filenames = os.listdir(clarifai_images_path)

# START CODING HERE

os.mkdir("/Users/kimberleyellars/github/image-sort2/puppy")
os.mkdir("/Users/kimberleyellars/github/image-sort2/tree")
os.mkdir("/Users/kimberleyellars/github/image-sort2/city")
os.mkdir("/Users/kimberleyellars/github/image-sort2/cream")

# 1. Loop through all the files in clarifai_images
for image_filename in image_filenames:
    # 2. Use .predict_by_filename() on model to get the json response from Clarifai
    image = clarifai_model.predict_by_filename(f"{clarifai_images_path}/{image_filename}")
    # 3. Create an empty list for the image tags
    image_tags = []
    # 4.  Loop through ['outputs'][0]['data']['concepts'] and append the items to the
    #     image tags list
    for tag in image['outputs'][0]['data']['concepts']:
        for things in tag:
            if things == 'name':
        ##image_tags.append(tag)
    # 5. Move the files to the appropriate folder based on whether or not the image tag
    #    matches the name in DIRECTORIES
    #    Hint: Review your file organizer
                if str(tag['name']) in DIRECTORIES:
                    shutil.move(f"{clarifai_images_path}/{image_filename}", f"/Users/kimberleyellars/github/image-sort2/{str(tag['name'])}")
