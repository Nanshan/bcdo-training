import os
import re
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.EC2_US_WEST)

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', 'AKIAJOM4IDJVZSUA4SEQ')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', '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')
assert AWS_ACCESS_KEY is not None
assert AWS_SECRET_KEY is not None

conn = Driver(AWS_ACCESS_KEY, AWS_SECRET_KEY)

