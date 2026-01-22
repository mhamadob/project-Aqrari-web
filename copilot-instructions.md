# Copilot / AI agent instructions — EMO project (Django)

Short, actionable guidance so an AI coding agent can be productive immediately.

1. Quick project summary
   - Django project: `EMO` (root: `EMO/settings.py`).
   - Apps: `property` (folder: `property/`), `service_provider`, `client`.
   - DB: SQLite (default in `settings.py` -> `db.sqlite3`).
   - Media: `MEDIA_ROOT` = `media/`, `MEDIA_URL` = `/media/` (see `EMO/settings.py`).

2. Dev environment & essential commands (Windows)
   - Activate virtualenv (PowerShell): `.\env\Scripts\Activate.ps1` or `.\env\Scripts\activate` (cmd).
   - Use venv Python explicitly when scripting: `env\Scripts\python <manage.py command>`.
   - Common commands:
     - `env\Scripts\python manage.py makemigrations`
     - `env\Scripts\python manage.py migrate`
     - `env\Scripts\python manage.py runserver`
     - `env\Scripts\python -m pip install Pillow` (ImageField requires Pillow).
     - `env\Scripts\python manage.py check` (Django system check).

3. Important patterns & project-specific quirks
   - App label vs package name: the app package is `property` (folder `property/`) and its `apps.py` should have `name = 'property'`. If you change the app label, update migration files accordingly (see migrations note below).
   - Model naming: current models use nonstandard lowercase names (`propertys`, `booking`) in `property/models.py`. Be careful: changing model class names requires careful migration handling.
   - ImageField usage: `property.property_image`, `service_provider.service_provider_image`, and `client.client_image` use Django `ImageField` — ensure Pillow is available in the environment before running migrations or system checks.
   - Templates: Project-level `templates/` + app templates in `property/templates/propertys/`, `service_provider/templates/service_provider/`, `client/templates/client/`.
   - Default related names rely on model class names (e.g., `request.user.service_provider.propertys_set.all()` is used in views).

4. Migrations & app-label changes (frequent source of breakage)
   - Migrations store dependencies and literal `to='app_label.modelname'` strings. If you rename an app's label (`apps.py` `name =`), update migration files to reflect that label:
     - Update `dependencies = [('old_label', '000X_...'), ...]` → `('new_label', '000X_...')`
     - Update model references inside migrations `to='old_label.model'` → `to='new_label.model'`
   - Always run migrations with the project's venv Python (e.g., `env\Scripts\python manage.py makemigrations`) so package availability (Pillow, Django) is consistent.
   - Example from this repo: many migrations referenced `('propertys', '...')` while the package is `property/`; we updated dependency tuples and `to='propertys.propertys'` occurrences to use `property` as app label.

5. Files to read first when exploring
   - `EMO/settings.py` — settings, STATIC & MEDIA config, INSTALLED_APPS
   - `EMO/urls.py` — root includes for apps
   - `property/models.py`, `property/views.py`, `property/urls.py`, `property/forms.py` — main domain logic for properties and bookings
   - `service_provider/models.py` — profile creation signals tied to Django `User` model
   - `property/migrations/` — review if changing app labels or models

6. Tests & local verification
   - Run `env\Scripts\python manage.py check` and then `migrate`.
   - Run `env\Scripts\python manage.py test` (if tests exist or as you add them).
   - For functional checks, open dev server and exercise basic pages: property listing (`propertys_page_NE`), property creation, and booking flows.

7. Common quick fixes an AI may need to apply
   - Fix ImportError from wrong package/app names: align `apps.py` `name` with the package (folder) name; update `EMO/settings.py` and `EMO/urls.py` as needed.
   - Fix migration graph errors after renaming an app by updating migration dependency tuples and `to='...'` references.
   - Ensure `admin.py` imports correct model names (e.g., `from .models import propertys, booking`).

8. Style recommendations for contributions
   - Prefer singular, PascalCase model names (`Property`, `Booking`) if you plan a refactor — but that requires careful migrations and DB migration/mapping.
   - Keep `apps.py` `name` equal to the package directory (e.g., `name = 'property'`).

If anything above is unclear or you want me to change the style (e.g., convert `propertys` model to `Property` with automated migrations), tell me which approach you prefer and I will prepare a safe migration plan and code changes. Feedback welcome — I can iterate on this document. 👇