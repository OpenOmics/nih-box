#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Python standard library
from __future__ import print_function
import configparser, os, sys 

# Local imports
from utils import fatal, err

# 3rd party imports
from boxsdk import Client, OAuth2


def parsed(config_file = None, required = [
        'client_id', 'client_secret', 
        'access_token', 'refresh_token'
        ]
    ):
    """Parses config file in TOML format. This file should contain
    keys for client_id, client_secret, access_token, refresh_token.
    The `auth` function below will update the values of access_token
    and refresh_token to keep the users token alive. This is needed 
    because the developer tokens have a short one hour life-span.
    @Example `config_file`:
    [secrets]
    client_id = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    client_secret = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    access_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    refresh_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    @param config_file <str>:
        Path to config file, default location: ~/.config/bx/bx.toml 
    @return [client_id, client_secret, access_token, refresh_token]:
        Returns a list of <str> with authenication information:
            [0] client_id
            [1] client_secret
            [2] access_token
            [3] refresh_token
    """
    # Information to parse from config file
    secrets, missing = [], []
    if not config_file:
        # Set to default location
        # ~/.config/bx/bx.toml
        home = os.path.expanduser("~")
        # TODO: add ENV variable to
        # override this default PATH
        config_file = os.path.join(home, ".config", "bx", "bx.toml")  

    # Read and parse in config file 
    config = configparser.ConfigParser()
    config.read(config_file)
    # Get authentication information,
    # Collect missing required info
    # to pass to user later
    for k in required:
        try:
            v = config['secrets'][k]
            secrets.append(v)
        except KeyError as e:
            missing.append(k)

    if missing:
        # User is missing required 
        # Authentication information
        fatal(
            'Fatal: bx config {0} is missing these required fields:\n\t{1}'.format(
                config_file,
                missing
            )
        )

    return secrets


def update(access_token, refresh_token, config_file=None):
    """Callback to update the authentication tokens. This function is 
    passed to the `boxsdk OAuth2` constructor to save new `access_token` 
    and `refresh_token`. The boxsdk will automatically refresh your tokens
    if they are less than 60 days old and they have not already been re-
    freshed. This callback ensures that when a token is refreshed, we can
    save it and use it later.
    """
    if not config_file:
        # Set to default location
        # ~/.config/bx/bx.toml
        home = os.path.expanduser("~")
        # TODO: add ENV variable to
        # override this default PATH
        config_file = os.path.join(home, ".config", "bx", "bx.toml")
    # Read and parse in config file 
    config = configparser.ConfigParser()
    config.read(config_file)
    # Save the new `access_token` 
    # and `refresh_token`
    config['secrets']['access_token'] = access_token
    config['secrets']['refresh_token'] = refresh_token
    with open(config_file, 'w') as ofh:
        # Method for writing is weird, but
        # this is what the docs say todo
        config.write(ofh)


def authenticate(client_id, client_secret, access_token, refresh_token):
    """Authenticates a user with their client id, client secret, and tokens.
    By default, authentication information is stored in "~/.config/bx/bx.toml".
    Here is an example of bx.toml file:
    [secrets]
    client_id = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    client_secret = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    access_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    refresh_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    NOTE: This operation needs to be performed prior to any Box API calls. A 
    Box developer token has a short life-span of only an hour. This function will
    automatically refresh a token, to extend its life, when called. A token that
    has an expiration date past 60 days CANNOT be refreshed. In this scenario, a 
    user will need to create a new token prior to running the tool. A new token 
    can be create by creating an new 0auth2 app here: http://developers.box.com/
    """
    auth = OAuth2(
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token,
        store_tokens = update
    )

    try:
        access_token, refresh_token = auth.refresh(None)
    except Exception as e:
        # User may not have refreshed 
        # their token in 60 or more days
        err(e)
        err("\nFatal: Authentication token has expired!")
        fatal(" - Create a new token at: https://developer.box.com/")
    
    return access_token, refresh_token



if __name__ == '__main__':
    try:
        # Use user provided config
        test_file = sys.argv[1]
    except IndexError:
        # Test auth config file parser
        home = os.path.expanduser("~")
        test_file = os.path.join(home, ".config", "bx-dev", "bx.toml")
    
    client_id, client_secret, access_token, refresh_token = parsed(
        config_file = test_file
    )

    # Test token refresh 
    new_access_token, new_refresh_token = authenticate(
         client_id = client_id, 
         client_secret = client_secret,
         access_token = access_token, 
         refresh_token = refresh_token
    )

    # Manually update tokens
    update(
        access_token = new_access_token, 
        refresh_token = new_refresh_token, 
        config_file = test_file
    )

    # Test authentication
    auth = OAuth2(
        client_id = client_id,
        client_secret = client_secret,
        access_token = new_access_token,
        refresh_token = new_refresh_token,
        store_tokens = update
    )

    # Get user info
    client = Client(auth)
    user = client.user().get()
    print("The current user ID is {0}".format(user.id))