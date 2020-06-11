import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-tablefield",
    version="0.0.1b",
    author="Yury Lapshinov",
    author_email="y.raagin@gmail.com",
    description="tables in django admin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raagin/django-tablefield",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    python_requires='>=3',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)