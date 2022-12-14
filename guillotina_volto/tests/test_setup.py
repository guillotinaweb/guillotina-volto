import asyncio

import pytest

from guillotina_volto.tests.utils import add_content


pytestmark = pytest.mark.asyncio


async def test_basic_content(cms_requester):
    async with cms_requester as requester:
        await add_content(requester)
        await asyncio.sleep(1)
