import os

import pytest

from LinkStream.LinkStream import LinkStream


@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    output_folder = 'test/test_output'
    if not os.path.exists(output_folder):
        os.path.mkdir(output_folder)

@pytest.fixture
def link_stream():
    return LinkStream()
