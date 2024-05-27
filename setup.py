import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="wechat_ob12",
    version="0.0.2.2",
    author="Dragon_ts",
    author_email="2658651085@qq.com",
    description="onebot12 to wechat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dragon-ts/wechat-ob12",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
