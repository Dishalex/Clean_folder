from setuptools import setup, find_namespace_packages

setup(name='Clean folder',
      version='0.0.1',
      description='Package for sorting folders',
      url='https://github.com/Dishalex/Clean_folder',
      author='Oleksandr Dyshliuk',
      author_email='dishalex@gmail.com',
      license='MIT',
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],
      packages=['clean_folder'],
      include_package_data=True,
      #      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_my_folder=clean_folder.clean: main']})
