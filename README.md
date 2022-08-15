## Indian Profanity

This package help you to detect indian slang words, which will be helpful to identify words and censored them. This is initial version so our first language is marathi later on we will also add hindi and other indian languages as well.
Some of the functions which indian profanity provides

#### Install package
```bash
pip install indian_profanity
```

### Marathi
###### detectSlangMarathi
```
from indian_profanity.detect_marathi import detectSlangMarathi

simple_string = "ha nalayak ahe"
print(detectSlangMarathi(simple_string))

```
This will return boolean value if marathi slang word is present return either True or False

###### detectSlangMarathiWord
```
from indian_profanity.detect_marathi import detectSlangMarathiWord

simple_string = "ha nalayak ahe"
print(detectSlangMarathiWord(simple_string))

```
This will return list of slang word used in string 

###### censoredSlangMarathiWord
```
from indian_profanity.detect_marathi import censoredSlangMarathiWord

simple_string = "ha nalayak ahe"
print(censoredSlangMarathiWord(simple_string))

```
This will return string in censored way

