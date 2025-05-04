import datetime

# ADT: Person
# The Person class abstracts the concept of a person with a name and a birthday.
# Users of the class do not need to know how names or dates are stored or managed.

class Person:
    def __init__(self, name):
        """Initialize a person with a full name. Abstracts away the parsing logic."""
        self._name = name
        
        # Abstracts how we derive the last name from full name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except ValueError:
            self._last_name = name

        self._birthday = None  # Abstracts birthdate as optional data

    def get_name(self):
        """Public interface to get full name (no internal details exposed)"""
        return self._name

    def get_last_name(self):
        """Public interface to get last name"""
        return self._last_name

    def set_birthday(self, birthday):
        """Sets the birthday (expects datetime.date object).
        Hides internal storage details from the user."""
        self._birthday = birthday

    def get_age(self):
        """Returns age in days.
        Abstracts away the calculation from the user."""
        if self._birthday is None:
            raise ValueError("Birthday not set")
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """Compare persons by last name, then by full name.
        Abstracts comparison logic for sorting."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Return string representation of the person (their full name)."""
        return self._name
