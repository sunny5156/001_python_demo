1.安装gcc 
sudo apt-get build-dep gcc


安装cython

 pip install Cython

安装python-devel




2.编译整个目录:
将需要编译的目录和setup.py放在同一层级,

执行python setup.py 

如果
编译某个文件夹：
    python py-setup.py BigoModel





3、生成结果：
  目录 build 下

生成完成后



4、启动文件还需要py/pyc担当，须将启动的py/pyc拷贝到编译目录并删除so文件
