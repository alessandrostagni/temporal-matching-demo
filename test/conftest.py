import pytest

from LinkStream.LinkStream import LinkStream


@pytest.fixture
def link_stream():
    return LinkStream()
