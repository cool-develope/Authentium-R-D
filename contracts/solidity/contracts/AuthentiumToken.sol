// contracts/GLDToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract AuthentiumToken is ERC20 {

    AggregatorV3Interface internal priceFeed;
    uint256 public poolBalance;
    address admin;

    /**
     * Network: Kovan
     * Aggregator: ETH/USD
     * Address: 0x9326BFA02ADD2366b30bacB125260Af641031331
     */
    constructor(uint256 initialSupply) ERC20("AuthentiumToken", "AUT") {
        _mint(msg.sender, initialSupply);
        priceFeed = AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331);
        admin = _msgSender();
    }

    /**
     * @dev Returns the number of decimals used to get its user representation.
     * For example, if `decimals` equals `2`, a balance of `505` tokens should
     * be displayed to a user as `5.05` (`505 / 10 ** 2`).
     */
    function decimals() public pure override returns (uint8) {
        return 5;
    }

    /**
     * Returns the latest price
     */
    function getThePrice() public view returns (int) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return price;
    }

    /**
     * Deposit the ether and get tokens
     */
    function deposit() public payable {
        int256 price = getThePrice();

        require(price > 0, "The price is not negative");
        uint256 amount = msg.value / (uint(price / 1000));

        _burn(admin, amount);
        poolBalance += msg.value;
        _mint(_msgSender(), amount);

        emit Deposit(_msgSender(), msg.value);
    }

    /**
     * Deposit the ether and get tokens
     */
    function withdraw() public {
        uint256 amount = balanceOf(_msgSender());
        uint256 ethers = amount * (poolBalance / totalSupply());

        _burn(_msgSender(), amount);

        (bool sent, ) = payable(_msgSender()).call{value: ethers}("");
        require(sent, "Failed to send Ether");
        poolBalance -= ethers;
        
        _mint(admin, amount);

        emit Withdraw(_msgSender(), ethers);
    }

    /**
     * @dev Emitted when deposit ether to the pool
     *
     * Note that `value` may be zero.
     */
    event Deposit(address indexed from, uint256 value);

    /**
     * @dev Emitted when withdraw ether from the pool
     *
     * Note that `value` may be zero.
     */
    event Withdraw(address indexed to, uint256 value);
}