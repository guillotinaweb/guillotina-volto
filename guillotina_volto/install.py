# -*- coding: utf-8 -*-
from guillotina import configure
from guillotina.addons import Addon
from guillotina.behaviors.dublincore import IDublinCore
from guillotina.interfaces import ILayers
from guillotina.utils import get_registry

from guillotina_volto.behaviors.image import IImageAttachment
from guillotina_volto.behaviors.syndication import ISyndicationSettings
from guillotina_volto.interfaces import IBlocks
from guillotina_volto.interfaces import ICMSBehavior
from guillotina_volto.interfaces import IImagingSettings
from guillotina_volto.interfaces import IMenu


CMS_LAYER = "guillotina_volto.interfaces.ICMSLayer"


@configure.addon(name="cms", title="Guillotina CMS")
class CMSAddon(Addon):
    @classmethod
    async def install(cls, container, request):
        container.add_behavior(ISyndicationSettings)
        container.add_behavior(IImageAttachment)
        container.add_behavior(ICMSBehavior)
        container.add_behavior(IDublinCore)
        container.add_behavior(IBlocks)
        container.register()

        registry = await get_registry()
        registry.for_interface(ILayers)["active_layers"] |= {CMS_LAYER}
        registry.register_interface(IImagingSettings)
        registry.register_interface(IMenu)
        registry.register()

    @classmethod
    async def uninstall(cls, container, request):
        container.remove_behavior(ISyndicationSettings)
        registry = await get_registry()
        registry.for_interface(ILayers)["active_layers"] -= {CMS_LAYER}
        registry.register()
