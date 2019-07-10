
# fumo_url = 'http://127.16.10.4:9081/fumo'  # 长城
fumo_url = 'http://127.0.0.1:9081/fumo'
# fumo_url = 'http://omatest.adups.com/fumo'

root_path = 'client_pkgs'

# client_username = 'IMEI:008600251148888'
client_username = 'WVWPR13C6AE170000'
client_password = 'a01483b953dd70b148d9b21943f6b120'
nonce_client_1 = b'server_nonce_default'  # pkg3的nonce
nonce_client_2 = b'nonce_456'  # pkg5的nonce

server_username = 'wuxl'
server_password = '123456'
server_nonce = b''  # pkg2的nonce,pkg4的nonce

session = '1'

protocol = 'xml'  # xml or wbxml


def to_string():
    return 'server_url={}\nclient={}:{}\nserver={}:{}\nroot_path={}\nsession={}\nprotocol={}'.format(
        fumo_url,
        client_username,
        client_password,
        server_username,
        server_password,
        root_path,
        session,
        protocol)
