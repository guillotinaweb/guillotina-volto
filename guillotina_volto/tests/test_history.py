import json

import pytest


pytestmark = pytest.mark.asyncio


async def test_history_creation(cms_requester):
    async with cms_requester as requester:

        resp, status = await requester(
            "POST",
            "/db/guillotina/",
            data=json.dumps({"@type": "Document", "title": "Document 1", "id": "doc1"}),
        )

        resp, status = await requester("GET", "/db/guillotina/doc1")

        behavior = resp["guillotina.contrib.workflows.interfaces.IWorkflowBehavior"]
        assert behavior["history"] is not None
        assert behavior["history"][0]["title"] == "Created"

        resp, status = await requester("GET", "/db/guillotina/doc1/@workflow")

        assert resp["history"] is not None
        assert resp["history"][0]["title"] == "Created"
