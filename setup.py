from setuptools import setup, find_packages

setup(name="pyeogpr",
      version ="1.0.1",
      description="Python based library to use Earth Observation data to retrieve biophysical maps using Gaussian Process Regression",
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      author = "Dávid D.Kovács",
      author_email = "daviddkovacs@gmail.com",
      packages = find_packages(include=["pyeogpr","pyeogpr.*"]),
      install_requires = ["numpy","openeo","scipy"])
