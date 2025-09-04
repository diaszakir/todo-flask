# JWT Secret key generator
import secrets

jwt = str(secrets.SystemRandom().getrandbits(128))
print(jwt)