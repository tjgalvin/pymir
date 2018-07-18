# pymir

A simple class to help run miriad tasks.

It makes no attempt to verify calling signatures of miriad tasks like other miriad packages (mirpy for instance). It also operates on the string invocation of miriad tasks. Operating this way does not clash with python keywords (`in` or `map` for example).

Some attempts are made to expose miriad options as attributes to the class. For instance you can access keywords of the calling miriad string by simply treating it as an attribute. Assuming a variable called `atlod` containing the result of a atlod miriad task, then `atlod.out` will return the value of the `out` keyword of the calling string.
