上传至pypi

1.新建~/.pypirc文件：

    [distutils]
    index-servers =
      pypi
      test

    [pypi]
    repository: https://upload.pypi.org/legacy/
    username: test
    password: 123456

    [test]
    repository: https://test.pypi.org/legacy/
    username: test
    password: 123456

2.上传命令

    #由于上传的包同版本不能重复，可先上传到pypi测试环境
    python setup.py sdist upload -r test

    #pypi正式环境
    python setup.py sdist upload ／ python setup.py sdist upload -r pypi

