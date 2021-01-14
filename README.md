# Key-Value-DataBase
This is a way to create simple key-value databases for simple tasks.

To initialize the DataBase, you need to specify the path that you want it to be in, and give it a name.

It will automatically create/load it, depending on whether it's created or not.

To add new key to your database, simply call add(key, value) method.

To add more than one key at a time, use add_keys({ "key1":"value1", "key2":"value2",}).

To change the value of an existing key, use change(key, new_value) method.

To delete a key from the database, call delete(key) method.

To view the keys and values pf your database, use display() method.

To get the value of a certain key, use get(key) method.

To get values of more than one key, use get_keys(keys), i.e. get_keys("key1", "key2", "key3").

To check if a key is found in database or not, use isfound(key) method.

To clear all the rows in the database, use clear_all().

To delete the database you are working with, call delete_this_database() method.

To delete another database, use deleteDataBase(directory, name) function, where directory is where you store the database, and name is its name.

Finally, don't forget to save the database using save() method, if you forget to save it, all the changes
won't be saved and you need to work again, so be careful.

However, you can enable autosaving by calling enable_autosave(), and you can disable it by calling disable_autosave().

Note that enabling autosave is not recommended for big databases (rows >= 10000), manual saving it better.


# If you want to create the database in the current folder, just put the path as empty string and set current_directory to True, for example:
# db = DataBase("", "MyDb", current_directory=True)

You can use this database to store many things, like my_db.add_key("username", ["password", "email", "location", "id"]) or many other uses.


pip command to download from cmd/terminal: pip install keyvalue-database
