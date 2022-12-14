import asyncio
import json


async def add_content(requester, num_folders=2, num_items=10, base_id="cms-"):
    created = 0
    for fidx in range(num_folders):
        path = "/db/guillotina/"
        folder_id = f"{base_id}folder{str(fidx)}"
        resp, status = await requester(
            "POST",
            path,
            data=json.dumps(
                {"@type": "CMSFolder", "title": "Folder" + str(fidx), "id": folder_id}
            ),
        )
        created += 1
        assert status == 201
        path += "/" + folder_id
        for idx in range(num_items):
            resp, status = await requester(
                "POST",
                path,
                data=json.dumps(
                    {
                        "@type": "Document",
                        "title": "Document " + str(idx),
                        "@behaviors": [
                            "guillotina_volto.interfaces.richtext.IRichText"
                        ],
                        "guillotina_volto.interfaces.richtext.IRichText": {
                            "text": {
                                "encoding": "utf-8",
                                "content-type": "",
                                "data": "This is a long text and needs some extra values",  # noqa
                            }
                        },
                    }
                ),
            )
            created += 1
            assert status == 201

    await asyncio.sleep(1)  # make sure async index tasks finish
    return created
