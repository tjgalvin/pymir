# pymir

A simple class to help run miriad tasks.  

It makes no attempt to verify calling signatures of miriad tasks like other miriad packages (mirpy for instance). It also operates on the string invocation of miriad tasks. Operating this way does not clash with python keywords (`in` or `map` for example).

Some attempts are made to expose miriad options as attributes to the class. For instance you can access keywords of the calling miriad string by simply treating it as an attribute. Assuming a variable called `atlod` containing the result of a atlod miriad task, then `atlod.out` will return the value of the `out` keyword of the calling string.

It can be installed using pip following:
`pip3 install git+git://github.com/tjgalvin/pymir.git#egg=pymir`

## Usage

Assuming a variable called `uv` whose value is the path to a miriad visibility file, then that `uv`-file can be imaged with:

`invert = mirstr(f"invert vis={uv} options=mfs,sdb,double,mosaic offset=3:32:22.0,-27:48:37 stokes=i imsize=6,6,beam map={self.uv}.map beam={self.uv}.beam").run()`

The trailing `.run()` will execute the task. Using `print()` on the variable `invert` will print not only the invocation string, but also the output of `invert`. 

Attributes of the invocation string can be accessed either explicitly through the `attribute` method (`invert.attribute('map')`) or implicitly as an attribute itself (`invert.out`). 

There exists a small interface to expand an invocation string or attempt to overwrite some component. The `over` keyword can be used when creating a `mirstr` to replace key/value pairs to a invocation string, or add to it. For instance

```python
invert_kwargs = {"imsize":"3,3,beam", "stokes":"i"}
invert = mirstr(f"invert vis={uv} options=mfs,sdb,double,mosaic offset=3:32:22.0,-27:48:37 stokes=i imsize=6,6,beam map={uv}.map beam={uv}.beam", over=invert_kwargs).run()
```

will update the value of the `imsize` key to `3,3,beam` and add the `stokes` keyword. 