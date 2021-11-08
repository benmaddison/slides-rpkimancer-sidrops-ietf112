# rpkimancer - IETF112

Slides and example code for presentation of `rpkimancer` at IETF 112.

## RPKI Signed Poems

`rpkimancer-poem` in an implementation of a hypothetical example object
containing a poem signed by an ASN.

*Please do not use this for any other purpose!.*

To use:

``` bash
$ python3 -m venv .venv
$ . .venv/bin/activate
$ python3 -m pip install .
...
$ rpkincant conjure
...
$ rpkincant perceive target/**/*.rsp
{
  asID 65000,
  poem "
  A document RIPE-181
  Tells how everything ought to be done
  There are objects galore
  Heaven knows what they're for
  'Cos they're all out of date, every one.
  -- Nigel Titley (NT13)
  "
}
```
