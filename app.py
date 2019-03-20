#!/usr/bin/env python3
import datetime

import logging
import logzero
from logzero import logger

import connexion
from connexion import NoContent

from secrets import (basic_auth, get_secret)

# our memory-only pet storage
PETS = {}

logzero.loglevel(logging.DEBUG)
log = logger


def get_pets(limit, animal_type=None):
    return {"pets":
            [pet for pet in PETS.values() if not animal_type or
             pet['animal_type'] == animal_type][:limit]
            }


def get_pet(pet_id):
    pet = PETS.get(pet_id)
    log.info("get, pet_id <%s>", pet_id)
    return pet or ("Not found", 404)


def put_pet(pet_id, pet):
    exists = pet_id in PETS
    pet['id'] = pet_id
    if exists:
        log.info("update, pet_id <%s>", pet_id)
        PETS[pet_id].update(pet)
    else:
        log.info("create, pet_id <%s>", pet_id)
        pet['created'] = datetime.datetime.utcnow()
        PETS[pet_id] = pet
    return NoContent, (200 if exists else 201)


def delete_pet(pet_id):
    if pet_id in PETS:
        log.info("delete, pet_id <%s>", pet_id)
        del PETS[pet_id]
        return NoContent, 204
    else:
        return NoContent, 404


app = connexion.App(__name__)
app.add_api('petstore_swagger.yml')

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app

application = app.app


if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
