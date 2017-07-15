"""
Test the config.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""


def test_name(config):
    """Verify NAME."""
    name = config['NAME']
    assert name.default == 'petiquette'
    assert name.long == 'Petiquette Dog Training App'
    assert str(name) == name.default
    assert name.default != name.long


def test_allowed_domains(config):
    """Verify ALLOWED_DOMAINS."""
    domains = config['ALLOWED_DOMAINS']
    assert len(domains) == 5

    valid_domains = (
        'petiquette.{}'.format(top)
        for top in ['dog', 'training', 'us', 'dev', 'local']
    )
    for domain in valid_domains:
        assert domain in domains
