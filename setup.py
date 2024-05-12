from setuptools import setup, find_packages


setup(
    name='sigaocaue_normalized_folder_name',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'click',
        'unidecode',
        'gnureadline',
        'pyreadline'
    ],
    entry_points={
        'console_scripts': [
            'normalized_folder_name=normalized_folder_name.normalized_folder_name_cli:cli'
        ]
    }
)
