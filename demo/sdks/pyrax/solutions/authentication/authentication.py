import os
import pyrax


pyrax.set_credentials(os.getenv('RAX_USERNAME'), os.getenv('RAX_API_KEY'))
print "Authenticated"

