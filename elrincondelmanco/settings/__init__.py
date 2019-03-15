from __future__ import absolute_import
import os
try:
	username=os.uname()[1]
except Exception:
	from .dev import *
else:
	if username == 'vps153696':
		from .prod import *
	else:
		from .dev import *
		