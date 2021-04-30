from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

from models.Conexion import *

from route.routes import *

CORS(app, resources={r"/*": {"origins": "*"}})

# users
app.add_url_rule(users["create_user"], view_func=users["create_user_controllers"])
app.add_url_rule(users["Login_user"], view_func=users["login_user_controllers"])
app.add_url_rule(users["validate_account_user"], view_func=users["validate_account"])
app.add_url_rule(users["recover_email_user"], view_func=users["recover_email"])
app.add_url_rule(users["recover_password_user"], view_func=users["recover_password"])
app.add_url_rule(users["modification_password_user"], view_func=users["modification_password"])
app.add_url_rule(users["authorization_user"], view_func=users["authorization_user_controller"])

# work_environment
app.add_url_rule(environment["create_environment"], view_func=environment["create_environment_controller"])
app.add_url_rule(environment["show_environment"], view_func=environment["show_environment_controller"])
app.add_url_rule(environment["remove_environment"], view_func=environment["remove_environment_controller"])
app.add_url_rule(environment["search_environment"], view_func=environment["search_environment_controller"])
    #- Manage_Users
app.add_url_rule(environment["manage_users_environment"], view_func=environment["manage_users_controller"])
app.add_url_rule(environment["manage_users_remove_environment"], view_func=environment["manage_users_remove_controller"])
app.add_url_rule(environment["manage_join_by_code_environment"], view_func=environment["manage_join_by_code_controller"])
app.add_url_rule(environment["manage_search_environment"], view_func=environment["manage_search_controller"])
app.add_url_rule(environment["manage_send_email_environment"], view_func=environment["manage_send_email_controller"])

#divice
"""app.add_url_rule(device["device_add"], view_func=device["device_add_controllers"])"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)