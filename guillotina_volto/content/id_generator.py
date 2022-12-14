from guillotina import app_settings
from guillotina import configure
from guillotina.interfaces import IIDGenerator

from guillotina_volto.interfaces import ICMSLayer


@configure.adapter(for_=ICMSLayer, provides=IIDGenerator)
class IDGenerator(object):
    """Default IDGenerator adapter.

    Requires request to adapt on different layers. Returns the urls path id.
    """

    def __init__(self, request):
        self.request = request

    def __call__(self, data):

        if "title" in data:
            new_id = data["title"].lower().replace(" ", "-")
        elif "@type" in data and data["@type"] == "Image":
            try:
                new_id = data["image"]["filename"]
            except KeyError:
                return None
        elif "@type" in data and data["@type"] == "File":
            try:
                new_id = data["file"]["filename"]
            except KeyError:
                return None
        else:
            return None
        if new_id:
            if new_id[0] in ("_", "@"):
                new_id = new_id[1:]
            return "".join(
                i for i in new_id if i in app_settings["valid_id_characters"]
            )
        else:
            return None
