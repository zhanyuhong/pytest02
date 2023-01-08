import os

import pytest



if __name__=='__main__':
    # pytest.main(['-vs','./interface_testcase/test_interface.py::test_04_function'])
    # pytest.main(['-vs','./testcase','--reruns=2','-n=2'])
    pytest.main()
    os.system('allure generate ./temp -o ./report  --clean')