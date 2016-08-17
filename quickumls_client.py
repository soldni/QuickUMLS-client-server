from MinimalServer import MinimalClient
from QuickUMLS.quickumls import QuickUMLS

def get_quick_umls_client(host='localhost', port=4645):
    client = MinimalClient(
        QuickUMLS, host=host, port=port,
        buffersize=4096, pickle_protocol=2)
    return client

