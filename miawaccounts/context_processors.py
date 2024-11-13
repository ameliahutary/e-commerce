import os
from django.conf import settings

def versioned_static(request):
    version = 'v1.1'  
    return {
        'STATIC_VERSION': version,
    }
