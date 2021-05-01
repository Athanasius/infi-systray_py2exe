from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'sample_systray.py'}],
    options={
        'py2exe': {
            'verbose': 4,
            'includes': [
                'pkg_resources',
            ],
        }
    },
)
