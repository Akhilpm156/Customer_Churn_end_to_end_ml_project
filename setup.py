import setuptools

REPO_NAME = "Customer_Churn_end_to_end_ml_project"
AUTHOR_USER_NAME = "Akhilpm156"
SRC_REPO = "Customer_Churn_Prediction"
AUTHOR_EMAIL = "akhilpm156@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version= "0.0.0",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Machine Learning Project",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )