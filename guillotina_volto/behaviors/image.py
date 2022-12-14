from guillotina import configure
from guillotina import schema
from guillotina.fields import CloudFileField
from guillotina.interfaces import IResource
from zope.interface import Interface

from guillotina_volto.interfaces import IHasImage


@configure.behavior(title="Image attachment", for_=IResource, marker=IHasImage)
class IImageAttachment(Interface):

    image = CloudFileField()

    caption = schema.TextLine()


@configure.behavior(title="Lead image attachment", for_=IResource, marker=IHasImage)
class ILeadImage(Interface):

    lead = CloudFileField()
