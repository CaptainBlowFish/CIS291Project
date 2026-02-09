import setuptools
from setuptools import setup


# The actual setup function call:
setup(
    name="DMS_Core",
    version="0.1.dev0",
    description="Document Management System",
    package_dir={
        "": "src",
        # ...
    },
    packages=setuptools.find_packages(),
    package_data={
#        "dms_core": [
#            "filename.ext",
#            # ...
#        ]
    },
    entry_points={
#        "console_scripts": [
#            "executable_name = namespace.path:function",
#            # ...
#        ],
    },
)
