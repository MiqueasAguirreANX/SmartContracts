const TestContract = artifacts.require('./TextContract.sol');
module.exports = function(deployer) {
    deployer.deploy(TestContract);
}