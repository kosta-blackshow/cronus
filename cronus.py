from backend import app, db
from backend.models import Patient

@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        Patient=Patient
    )
