const AuthentiumToken = artifacts.require("AuthentiumToken");

module.exports = function (deployer) {
  deployer.deploy(AuthentiumToken, 10**14);
};
