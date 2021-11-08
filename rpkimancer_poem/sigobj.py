"""RPKI Poem implementation."""

from __future__ import annotations

import logging
import typing

from rpkimancer.asn1.mod import RPKI_Poem_2021
from rpkimancer.resources import AFI, AsResourcesInfo
from rpkimancer.sigobj.base import EncapsulatedContent, SignedObject

log = logging.getLogger(__name__)


class PoemEContent(EncapsulatedContent):
    """encapContentInfo for RPKI Poem Objects."""

    content_type = RPKI_Poem_2021.id_ct_Poem
    content_syntax = RPKI_Poem_2021.Poem
    file_ext = "rsp"
    ip_resources = None

    def __init__(self, *,
                 version: int = 0,
                 as_id: int,
                 poem: str) -> None:
        """Initialise the encapContentInfo."""
        data = {"version": version,
                "asID": as_id,
                "poem": poem}
        super().__init__(data)
        self._as_resources = [as_id]

    @property
    def as_resources(self) -> typing.Optional[AsResourcesInfo]:
        """Get the AS Number Resources covered by this Poem."""
        return self._as_resources


class Poem(SignedObject, econtent_type=RPKI_Poem_2021.ct_Poem):
    """CMS ASN.1 ContentInfo for RPKI Poem Objects."""

    econtent_cls = PoemEContent
