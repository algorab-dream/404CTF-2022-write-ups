## La Guerre des contrats (1/2)

### Description

L'objectif est de récupérer la clé publique de l'adresse ``_secretAddress`` définie dans le contrat donc le code est le suivant:
```s
pragma solidity 0.8.13;

contract publicKey {

    address private secretAddress;

    constructor(address _secretAddress){
        secretAddress = _secretAddress;
    }

    function isPublicKey(bytes memory mystery) external view returns(bool){
        require(address(uint160(uint256(keccak256(mystery)))) == secretAddress, "Essayez encore !");
        return true;
    }
}
```
Il faut donc dans un premier temps récupérer l'adresse ``_secretAddress``, puis calculer sa clé publique. Evidemment, impossible de le faire directement, cela reviendrait à trouver la réciproque d'une fonction de hashage.

### Solution

#### Récupération de l'adresse

Dans un contrat, une variable peut être privée, il n'en reste pas moins que sa valeur est stockée avec le contrat. Il est donc possible de [lire les variables privées dans un contrat.](https://blog.finxter.com/private-exploit-smart-contract-security-series-part-2/)
L'adresse étant déclarée en premier dans le contrat, on pourra la lire au niveau du premier bloc dans le contrat.
On peut donc la récupérer :
```javascript 
>> web3.eth.getStorageAt('0xd22213f7B4E5997C9B542105cce6ed4dfEAE5F91', 0, console.log); 
0x0000000000000000000000009acadffa3d622b6f77b2dd625ad41e054eec300e
```

On a donc ``_secretaddress = '0x9acadffa3d622b6f77b2dd625ad41e054eec300e'``. Néanmoins, pour la retrouver, il faut penser à la checksum avant ! Notre adress vaut donc finalement ``'0x9AcADFfA3d622B6F77b2Dd625ad41E054eEc300E'``.

#### Récupération de la clé publique

Afin de récupérer la clé publique, il faut que l'entité à l'adresse trouvée ait effectué des transactions. En effet, les transactions sont signées à l'aide de la clé privée, à partir de laquelle on peut retrouver la clé publique. Ainsi, à partir des informations de la transaction, notamment sa signature, il est possible de retrouver la clé publique.
En prenant la dernière transaction de l'adresse cible, on récupère les informations de la transaction par la commande suivante :
```javascript
web3.eth.getTransaction('0x6799103870e88fc59a9dc5f400dfd2fb5fed82b58fbffb09a99808003ee2634d', console.log) 
```
Puis on ressort la clé privée avec un script :
```python
from eth_account._utils.signing import to_standard_v
from eth_account._utils.legacy_transactions import serializable_unsigned_transaction_from_dict
from eth_keys.datatypes import Signature

def getPubKey():

    vrs = (to_standard_v(0x1c), int("e58712e11aaa32ac207e893cde3b91159c1e1dc5be5a9bd18f0476869806feb6", 16), int("421eef8f63fc2872c86d79048ac053542980768f4b7638da40353c0a95012473", 16))
    signature = Signature(vrs=vrs)    
    tx_dict = {'nonce': 3,
               'gasPrice': 50000000000,
               'gas': 2000000,
               'to': "0xafb1E5c639950c547473De7DC5aFb8D8cEa0658C",
               'value': 1000000000000000
    }
    serialized_tx = serializable_unsigned_transaction_from_dict(tx_dict)
    pubKey = signature.recover_public_key_from_msg_hash(serialized_tx.hash())
    return(pubKey)

print(getPubKey())
```
On récupère alors la bonne clé publique, qui nous donne le flag : 404CTF{0xb227feb5ecb369faf668f711f2331d163244fddb5e297be94fe30046b261732fda92d1afe5578f1d88c29ae439a7220ecc984701411742b5fec2b1639433100d}.