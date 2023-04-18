from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

# Import forms
from .add_film_form import AddFilmForm
from .add_director_form import AddDirectorForm
