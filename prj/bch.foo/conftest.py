from pathlib import Path
import tempfile
name=Path(__file__).parent.name
callback=f"{tempfile.mktemp()}/callback"
def pytest_configure(config):
    import os
    """Inject environment variables before tests are imported."""
    os.environ[ "THIS"            ] = "THIS_35047"
    os.environ[ "THIS_35047_NAME" ] = name
    os.environ[ "THIS_35047_CALLBACK" ] = callback



