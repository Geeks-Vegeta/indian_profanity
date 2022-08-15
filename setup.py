from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'indian_profanity',         # How you named your package folder (MyLib)
  packages = ['indian_profanity'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'To detect slang indian words',   # Give a short description about your library
  author = 'Shreyas Mohite',     
  long_description=long_description,
  author_email = 'shreyasmohite786@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Geeks-Vegeta',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Geeks-Vegeta/indian_profanity/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['indian_profanity', 'HINDI', 'MARATHI', "HINDI SLNG", "SLANG", "SWEAR wORD"],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)