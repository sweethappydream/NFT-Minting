from brownie import network, SimpleCollectible
from scripts.helpful_scripts import (
    get_account,
    # get_contract,
    # get_breed,
    OPENSEA_URL,
)

sample_token_uri = "https://ipfs.io/ipfs/QmQBDgz7xUdF2poEYRPGskGBDV2gTmzFxg5DMRPMrJ33wD?filename=tamar_token_uri.json"


def deploy_and_create():
    account = get_account()
    from_account = {"from": account}
    simple_collectible = SimpleCollectible.deploy(from_account)
    tx = simple_collectible.createCollectible(sample_token_uri, from_account)
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")
    return simple_collectible

def main():
    deploy_and_create()