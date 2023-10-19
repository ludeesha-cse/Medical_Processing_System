import hashlib
import base64

#hashing the user entered password
def HashingPassword(UserPW):
    HashedPW = hashlib.md5() #hashing user entered password using md5 library
    HashedPW.update(UserPW.encode("utf-8"))
    return HashedPW.hexdigest()

#encoding user entered data
def Encode(EncodeText):
    EncodedMessage = base64.b64encode(EncodeText.encode('ascii')) # encoding user entered data using base64 library for transmitting purposes
    DecodedMessage = EncodedMessage.decode('ascii') # decoding the encoded data after trasmitting
    return DecodedMessage

#decoding encoded message
def Decode(DecodeText):
    DecodedBase64 = base64.b64decode(DecodeText.encode('ascii'))
    DecodedMessage = DecodedBase64.decode('ascii')
    return DecodedMessage
