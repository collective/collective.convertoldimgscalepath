# -*- coding: utf-8 -*-
from plone import api
from plone.app.textfield.value import RichTextValue
from plone.protect.interfaces import IDisableCSRFProtection
from Products.Five import BrowserView
from zope.interface import alsoProvides
import re


class ConvertScalePathsView(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        items = api.content.find(
            portal_type=('Document', 'News Item', 'Event', ),
            path='/'.join(self.context.getPhysicalPath())
        )
        for item in items:
            obj = item.getObject()
            if obj.text and '/image_' in obj.text.raw:
                obj.text = RichTextValue(
                    re.sub(r"(\/image_)(.*?)", r"/@@images/image/\2",
                           obj.text.raw),
                    mimeType=obj.text.mimeType,
                    encoding=obj.text.encoding,
                    outputMimeType=obj.text.outputMimeType,
                )
                print "Image paths converted for {0}".format(
                    obj.absolute_url())
