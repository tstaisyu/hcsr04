from setuptools import setup

package_name = 'hcsr04'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'python_programs.talker',
        'python_programs.listener',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='user',
    author_email="user@todo.todo",
    maintainer='user',
    maintainer_email="user@todo.todo",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker= python_programs.talker:main',
            'listener= python_programs.listener:main',
        ],
    },
)
