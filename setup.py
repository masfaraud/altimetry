from distutils.core import setup


def setup_config():
    config = {
        'name': 'srtm.py',
        'version': '0.1',
        'description': 'Lightweight Python parser for SRTM',
        'author': 'Tom de Ruijter',
        'author_email': 'deruijter.tom@gmail.com',
        'url': 'https://github.com/tomderuijter/srtm.py',
        'packages': ['srtm'],
        'classifiers': [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
        ],
        'requires': ['joblib'],
    }
    return config


if __name__ == "__main__":
    setup(**setup_config())
