import pytest
from pyTestsDemo.baseclass import BaseClass


# from pyTestsDemo.conftest import data_load


@pytest.mark.usefixtures("data_load")
class TestExample2(BaseClass):
    def test_edit_profile(self, data_load):
        log = self.get_logger()
        log.info(data_load[0])
        log.info(data_load[2])
        # print(data_load[0])
        # print(data_load[2])
