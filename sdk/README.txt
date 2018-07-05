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

    #工具包安装
    ##产生.whl文件，bdist_wheel需要
    pip install wheel
    ##mac os下macports安装位于/opt/local/Library/Frameworks/Python.framework/Versions/3.6/bin/twine
    ##需要将twine加入环境变量PATH中
    pip install twine

    #打包
    python setup.py sdist bdist_wheel --universal

    #由于上传的包同版本不能重复，可先上传到pypi测试环境
    twine upload dist/* -r test

    #pypi正式环境
    twine upload dist/* -r pypi

3.查看python的site-packages目录地址

 python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"

