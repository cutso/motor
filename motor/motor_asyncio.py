# Copyright 2011-2015 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Asyncio support for Motor, an asynchronous driver for MongoDB."""

__all__ = ['AsyncIOMotorClient']

from . import core, motor_gridfs
from .frameworks import asyncio as asyncio_framework
from .metaprogramming import create_class_with_framework


def create_asyncio_class(cls):
    return create_class_with_framework(cls, asyncio_framework, 'motor_asyncio')


AsyncIOMotorClient = create_asyncio_class(core.AgnosticClient)


AsyncIOMotorDatabase = create_asyncio_class(
    core.AgnosticDatabase)


AsyncIOMotorCollection = create_asyncio_class(
    core.AgnosticCollection)


AsyncIOMotorCursor = create_asyncio_class(
    core.AgnosticCursor)


AsyncIOMotorCommandCursor = create_asyncio_class(
    core.AgnosticCommandCursor)


AsyncIOMotorAggregationCursor = create_asyncio_class(
    core.AgnosticAggregationCursor)


AsyncIOMotorBulkOperationBuilder = create_asyncio_class(
    core.AgnosticBulkOperationBuilder)


AsyncIOMotorGridFS = create_asyncio_class(
    motor_gridfs.AgnosticGridFS)


AsyncIOMotorGridFSBucket = create_asyncio_class(
    motor_gridfs.AgnosticGridFSBucket)


AsyncIOMotorGridIn = create_asyncio_class(
    motor_gridfs.AgnosticGridIn)


AsyncIOMotorGridOut = create_asyncio_class(
    motor_gridfs.AgnosticGridOut)


AsyncIOMotorGridOutCursor = create_asyncio_class(
    motor_gridfs.AgnosticGridOutCursor)
