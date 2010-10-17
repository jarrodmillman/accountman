"""Simple command-line interface for managing account information.

The account db is a dictionary of dictionaries.  This db is stored
as json file.
"""

import json

import passman

account_fields = ['url', 'name']

def load(filename):
    """Open the file containing the account DB.

    Parameters
    ----------
    filename : string

    Returns
    -------
    accounts : dictionary
    """
    with open(filename, 'r') as f:
        accounts = json.load(f)
    
    return accounts

def save(accounts, filename):
    """Save the file containing the account DB.

    Parameters
    ----------
    accounts : dictionary
    filename : string

    Returns
    -------
    status : dictionary
    """
    with open(filename, 'w') as f:
        status = json.dump(accounts, f, indent=4)
    
    return status

def new():
    """Create a new account entry.

    Returns
    -------
    account : dictionary
    """
    account = {}
    for field in account_fields:
       account[field] = raw_input(field+": ")

    account['password'] = passman.getpass()
    return account

def pprint(accounts):
    """Pretty print the account db.

    Parameters
    ----------
    accounts : dictionary
    """
    print json.dumps(accounts, sort_keys=True, indent=4)
