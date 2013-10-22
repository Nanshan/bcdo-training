import os
import re
import libcloud.security
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

Driver = get_driver(Provider.EC2_US_WEST)

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', 'AKIAJAYGQMYOTCOULBYQ')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', '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')
assert AWS_ACCESS_KEY is not None
assert AWS_SECRET_KEY is not None

conn = Driver(AWS_ACCESS_KEY, AWS_SECRET_KEY)

