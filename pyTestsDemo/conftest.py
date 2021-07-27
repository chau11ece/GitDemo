import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute FIRST")
    yield
    print("I will executed LAST")


@pytest.fixture()
def data_load():
    print("User profile data is being created")
    return ["chau", "tran", "chau.tran@mailinator.com"]


@pytest.fixture(params=[("chrome", "chau", "tran"), ("Firefox", "nathalia"), "IE"])
def cross_browser(request):
    return request.param


