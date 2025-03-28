import pytest

@pytest.fixture()
def some_data():
    yield 42

def test_some_data(some_data):
    assert some_data == 42

@pytest.fixture(scope='module')
def example_data():
    """Fixture returning a sample list."""
    return [1, 2, 3]

def test_sum(example_data):
    print("example_data:", example_data)
    print("Sum", sum(example_data))

def test_length(example_data):
    print("example_data:", example_data)
    print("Len", len(example_data))
    assert len(example_data) == 3