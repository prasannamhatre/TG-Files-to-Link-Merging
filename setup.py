import setuptools

from tgfilestream import __version__

try:
    long_desc = open("README.md").read()
except IOError:
    long_desc = "Failed to read README.md"

setuptools.setup(
    name="tgfilestream",
    version=__version__,
    url="https://mau.dev/tulir/tgfilestream",

    author="Tulir Asokan",
    author_email="tulir@maunium.net",

    description="A Telegram bot that can stream Telegram files to users over HTTP.",
    long_description=long_desc,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),

    install_requires=[
        "aiohttp>=3",
        "telethon>=1.10",
        "yarl>=1",
    ],
    extras_require={
        "fast": ["cryptg>=0.2"],
    },
    python_requires="~=3.7",

    entry_points="""
        [console_scripts]
        tgfilestream=tgfilestream.__main__:main
    """,
)
