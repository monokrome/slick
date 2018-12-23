import typed_bencode

Request = typed_bencode.for_dict(cert=bytes, name=str, public_key=bytes)
File = typed_bencode.for_dict(url=str, size=int, type=str, name=str)
