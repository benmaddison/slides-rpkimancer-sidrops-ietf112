"""rpkincant conjure plugins for RPKI Poem objects."""

from __future__ import annotations

import logging
import typing

from rpkimancer.cli import Args
from rpkimancer.cli.conjure import (ConjurePlugin,
                                    DEFAULT_CA_AS_RESOURCES,
                                    META_AS,
                                    PluginReturn)

if typing.TYPE_CHECKING:
    from rpkimancer.cert import CertificateAuthority

log = logging.getLogger(__name__)

META_POEM = "<poem>"

RIPE181 = """
A document RIPE-181
Tells how everything ought to be done
There are objects galore
Heaven knows what they're for
'Cos they're all out of date, every one.

-- Nigel Titley (NT13)
"""


class ConjurePoem(ConjurePlugin):
    """rpkincant conjure plugin for RPKI Poem Objects."""

    def init_parser(self) -> None:
        """Set up command line argument parser."""
        self.parser.add_argument("--poem-as-id",
                                 type=int,
                                 default=DEFAULT_CA_AS_RESOURCES[0],
                                 metavar=META_AS,
                                 help="Poem AS "
                                      "(default: %(default)s)")
        self.parser.add_argument("--poem",
                                 type=str,
                                 default=RIPE181,
                                 metavar=META_POEM,
                                 help="Poem text "
                                      "(default: %(default)s)")

    def run(self,
            parsed_args: Args,
            ca: CertificateAuthority,
            *args: typing.Any,
            **kwargs: typing.Any) -> PluginReturn:
        """Run with the given arguments."""
        # create Poem object
        from .sigobj import Poem
        log.info("creating Poem object")
        Poem(issuer=ca, as_id=parsed_args.poem_as_id, poem=parsed_args.poem)
        return None
