import setuptools
from distutils.core import setup

setup(name='Ohadutils',
      version='1.0',
      description="Ohad Rubin's utilities",
      author='Ohad Rubin',
      author_email='iohadrubin@gmail.com',
      url='',      
      long_description_content_type="text/plain",
      
      packages=setuptools.find_packages(),
      include_package_data=True,
      classifiers=[],
      python_requires=">=3.6",
      install_requires=[
            # By definition, a Custom Component depends on Streamlit.
            # If your component has other Python dependencies, list
            # them here.
            "sqlitedict == 2.0.0",
            "appdirs == 1.4.4",
            "fire == 0.4.0",
            "filelock == 3.8.0",
            "loguru == 0.6.0",
            "cryptography==37.0.1",
            "redis-dict==1.6.0",
      ],
      
      entry_points={"console_scripts": ["tiny_queue = tiny_queue.cli:main"]},
     )