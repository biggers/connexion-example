# connexion-example/secrets-example.py
# RENAME.ME to secrets.py, and "fix" any secrets
# ... FIX.ME -- this is hardly the "best way" to do this...

def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        return {'sub': 'admin'}

    # optional: raise exception for custom error response
    return None


def get_secret(user):
    return "You are {user} and the secret is 'wbevuec'".format(user=user)
