from backend import server, db
from backend.models import Patient


@server.shell_context_processor
def make_shell_context():
    return dict(
        server=server,
        db=db,
        Patient=Patient
    )
