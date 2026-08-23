import os

class This(dict):
    def __init__(self):
        prefix = os.environ['THIS']
        for key,val in os.environ.items():
            if key.startswith(prefix):
                shortkey = '_'.join(key.split('_')[2:])
                if shortkey:
                    self[shortkey] = val
    def __getattr__(self, name):
        return self[name]


def test_THIS_NAME():
    from pathlib import Path
    import __me__ as ME 
    name=Path(__file__).parent.parent.parent.name
    if not ME.THIS.NAME == name:
        print("""
        UPDATE NAME IN pytest.ini'
        """)
    assert ME.THIS.NAME == name

THIS=This()
