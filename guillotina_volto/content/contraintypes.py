from guillotina import FACTORY_CACHE
from guillotina import app_settings
from guillotina import configure
from guillotina.constraintypes import FTIConstrainAllowedTypes
from guillotina.interfaces import IConstrainTypes
from zope.interface import Interface

from guillotina_volto.interfaces import ICMSConstrainTypes


@configure.adapter(for_=Interface, provides=ICMSConstrainTypes)
class CMSCustomAllowedTypes(FTIConstrainAllowedTypes):
    def get_allowed_types(self) -> list:
        tn = getattr(self.context, "__allowed_types__", None)
        if tn is None:
            tn = super(CMSCustomAllowedTypes, self).get_allowed_types()

        if tn is None:
            tn = FACTORY_CACHE.keys()
        global_disallowed_types = app_settings.get("global_disallowed_types", [])
        return [type_ for type_ in tn if type_ not in global_disallowed_types]


@configure.adapter(for_=Interface, provides=IConstrainTypes)
class NativeCustomAllowedTypes(FTIConstrainAllowedTypes):
    def get_allowed_types(self) -> list:
        tn = getattr(self.context, "__allowed_types__", None)
        if tn is None:
            tn = super(NativeCustomAllowedTypes, self).get_allowed_types()

        if tn is None:
            tn = FACTORY_CACHE.keys()
        return tn
