# from setuptools import setup, find_packages

# setup(
#     name="black_box",
#     version="0.1.0",
#     packages=find_packages(exclude=["tests*"]),
#     install_requires=[
#         "pyserial",  # for serial communication
#         "requests",  # for HTTP requests (data uploading)
#         "pandas",    # for data manipulation and CSV handling
#         # Add other dependencies here
#     ],
#     entry_points={
#         "console_scripts": [
#             "black_box=black_box.main:main",
#         ],
#     },
#     author="Travis",
#     author_email="travisfernandes2327@gmail.com",
#     description="A black box system for collecting and uploading car data",
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/travis2319/blackbox",
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.6",
# )