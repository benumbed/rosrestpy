from attr import dataclass

example = {
    ".id": "*2",
    "akid": "",
    "common-name": "sw-8gp-2xge-157n.adm.nexus",
    "country": "US",
    "crl": "false",
    "days-valid": "365",
    "fingerprint": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "invalid-after": "1970-01-01 00:00:00",
    "invalid-before": "1970-01-01 00:00:00",
    "key-size": "secp384r1",
    "key-type": "ec",
    "key-usage": "digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign,tls-server,tls-client",
    "locality": "Mercer Island",
    "name": "TEMPLATE sw-8gp-2xge-157n.adm.nexus",
    "organization": "nexus Heavy Industries",
    "private-key": "false",
    "skid": "",
    "state": "Washington",
    "subject-alt-name": "DNS:sw-8gp-2xge-157n.adm.nexus,DNS:cluster-sw-1.adm.nexus,IP:192.168.128.13",
    "unit": "Core"
  },
ex = {
    ".id": "*3",
    "akid": "4ab0ecfe3289d6b586324e83a12d1368b553f11e",
    "common-name": "sw-8gp-2xge-157n.adm.nexus",
    "country": "US",
    "crl": "true",
    "days-valid": "365",
    "digest-algorithm": "sha384",
    "expires-after": "43w4d16h1m33s",
    "fingerprint": "2561da20748b615e956edaaff41edc7116902bec89c6611c21e7d6343039cfa6",
    "invalid-after": "2024-12-26 00:27:17",
    "invalid-before": "2023-12-27 00:26:47",
    "issuer": "C=US,S=Washington,L=Mercer Island,O=nexus Heavy Industries,OU=Security,CN=nexus Heavy Industries Intermediate CA",
    "key-size": "secp384r1",
    "key-type": "ec",
    "key-usage": "digital-signature,key-encipherment,tls-server,tls-client",
    "locality": "Mercer Island",
    "name": "sw-8gp-2xge-157n.adm.nexus",
    "organization": "haven Biotic Ventures, LLC",
    "private-key": "true",
    "serial-number": "551462745afafb8ab35d26ac616cc439d096a437",
    "skid": "9cb484f87cf436129b32d922881e87f62a2514f2",
    "state": "Washington",
    "subject-alt-name": "DNS:cluster-sw-1.adm.nexus,DNS:sw-8gp-2xge-157n.adm.nexus,IP:192.168.128.13",
    "trusted": "true"
  },

@dataclass
class Certificate:
    id: str
    common_name: str
    crl: bool
    days_valid: int
    fingerprint: str
    invalid_after: str
    invalid_before: str
    key_size: str
    key_type: str
    key_usage: str
    name: str
    organization: str
    subject_alt_name: str
    akid: str = None
    country: str = None
    locality: str = None
    private_key: bool = False
    skid: str = None
    state: str = None
    unit: str = None

    def __str__(self) -> str:
        return self.name
