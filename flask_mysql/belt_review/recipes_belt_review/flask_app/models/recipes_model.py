from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB_NAME
from flask_app.models import user_model
from flask import flash

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.Date_Cooked = data["Date_Cooked"]
        self.unedr_30 = data["unedr_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def create_party(cls, data):
        
        query = """
                    INSERT INTO recipes (name, description,instruction,Date_Cooked,under_30,user_id)
                    VALUES (%(name)s,%(description)s,%(instruction)s,%(Date_Cooked)s,%(unedr_30)s,%(user_id)s);
                """
        

        results = connectToMySQL(DB_NAME).query_db(query, data)
        return results
    @classmethod
    def get_all(cls):

        query = """
                        SELECT * FROM recipes
                        JOIN users
                        ON recipes.user_id = users.id ;
                 """
        results = connectToMySQL(DB).query_db(query)

        all_recipes = []

        for row in results:
            this_recipe = cls(row)
            # fix up the hero ambiguity for the hero
            # prepare the data for the contructor

            user_data = {
                **row,
                "id": row["users.id"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }

            this_user = user_model.User(user_data)
            this_recipe.user = this_user
            all_recipes.append(this_recipe)

        return all_recipes