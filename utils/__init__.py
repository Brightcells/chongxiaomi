#!/usr/bin/env python
# encoding: utf-8

import os
import datetime
import re


def get_safe_now():
    from django.conf import settings
    from django.utils.timezone import utc
    if settings.USE_TZ:
        return datetime.datetime.utcnow().replace(tzinfo=utc)
    return datetime.datetime.now()


def mkdir(path):
    """
    """
    if not os.path.exists(path):
        os.makedirs(path, 0755)
        return True
    return False


def handle_uploaded_file(f, prefix='', extension=None):
    """
    """
    from django.conf import settings
    from uuid import uuid4
    from shutil import copyfileobj

    hash_name = uuid4().get_hex()

    time_section = os.path.join(prefix,
                                datetime.datetime.utcnow().strftime('%Y/%m'))
    full_path = os.path.join(settings.MEDIA_ROOT, time_section)

    mkdir(full_path)

    if extension:
        hash_name += '.' + extension

    target_path = os.path.join(full_path, hash_name)

    with open(target_path, 'wb+') as destination:
        copyfileobj(f, destination)
    return os.path.join(time_section, hash_name)


def get_referer_view(request, default=None):
    '''
    Return the referer view of the current request

    Example:

    def some_view(request):
    ...
    referer_view = get_referer_view(request)
    return HttpResponseRedirect(referer_view, '/accounts/login/')
    '''

    # if the user typed the url directly in the browser's address bar
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return default

    # remove the protocol and split the url at the slashes
    referer = re.sub('^https?:\/\/', '', referer).split('/')
    '''
    if referer[0] != request.META.get('SERVER_NAME'):
        return default
    '''

    # add the slash at the relative path's view and finished
    referer = u'/' + u'/'.join(referer[1:])
    return referer


def unicode_encode(s):
    """
    Detect if a string is unicode and encode as utf-8 if necessary
    """
    return isinstance(s, unicode) and s.encode('utf-8') or s
