from attr import dataclass

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
