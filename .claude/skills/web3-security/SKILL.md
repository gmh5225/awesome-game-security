---
name: web3-security
description: Guide for Web3 and blockchain security research including smart contract auditing, DeFi vulnerabilities, and blockchain gaming security. Use this skill when working with Solidity, smart contract analysis, or blockchain-based game security.
---

# Web3 & Blockchain Security

## Overview

This skill covers Web3 security resources from the awesome-game-security collection, focusing on smart contract security, DeFi vulnerabilities, and blockchain gaming.

## Smart Contract Security

### Common Vulnerabilities
```
- Reentrancy attacks
- Integer overflow/underflow
- Access control flaws
- Front-running
- Flash loan attacks
- Oracle manipulation
- Timestamp dependence
- Unchecked external calls
```

### Reentrancy Example
```solidity
// Vulnerable
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount);
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
    balances[msg.sender] -= amount;  // State change after external call
}

// Fixed
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;  // State change before external call
    (bool success, ) = msg.sender.call{value: amount}("");
    require(success);
}
```

## Analysis Tools

### Static Analyzers
- **Slither**: Trail of Bits' static analyzer
- **Mythril**: ConsenSys security tool
- **4naly3er**: Automated code analysis
- **Semgrep**: Pattern-based scanning

### Dynamic Analysis
- **Echidna**: Property-based fuzzer
- **Manticore**: Symbolic execution
- **Foundry**: Testing framework with fuzzing
- **Ityfuzz**: EVM fuzzer

### Decompilers
- **ABI Decompiler**: Recover contract ABI
- **EthIR**: Bytecode analysis framework
- **Heimdall-rs**: Bytecode analysis in Rust

## Security Frameworks

### OpenZeppelin
```
- Audited contract libraries
- Access control patterns
- Upgradeable contracts
- Security best practices
```

### Development Tools
- **Foundry**: Modern Solidity toolkit
- **Hardhat**: Development environment
- **Truffle**: Testing framework
- **Brownie**: Python-based framework

## DeFi Security

### Attack Vectors
```
- Flash loan attacks
- Price oracle manipulation
- Liquidity pool attacks
- Governance attacks
- MEV extraction
```

### Protection Mechanisms
```
- Time locks
- Multi-sig requirements
- Oracle diversification
- Rate limiting
- Circuit breakers
```

## Blockchain Gaming Security

### On-Chain Game Issues
```
- Randomness manipulation
- Front-running player actions
- Economic exploits
- NFT vulnerabilities
- Token inflation
```

### Off-Chain Components
```
- API security
- Database integrity
- Asset verification
- Player identity
```

## Audit Process

### Pre-Audit Checklist
```
1. Complete code documentation
2. Test coverage report
3. Deployment configuration
4. Previous audit findings
5. Scope definition
```

### Audit Methodology
```
1. Automated analysis (Slither, Mythril)
2. Manual code review
3. Business logic verification
4. Access control analysis
5. Economic model review
6. Integration testing
```

### Post-Audit
```
1. Findings report
2. Severity classification
3. Remediation verification
4. Ongoing monitoring
```

## Learning Resources

### Practice Platforms
- **Damn Vulnerable DeFi**: CTF challenges
- **Ethernaut**: OpenZeppelin's wargame
- **DeFiHackLabs**: Reproduce real hacks
- **DeFiVulnLabs**: Learn vulnerabilities

### Research
- **Rekt News**: Hack postmortems
- **Trail of Bits Blog**: Security research
- **Consensys Blog**: Best practices
- **SlowMist**: Security reports

## Security Standards

### EIP Standards
- EIP-20: Token standard
- EIP-721: NFT standard
- EIP-1155: Multi-token standard
- EIP-2535: Diamond standard

### Audit Standards
- Smart Contract Security Verification Standard (SCSVS)
- Wallet Security Verification Standard

## MEV (Miner Extractable Value)

### Concepts
```
- Transaction ordering
- Sandwich attacks
- Arbitrage extraction
- Liquidation frontrunning
```

### Protection
- Flashbots RPC
- Private transactions
- Commit-reveal schemes
- Time-weighted pricing

## Solana Security

### Unique Considerations
```
- Account model vs UTXO
- Program-derived addresses
- Cross-program invocation
- Rent mechanism
```

### Tools
- Anchor framework
- Trident fuzzer
- Solana-specific analyzers

## Move Language Security

### Platforms
- Aptos
- Sui
- Movement

### Security Features
```
- Resource-oriented programming
- Linear types
- Built-in formal verification
- Ability-based access control
```

## Report Writing

### Severity Levels
```
Critical: Direct fund loss possible
High: Significant impact, complex exploit
Medium: Limited impact or difficult exploit
Low: Best practice violations
Informational: Gas optimizations, style
```

### Finding Format
```markdown
## [Severity] Finding Title

**Description**: What the issue is
**Impact**: Potential consequences  
**Location**: File and line numbers
**Recommendation**: How to fix
**Status**: Fixed/Acknowledged/Disputed
```
