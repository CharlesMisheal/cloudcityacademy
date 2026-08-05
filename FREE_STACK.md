# CloudCity Academy

Free Python academy app for beginners and advanced classes.

**Public free URL (when you claim the free PythonAnywhere username):**  
https://cloudcity.pythonanywhere.com

## Zero paid cost stack

| Thing | What we use | Cost |
|--------|-------------|------|
| App | Flask | Free / open source |
| Database | SQLite file on disk | Free |
| Hosting | PythonAnywhere free web app | Free |
| Screenshots | Local folder `static/uploads` | Free |
| PDF certificates | reportlab | Free |
| Fonts | Google Fonts (Fraunces + Figtree) | Free |
| Auth | Passwords hashed with werkzeug | Free |

No Supabase, Firebase, paid domains, paid storage, or paid APIs.

## Run locally (free)

```bash
cd cloudcity
python -m pip install --user -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

### Demo accounts (seeded on first run)

| Role | Email | Password |
|------|--------|----------|
| Admin | admin@cloudcity.local | Admin123! |
| Teacher | teacher@cloudcity.local | Teacher123! |

Students: use **Register free** and choose Beginner or Advanced.

## Deploy free on PythonAnywhere

1. Create a **free** account with username **`cloudcity`** so the site is `cloudcity.pythonanywhere.com`.
2. In **Files**, upload this `cloudcity` folder (or clone from Git if you use free GitHub).
3. Open a **Bash** console and run:

```bash
cd ~/cloudcity   # or wherever you uploaded
python3 -m pip install --user -r requirements.txt
```

4. **Web** tab → **Add a new web app** → Manual configuration → Python 3.x (free).
5. Set **Source code** path to the folder that contains `app.py` / `wsgi.py`.
6. Edit the WSGI file to:

```python
import sys
path = '/home/cloudcity/cloudcity'  # your real path
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

7. Reload the web app. Visit https://cloudcity.pythonanywhere.com

### Important free-tier notes

- Free accounts sleep when idle; first load may be slow — still free.
- Do not enable paid upgrades, custom domains, or always-on unless you choose to pay later.
- Change demo passwords after first login.
- Back up `instance/cloudcity.db` and `static/uploads` occasionally (download via Files).

## Features

- Student registration + course choice (Beginners / Advanced)
- Student weekly notes, MCQ + subjective + screenshot tests
- Teacher notes / questions / review of submissions
- Admin user list, assessment view (with names), end-of-course PDF certificates
