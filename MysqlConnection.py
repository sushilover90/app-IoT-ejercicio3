class MysqlConnection:
   __instance__ = None

   def __init__(self):
       """ Constructor.
       """
       if MysqlConnection.__instance__ is None:
           MysqlConnection.__instance__ = self
       else:
           raise Exception("You cannot create another MysqlConnection class")

   @staticmethod
   def get_instance():
       """ Static method to fetch the current instance.
       """
       if not MysqlConnection.__instance__:
           MysqlConnection()
       return MysqlConnection.__instance__