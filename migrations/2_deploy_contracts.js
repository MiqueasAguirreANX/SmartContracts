const TestContract = artifacts.require('TestContract');

module.exports = async function(deployer, networks, accounts) {
    await deployer.deploy(TestContract);
}