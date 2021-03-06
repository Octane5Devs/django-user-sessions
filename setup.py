from setuptools import setup, find_packages

setup(
    name='django-user-sessions',
    version='1.5.3',
    description='Django sessions with a foreign key to the user',
    long_description=open('README.rst').read(),
    author='Bouke Haarsma',
    author_email='bouke@webatoom.nl',
    url='http://github.com/Bouke/django-user-sessions',
    download_url='https://pypi.python.org/pypi/django-user-sessions',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests',)),
    install_requires=['Django>=1.8'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
)
