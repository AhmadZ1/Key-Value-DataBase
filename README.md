# Key-Value-DataBase
This is a way to create simple key-value databases for simple tasks.

To initialize the DataBase, you need to specify the path that you want it to be in, and give it a name.
If you haven't created the database yet, simply create it by calling this create() method, and a database 
with the name you gave it before will be created. 
If you have already created a database with the name you passed, you need to load it by this load() method.
Note that you don't need to call load() after calling create() for the first time.
To add keys and values to your database, simply call add_key(key, value) method.
To override an existing key, use override(key, new_value) method.
To delete a key from the database, call delete_key(key) method.
To view the keys and values pf your database, use display() method.
Finally, don't forget to save the database using save() method, if you forget to save it, all the changes
won't be saved and you need to work again, so be careful.
However, you can enable autosaving by calling enable_autosave(), and you can disable it by calling disable_autosave().
Note that enabling autosave is not recommended for big databases (rows >= 10000), manual saving it better.

You can use this database to store many things, like my_db.add_key("username", ["password", "email", "location", "id"]) or many other uses.


pip command to download from cmd/terminal: pip install keyvalue-database
