from setuptools import setup, find_packages

setup(
    name='repo-hf-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'huggingface_hub'
    ],
    entry_points={
        'console_scripts': [
            'repo-hf-cli=repo_hf_cli.repo_hf_cli:main',
        ],
    },
    author='Denis Kropp',
    author_email='dok@directfb1.org',
    description='Repo-level completion tool.',
    url='https://github.com/deniskropp/repo-hf-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
