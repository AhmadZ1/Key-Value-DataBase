# Key-Value-DataBase
This is a way to create simple key-value databases for simple tasks.

To use this key-value database, you first need to create a folder to place it in (you can place it anywhere on your pc, but it's better to use a specific folder for it).
Then, you just copy the path for the place you want to store it in, instantiate a DataBase, and pass the path and name you want as parameters.(my_db = DataBase(db_path, db_name)).
Now, if you haven't created a database with the given name yet, you need to do my_db.create(). However, if you already have a database with the same name, you just do my_db.load().
Then you can add keys and values by add_key(key, value) method, delete existing keys by delete_key(key) method, and override existing keys by override(key, new_value).
Finally, the most important thing is to save your database by using my_db.save(), for safety, put it in the last line of your code when you start working, to not forget it. If you did not call my_db.save(), all your changes and modifications will not be saved.
You can delete the database that you are working on by using my_db.delete_database() method.

You can use this database to store many things, like my_db.add_key("username", ["password", "email", "location", "id"]) or many other uses.
