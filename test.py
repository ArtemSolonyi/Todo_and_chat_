import re

import bcrypt
password = b'MYKA2MYKA2'
hashed = "b'$2b$12$A1pMoY9M/7JCc/DZuyKFceCR6CV5P.CyPix.1craM4FwxTAl9vlvS'"
hash = re.findall(r"[^']",hashed)[1:]
hashed = "".join(hash).encode("utf-8")


if bcrypt.checkpw(password, hashed):
    print("norm")
else:
    print("ne norm")