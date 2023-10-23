from setuptools import setup

with open("README.md",'r',encoding="utf-8") as f:
     long_description=f.read()


REPo_NAME="Books-Recommender-System-Machine-Learning"
AUTHOR_USER_NAME="vikalp026var"
SRC_REPO="src"
LIST_OF_REQUIREMENTS=['streamlit','numpy']

setup(
     name=SRC_REPO,
     version="0.0.1",
     author=AUTHOR_USER_NAME,
     description="A small package for Movie Recommender System",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPo_NAME}",
     author_email="vikalp026varshney@gmail.com",
     packages=[SRC_REPO],
     license="MIT",
     python_requires=">=3.7",
     install_requires=LIST_OF_REQUIREMENTS,
)