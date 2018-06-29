import pytest
import os

from en16931.entity import Entity
from en16931.invoice import Invoice
from en16931.invoice_line import InvoiceLine
from en16931.tax import Tax

@pytest.fixture()
def xml_path():
    path, name = os.path.split(os.path.abspath(__file__))
    return os.path.join(path, "files", "invoice.xml")

@pytest.fixture()
def invoice1():
    invoice = Invoice()
    seller = Entity(name="Acme Inc.", tax_scheme="VAT",
                    tax_scheme_id="ES34626691F", country="ES",
                    party_legal_entity_id="ES34626691F",
                    registration_name="Acme INc.", mail="acme@acme.io",
                    endpoint="ES76281415Y", endpoint_scheme="ES:VAT",
                    address="easy street", postalzone="08080",
                    city="Barcelona")
    buyer = Entity(name="Corp Inc.", tax_scheme="VAT",
                   tax_scheme_id="ES76281415Y", country="ES",
                   party_legal_entity_id="ES76281415Y",
                   registration_name="Corp INc.", mail="corp@corp.io",
                   endpoint="ES76281415Y", endpoint_scheme="ES:VAT",
                   address="busy street", postalzone="08080",
                   city="Barcelona")
    invoice.buyer_party = buyer
    invoice.seller_party = seller
    invoice.due_date = "2018-09-11"
    invoice.issue_date = "2018-06-11"
    # lines
    il1 = InvoiceLine(quantity=11, unit_code="EA", price=2,
                      item_name='test 1', currency="EUR",
                      tax_percent=0.21, tax_category="S")
    il2 = InvoiceLine(quantity=2, unit_code="EA", price=25,
                      item_name='test 2', currency="EUR",
                      tax_percent=0.21, tax_category="S")
    il3 = InvoiceLine(quantity=5, unit_code="EA", price=3,
                      item_name='test 3', currency="EUR",
                      tax_percent=0.1, tax_category="AA")
    invoice.add_lines_from([il1, il2, il3])
    return invoice


@pytest.fixture()
def tax1():
    return Tax(0.21, "S", None)


@pytest.fixture()
def tax2():
    return Tax(0.1, "AA", None)
