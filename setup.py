import setuptools

from pdf2txt.version import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf2txt",
    version=__version__,
    author="Mohamed Ben Haddou",
    author_email="mbenhaddou@mentis.io",
    include_package_data=True,
    description="A better pdf to text extraction toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["pandas", "pdf2image", "pdfminer.six", "Pillow","PyPDF2"],
    url="",
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.json', '*.npy', '*.db'],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
    ],
    python_requires='>=3.6',
)
