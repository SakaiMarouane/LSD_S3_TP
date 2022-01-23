#EX1:
# Person : is a class defined in the global scope. It is a global variable.
# person : is an instance of the Person class. It is also a global variable.
# surname : is a carracterestique of the variable person
# AGE :  is a method of the Person class. It is a local variable in the scope of the class.
# age : is a local variable inside the scope of the age method.

#EX2:
class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self._age = None
        self._age_last_recalculated = None
        self._recalculate_age()
    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self._age = age
        self._age_last_recalculated = today
    def age(self):
        if (datetime.date.today() > self._age_last_recalculated):
            self._recalculate_age()
        return self._age


#EX3:
# name :an instance attribute which is set in the constructor
# surname : a class attribute, and cannot be overridden in the constructor
# profession : is a class attribute, but it can optionally be overridden by an instance attribute in the constructor. 

#EX4:
class number():
  MULTIPLIER  = 5
  def __init__(self,x,y):
    if type(x) != int() or type(y) != int():
      self.x = x
      self.y = y
    else:
      raise ValueError;
  def add(self):
    return self.x + self.y
  def multiply(self, a):
        return self.MULTIPLIER * a
  def subtract(b,c):
        return b-c
  def value(self):
        return self.x, self.y

#EX6:
class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    def __str__(self):
        attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s: %s" % (classname, " ".join(attrs))
