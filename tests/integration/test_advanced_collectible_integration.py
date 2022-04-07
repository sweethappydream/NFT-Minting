from brownie import network, AdvancedCollectible
import pytest, time
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Acting step
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(80)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
