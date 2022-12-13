import hashlib

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


class HashTchai:
    @staticmethod
    def calculate_hash(sender, receiver, time_transaction, money, last_hash, is_first_iteration=False):
        # Formalise datas
        money = format(float(money), ".6f")

        # hash
        """Le salage est une méthode permettant de renforcer la sécurité des informations qui sont destinées à être 
        hachées (par exemple des mots de passe) en y ajoutant une donnée supplémentaire afin d’empêcher que deux 
        informations identiques ne conduisent à la même empreinte """

        salt = "niss22_11_99_rine"
        salt="niss"

        # For first iteration
        if is_first_iteration:
            last_hash = "niss_99_rine"
            last_hash = "nss"

        """
        SHA-512 est un algorithme de hachage utilisé en cryptographie, basé sur SHA-2 avec la variante à 512 bits. 
        Il a un principe identique au SHA-256, sauf qu'il calcule une empreinte numérique de 512 bits - 128 
        caractères hexadécimaux. 
        La seule méthode possible est de supposer que le contenu hashé est un mot de passe, 
        de récupérer une base de données de mots de passe et de comparer leur hash avec celui recherché. Cette 
        méthode ne peut pas couvrir tous les mots de passes possibles et ne fonctionne pas souvent, pourtant c'est la 
        meilleure méthode à ce jour. 
        """

        transaction_hash = hashlib.sha512(f"{sender}{receiver}{salt}{time_transaction}{money}{last_hash}".encode())
        transaction_hash = transaction_hash.digest().hex()
        # print("[utils/calculate_hash] transaction_hash: '{}'".format(transaction_hash))


        # Debug
        print("----------------")
        print("sender: '{}'".format(sender))
        print("receiver: '{}'".format(receiver))
        print("salt: '{}'".format(salt))
        print("time_transaction: '{}'".format(time_transaction))
        print("money: '{}'".format(money))
        print("last_hash: '{}'".format(last_hash))
        print("----------------")

        return transaction_hash

    @staticmethod
    def generate_rsa():
        key = RSA.generate(2048)
        private_key = key.export_key('PEM')
        public_key = key.publickey().export_key('PEM')
        print(private_key)
        print(public_key)
        return public_key, private_key

    @staticmethod
    def calculate_signature(sender, receiver, money, time_transaction, private_key):
        message_string = f'{sender}{receiver}{money}{time_transaction}'
        message_bytes = bytes(message_string, 'UTF-8')

        key = RSA.import_key(private_key)

        h = SHA256.new(message_bytes)
        signature = pkcs1_15.new(key).sign(h)

        return signature.hex()

    @staticmethod
    def verify_signature_with_public_key(sender, receiver, money, time_transaction, signature, public_key):
        message_string = f'{sender}{receiver}{money}{time_transaction}'
        message_bytes = bytes(message_string, 'UTF-8')

        key = RSA.import_key(public_key)
        h = SHA256.new(message_bytes)
        try:
            pkcs1_15.new(key).verify(h, signature)
            print("The signature is valid.")
            return True
        except (ValueError, TypeError):
            print("The signature is not valid.")
            return False


