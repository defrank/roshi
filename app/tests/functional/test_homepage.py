"""
Application home views testing.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""


def test_basic_unauthenticated(client):
    """
    Most important test.  That our homepage loads error free.

    """
    response = client.get('/')
    assert response.status_code == 200
