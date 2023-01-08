import pytest

@pytest.fixture(scope='class',params=['测试1222','测试222222','测试333333'])
def my_fixture(request):
    # print("\n这是前置的方法")
    # yield
    # print("\n这是后置的方法")
    return request.param
