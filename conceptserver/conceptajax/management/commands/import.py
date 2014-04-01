import csv

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

import wiki
import wiki.models

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        f = csv.reader(open(args[0]), delimiter = '\t')
        for l in f:
            if l[0] == "":
                continue
            if l[1] == "":
                title = l[0]
                continue
            slug = l[1]
            for c in ",.-&()/\\:* =":
                slug = slug.replace(c, "_")
            article = "*"+title+"*: "+ l[0]
            root = wiki.models.URLPath.objects.get(id = 1)
            user = User.objects.get(id = 1)
            group = None

            print "Importing [{parent}]/[{slug}]".format(parent = str(root), slug = str(slug))

            wiki.models.URLPath.create_article(
                parent = root, # parent article
                slug = slug, # slug
                title = slug, # title
                content = article,
                user_message = "Import", # Edit message
                user = user,
                ip_address = "127.0.0.1",
                article_kwargs = {'owner': user,
                                  'group': group,
                                  'group_read': True,
                                  'group_write': True,
                                  'other_read': True,
                                  'other_write': True,
                                  })
