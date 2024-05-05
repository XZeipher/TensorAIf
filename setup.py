from setuptools import setup

requirements = ['aiohttp','aiofiles']
readme = ''
with open('README.md', encoding="utf8") as f:
    readme = f.read()

setup(
    name='TensorART',
    author='Alpha Coder',
    author_email='alphacoders@yahoo.com',
    version='0.1',
    long_description=readme,
    url='https://github.com/XZeipher/TENSOR',
    license='GNU General Public License v3.0',
    classifiers=[
        "Framework :: AsyncIO",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='API BASED IMAGE GENERATOR PYPI.',
    include_package_data=True,
    keywords=['ai', 'ml', 'bot', 'api', 'image',
              'prompt'],
    install_requires=requirements
)
