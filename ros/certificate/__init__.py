from typing import Any, List
from ros._base import BaseModule, BaseProps

from .certificate import Certificate

class CertificateModule(BaseModule):
    _cert: BaseProps[Certificate] = None

    @property
    def certificate(self) -> BaseProps[Certificate]:
        if not self._cert:
            self._cert = BaseProps(self.ros, "/certificate", Certificate)
        return self._cert

    def __call__(self, **kwds: Any) -> List[Certificate]:
        return self.certificate(**kwds)
