try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(
    name='frontoxy',
    packages=find_packages(),
    install_requires=['pika', 'scrapy'],
    version='1.0.3',
    description='Distributed URLs frontier for Scrapy with RabbitMQ',
    author='Fabien Vauchelles',
    author_email='fabien@vauchelles.com',
    url='https://github.com/fabienvauchelles/frontoxy',
    download_url='https://github.com/fabienvauchelles/frontoxy/tarball/1.0.3',
    keywords=['crawler', 'crawling', 'scrapoxy', 'scrapy', 'scraper', 'scraping', 'frontier'],
    classifiers=[],
)
