from tools.validator import *
from tools.validator.personal_data_validator import validate_email

assert validate_email("_abc")== False
assert validate_email("fafa@qmail.ir")== True