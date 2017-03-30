# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: This module is here as a nasty work-around. The config parsing code
# relies on horrible and unpredictable import ordering and we need work around
# to make it work so the config doesn't get parsed multiple times.
# Real solution is nuking this awful config parsing and setting related code
# from orbit.

from st2tests.base import EventletTestCase
from st2tests.base import DbTestCase
from st2tests.base import DbModelTestCase

__all__ = [
    'EventletTestCase',
    'DbTestCase',
    'DbModelTestCase'
]
