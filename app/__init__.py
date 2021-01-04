from flask import Flask

app= Flask(__name__,template_folder='templetes')

from app import routes
