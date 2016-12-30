from numpy.distutils.core import setup

setup(
    name = "followR",
    version = "1.0",
    author = "Raphael Dussin",
    author_email = "raphael.dussin@gmail.com",
    description = ("follow and report tasks " ),
    license = "GPLv3",
    keywords = "task monitoring",
    url = "",
    packages=['followR'],
    scripts = ['followR/follow']
)

