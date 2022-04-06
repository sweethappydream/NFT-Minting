// SPDX-License-Identifier: MIT

// An NFT contract where the tokenURI can be one of 3
// different dogs randomly selected
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {}
