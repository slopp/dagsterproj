from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="dagsterproj",
        packages=find_packages(exclude=["dagsterproj_tests"]),
        install_requires=[
            "dagster",
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
