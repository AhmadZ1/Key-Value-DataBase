import sys

# Key-Value DataBase

# To initialize the DataBase, you need to specify the path that you want it to be in, and give it a name.
# If you haven't created the database yet, simply create it by calling this create() method, and a database 
# with the name you gave it before will be created. 
# If you have already created a database with the name you passed, you need to load it by this load() method.
# Note that you don't need to call load() after calling create() for the first time.
# To add keys and values to your database, simply call add_key(key, value) method.
# To override an existing key, use override(key, new_value) method.
# To delete a key from the database, call delete_key(key) method.
# To view the keys and values pf your database, use display() method.
# Finally, don't forget to save the database using save() method, if you forget to save it, all the changes
# won't be saved and you need to work again, so be careful.
# However, you can enable autosaving by calling enable_autosave(), and you can disable it by calling disable_autosave().
# Note that enabling autosave is not recommended for big databases (rows >= 10000), manual saving it better.


# If you want to create the database in the current folder, just put the path as empty string and set current_directory to True, for example:
# db = DataBase("", "MyDb", current_directory=True)


class DataBase:
    def __init__(self, path, name, current_directory=False):
        """Initializes a DataBase with a path and name"""
        self.path = path
        self.name = name
        self.auto = False
        self.curr = current_directory

    
    def create(self):
        """Creates the database in the path passed before, and gives it the name you passed before"""
        try:
            if self.curr:
                file = open(self.name + ".py", "w+")
                file.write("DataBase = {}")
                file.close()
                return
            full_path = self.path + '\\' + self.name +".py"
            file = open(full_path, "w+")
            file.write("DataBase = {}")
            file.close()
        except Error as msg:
            print(msg)

        self.load()

   
    def load(self):
        """Loads an existing database, with the name you passed when instantiated it"""
        try:
            if self.curr:
                database = __import__(self.name)
                self.db = database.DataBase
                return
        except ImportError as msg:
            print(msg)
        
        try:
            sys.path.insert(1, self.path)
        except Error as msg:
            print(msg)

        try:
            database = __import__(self.name)

        except ImportError as msg:
            print(msg)

        self.db = database.DataBase

    
    def add_key(self, key, value):
        """Add key with corresponding value to the database"""
        try:
            if self.db.get(key):
                raise KeyError("The key is already found in the database, you may use the override method. to override it.")
            self.db[key] = value

            if self.auto: self.save()

        except KeyError as msg:
            print(msg)


    def override(self, key, new_value):
        """Overrides existing keys' values by new_value"""
        try:
            if not self.db.get(key):
                raise KeyError("The key is not found in the database, you may add it using add_key method.")

            self.db[key] = new_value

            if self.auto: self.save()

        except KeyError as msg:
            print(msg)

    
    def delete_key(self, key):
        """Deletes the specified key"""
        try:
            del self.db[key]
            if self.auto: self.save()

        except KeyError as msg:
            print(msg)


    def get_key(self, key):
        """Returns the value of the passed key"""
        try:
            return self.db[key]
        except KeyError as msg:
            print(msg)


    def display(self):
        """Prints each key with its corresponding value in a clean way"""
        for key, value in self.db.items():
            print(key, ':', value)


    def delete_database(self):
        """Deletes the current database you are working with"""
        make_sure = input("Are you sure you want to delete the DataBase '" + self.name +"'?\nType yes to confirm.\n")
        if make_sure.lower() != "yes": return
        try:
            import os
            os.remove(self.path+"\\"+self.name+".py")
            print(f"The DataBase {self.name} has been deleted.")
        except:
            raise NameError("Please make sure the database you entered exists")


    def enable_autosave(self):
        self.auto = True


    def disable_autosave(self):
        self.auto = False


    def save(self):
        """Saves the database, notice that without saving it, nothing in the database will change so be careful"""
        file = open(self.path +"\\" + self.name + ".py", "w+")
        file.write("DataBase = ")
        file.write(str(self.db))
        file.close()


    def __str__(self):
        return "<Key-Value DataBase: " + str(len(self.db)) + " row(s)>"
