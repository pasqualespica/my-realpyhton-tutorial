from contextlib import contextmanager
import secrets


def gen_token():
    """Generate a random token."""
    return f'TOKEN_{secrets.token_hex(8)}'


@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex
    function during testing.
    """
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex


def test_gen_key():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"


# test_gen_key()
