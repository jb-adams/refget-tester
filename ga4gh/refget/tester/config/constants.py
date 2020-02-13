BASE_URL = "https://cl9lba3no5.execute-api.us-east-2.amazonaws.com/Prod"
REFGET_BASE_URL = BASE_URL + "/sequence"

SEQUENCE_REQUEST_TEMPLATE = REFGET_BASE_URL + "/{seqid}"
METADATA_REQUEST_TEMPLATE = SEQUENCE_REQUEST_TEMPLATE + "/metadata"
SERVICE_INFO_TEMPLATE = REFGET_BASE_URL + "/service-info"
ROUTE_NAMES = [
    "sequence",
    "metadata",
    "service-info"
]
TEMPLATES_DICT = {
    "sequence": SEQUENCE_REQUEST_TEMPLATE,
    "metadata": METADATA_REQUEST_TEMPLATE,
    "service-info": SERVICE_INFO_TEMPLATE
}
SEQIDS = [
    "2085c82d80500a91dd0b8aa9237b0e43f1c07809bd6e6785",
    "3332ed720ac7eaa9b3655c06f6b9e196",
    "959cb1883fc1ca9ae1394ceb475a356ead1ecceff5824ae7",
    "6681ac2f62509cfc220d78751b8dc524",
    "cfea89816a1a711055efbcdc32064df44feeb6b773990b07",
    "b7ebc601f9a7df2e1ec5863deeae88a3"
]
SEQLENGTHS = {
    "2085c82d80500a91dd0b8aa9237b0e43f1c07809bd6e6785": 5386,
    "3332ed720ac7eaa9b3655c06f6b9e196": 5386,
    "959cb1883fc1ca9ae1394ceb475a356ead1ecceff5824ae7": 230218,
    "6681ac2f62509cfc220d78751b8dc524": 230218,
    "cfea89816a1a711055efbcdc32064df44feeb6b773990b07": 270161,
    "b7ebc601f9a7df2e1ec5863deeae88a3": 270161
}

PARAM_TYPES = [
    None,
    "start-end",
    "range"
]