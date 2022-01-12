from app import app, db
from app.models import Patient

@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        Patient=Patient
    )
