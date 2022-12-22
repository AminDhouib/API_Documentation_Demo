from flask import Flask, request
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
import requests_cache

def create_app():
    app = Flask(__name__)
    app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 3}
    requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/",
    }

    template = dict(
        swaggerUiPrefix=LazyString(lambda: request.environ.get("HTTP_X_SCRIPT_NAME", ""))
    )

    app.json_encoder = LazyJSONEncoder
    swagger = Swagger(app, config=swagger_config, template=template)

    @app.route("/")
    def index():
        return "Hello! Navigate to /swagger/ to see the documentation."

    @app.route("/api/ping", methods=["GET"])
    @swag_from("swagger_ping_config.yml")
    def ping():
        return {"success": True}
    
    ############
    # ACCOUNTS #
    ############
    @app.route("/api/account", methods=["POST"])
    @swag_from("swagger_create_account.yml")
    def create_account():
        return {"success": True}
    
    @app.route("/api/account", methods=["GET"])
    @swag_from("swagger_get_account_config.yml")
    def get_account_by_id():
        return {"success": True}
    
    @app.route("/api/account", methods=["PATCH"])
    @swag_from("swagger_edit_account_config.yml")
    def edit_account():
        return {"success": True}
    
    @app.route("/api/account", methods=["DELETE"])
    @swag_from("swagger_delete_account_config.yml")
    def delete_account_by_id():
        return {"success": True}
    

    ###################
    # BILLING ADDRESS #
    ###################
    @app.route("/api/address", methods=["POST"])
    @swag_from("swagger_create_address.yml")
    def create_address():
        return {"success": True}
    
    @app.route("/api/address", methods=["DELETE"])
    @swag_from("swagger_delete_address_config.yml")
    def delete_address_by_id():
        return {"success": True}

    @app.route("/api/address", methods=["GET"])
    @swag_from("swagger_get_address_config.yml")
    def get_address_by_id():
        return {"success": True}
    
    @app.route("/api/address", methods=["PATCH"])
    @swag_from("swagger_edit_address_config.yml")
    def edit_address():
        return {"success": True}
    
    #################
    # SUBSCRIPTIONS #
    #################
    @app.route("/api/subscription", methods=["POST"])
    @swag_from("swagger_create_subscription.yml")
    def create_subscription():
        return {"success": True}
    
    @app.route("/api/subscription", methods=["DELETE"])
    @swag_from("swagger_delete_subscription_config.yml")
    def delete_subscription_by_id():
        return {"success": True}
    
    @app.route("/api/subscription", methods=["GET"])
    @swag_from("swagger_get_subscription_config.yml")
    def get_subscription_by_id():
        return {"success": True}
    
    @app.route("/api/subscription", methods=["PATCH"])
    @swag_from("swagger_edit_subscription_config.yml")
    def edit_subscription():
        return {"success": True}
    

    return app
    

if __name__ == "__main__":
    PORT_NUMBER = 5050
    doDebug = True
    app = create_app()
    app.run(debug=doDebug, port=PORT_NUMBER)
