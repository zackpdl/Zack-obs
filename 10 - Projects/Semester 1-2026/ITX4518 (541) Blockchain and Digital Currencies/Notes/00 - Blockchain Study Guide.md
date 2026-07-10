# 🏛️ ITX4518 — Blockchain & Digital Currencies — Study Guide

> **Semester:** 1/2026 | **Credits:** 3 (3-0-6) | **Type:** General Elective  
> **Instructor:** Assoc. Prof. Dr. Charnsak Srisawatsakul  
> **Textbook:** Bashir, I. (2023). *Mastering Blockchain* (4th ed.). Packt.  
> **Pre-requisite:** None

---

## 📚 Materials Inventory

| # | File | Content |
|---|------|---------|
| 1 | `ITX4518_Course_Plan_Student.pdf` | Course outline, CLOs, weekly schedule, assessment breakdown |
| 2 | `ITX4518_Week01_Orientation_upload.pdf` | Course orientation, AI policy, grading, instructor bio |
| 3 | `ITX4518_Lesson01_What is Blockchain_upload.pdf` | Blockchain origins, definitions, 5 keywords, CAP theorem, double-spending |
| 4 | `ITX4518_Lesson02_Hashing_and_TamperEvidence.pdf` | Hash function properties, SHA-256, Merkle trees, tamper-evidence |
| 5 | `ITX4518_Lesson03_KEY_and_Digital_Signature.pdf` | Symmetric (AES) vs asymmetric (RSA) crypto, digital signatures, paper wallets |
| 6 | `ITX4518_Lesson04_Blockchain_Component_and_TYPE.pdf` | Decentralization, 12 blockchain components, 4 blockchain types, trade-off matrix |
| 7 | `ITX4518_Lesson05.1_What_is_Money.pdf` | Evolution of money (stone → crypto), forms with pros/cons, properties of money |
| 8 | `ITX4518_Lesson05.2_Value_of_Money.pdf` | Value of money (image-heavy deck, covers fungibility, scarcity) |

---

## 🧭 Course Overview

### Course Learning Outcomes (CLOs)

| CLO | Description |
|-----|-------------|
| **CLO 1** | Explain blockchain fundamentals, cryptographic foundations (hashing, keys, digital signatures) |
| **CLO 2** | Distinguish public/private/permissioned blockchains; explain Bitcoin, mining, PoW & PoS |
| **CLO 3** | Analyse how blockchain disrupts industries; assess ICOs, security incidents, real-world risks |
| **CLO 4** | Guided hands-on experience with Ethereum and Hyperledger Fabric |
| **CLO 5** | Collaborate in teams to propose/present a blockchain-based business solution |

### Assessment Breakdown

| Component | Weight | When |
|-----------|--------|------|
| In-class Participation & Activities | 10% | Throughout |
| Quizzes & Assignments | 10% | Throughout |
| Midterm Examination | 20% | Week 9 |
| Project 1 — Crypto Case-Study (Group) | 10% | Week 10 |
| Project 2 — Business Use-Case (Group) | 20% | Weeks 12–15 |
| Final Examination | 30% | Final exam period |

### Course Phases

```
FOUNDATIONS (Weeks 1–5)  →  CORE TECHNOLOGY (Weeks 6–9)  →  APPLICATIONS & PROJECT (Weeks 10–15)
```

---

## 📖 Lesson Summaries

---

### Lesson 1 — What is Blockchain & Why It Matters

#### The Problem
- **Double-spending problem:** digital files copy perfectly → the same coin could be sent to two people. Any digital cash system must prevent this.
- **Byzantine Generals Problem:** nodes may crash, lag, or lie. Honest nodes must still agree on one truth.
- **CAP Theorem:** distributed systems can pick only 2 of 3 — Consistency, Availability, Partition tolerance.

#### History
- **1976:** Diffie–Hellman keys
- **1979:** Merkle trees
- **1982:** Blind signatures (David Chaum)
- **1991:** Haber & Stornetta — linked timestamps (first "chain of hashes")
- **1992:** Proof-of-Work idea
- **1998:** Bit Gold (Nick Szabo)
- **2008:** Satoshi Nakamoto — *Bitcoin: A Peer-to-Peer Electronic Cash System*
- **2009:** Bitcoin launches

#### Blockchain Defined

> **Layman:** "An ever-growing, secure, shared record-keeping system where each user holds a copy of the records, which can only be updated if a majority agree."
>
> **Technical:** "A peer-to-peer, distributed ledger that is cryptographically secure, append-only, immutable, and updateable only via consensus among peers."

#### 5 Keywords

| Keyword | Meaning |
|---------|---------|
| **Peer-to-peer** | No central boss; nodes talk directly |
| **Distributed ledger** | Records copied to every participant |
| **Append-only** | Add new records but never edit/delete old ones |
| **Cryptographically secure** | Maths protects records, not passwords |
| **Updated by consensus** | Records added only when peers agree |

#### Block Anatomy
- **Block header:** previous-block hash, timestamp, nonce, Merkle root
- **Block body:** list of transactions
- **Genesis block:** first block (no previous hash)
- **Hash pointer:** each block stores the hash of the previous block → creates the chain

#### Benefits & Limitations
| Benefits | Limitations |
|----------|-------------|
| Decentralisation | Scalability (fewer TPS than cards) |
| High availability | Regulation challenges |
| Transparency | Privacy concerns |
| Cost & speed | Immaturity |
| Immutability | Interoperability issues |
| Smart contracts | Adoption still limited |

---

### Lesson 2 — Cryptography I: Hashing & Tamper-Evidence

#### Cryptography Basics
- **P**laintext → **E**ncryption → **C**iphertext → **D**ecryption → **K**ey
- **Confidentiality:** only authorised people can read data
- **Integrity:** only authorised people can change data (hashing delivers this)
- **Authentication & Non-repudiation:** prove identity and prevent denial

#### Hash Functions — 6 Key Properties

| # | Property | Meaning |
|---|----------|---------|
| 1 | **Deterministic** | Same input → same output, always |
| 2 | **Fixed-size output** | Any input length → fixed digest (SHA-256 = 256 bits / 64 hex chars) |
| 3 | **Fast to compute** | Hundreds of MB/s on modern hardware |
| 4 | **Avalanche effect** | One-bit change flips ~50% of output bits |
| 5 | **Preimage resistance** | Given `h(x)`, infeasible to find `x` (one-way) |
| 6 | **Collision resistance** | Infeasible to find two inputs with same digest |

#### Secure vs Broken Hashes
- **❌ Broken (never use):** MD5, SHA-1
- **✅ Secure:** SHA-256 (SHA-2 family), SHA-3 (Keccak)
- **Bitcoin uses SHA256d:** `SHA-256(SHA-256(x))` — double hash to prevent length-extension attacks

#### Tamper-Evidence via Chained Hashes
- Each block stores the hash of the previous block
- Edit any block → its hash changes → breaks all subsequent links
- **Merkle tree:** hash pairs of transactions up to a single Merkle root → compact verification

#### Password Security
- Never store plaintext passwords
- Store `hash(password + salt)` instead
- **Salt:** unique random value per user (stored openly)
- Use slow hashes: **bcrypt, scrypt, Argon2** (not raw SHA-256)

---

### Lesson 3 — Cryptography II: Keys & Digital Signatures

#### Symmetric Cryptography (AES)
- One shared key for encryption AND decryption
- **AES:** NIST standard block cipher (2001)
  - 128-bit blocks, 128/192/256-bit keys
  - 4 operations per round: SubBytes, ShiftRows, MixColumns, AddRoundKey
- **Problem:** how to securely share the key between two parties?

#### Asymmetric (Public-Key) Cryptography
- **Key pair:** private key (secret) + public key (shared)
- **RSA:** widely used asymmetric algorithm
- Solves the key distribution problem of symmetric crypto

#### Digital Signatures
| Concept | Meaning |
|---------|---------|
| **Sign** | Sender uses **private key** to sign a message hash |
| **Verify** | Anyone uses sender's **public key** to verify |
| **Non-repudiation** | Signer cannot deny signing |
| **Integrity** | Tampered message → verification fails (RED) |

#### Paper Wallets (bitaddress.org)
- **Public key / Address:** shareable (like an account number)
- **Private key:** secret (must never be shared — if lost, funds are unrecoverable)

> **Key insight:** In asymmetric crypto, the public key can be freely distributed. The private key must remain secret. Security lives in the key, not in hiding the algorithm.

---

### Lesson 4 — Blockchain Components & Types

#### Decentralization
| Concept | Definition |
|---------|------------|
| **Centralized** | One authority controls everything |
| **Distributed** | Infrastructure spread across machines, but control may still be centralised |
| **Decentralized** | Control and validation shared among independent participants |

> **Exam trap:** "Many servers" ≠ decentralised. Ask *who controls the rules*.

#### Spectrum of Decentralization
```
Centralized → Federated → Distributed → Decentralized → Autonomous
```

#### Methods of Decentralization
1. **Disintermediation** — remove middlemen entirely (e.g., P2P money transfer)
2. **Contest-driven** — multiple providers compete (e.g., oracles, validators)

#### Four-Question Framework (Narayanan et al.)
1. **What** is being decentralised?
2. What **level** of decentralisation is required?
3. What **blockchain** is used?
4. What **security mechanism** is used?

#### 12 Blockchain Components

| # | Component | Description |
|---|-----------|-------------|
| 1 | **Addresses** | Derived from public keys; identify sender/recipient |
| 2 | **Accounts** | Externally owned (private key) or contract (program logic) |
| 3 | **Transactions** | Signed instructions that change state (sender, recipient, value, fee, nonce, signature) |
| 4 | **Blocks** | Bundle transactions + header (prev hash, timestamp, nonce, Merkle root) |
| 5 | **Hashes** | One-way fingerprints for integrity and chain-linking |
| 6 | **Merkle Trees** | Hash tree → compact root; efficient proof of inclusion |
| 7 | **P2P Network** | Nodes broadcast transactions/blocks without central server |
| 8 | **Nodes** | Full node, validator/miner, light client, archive node |
| 9 | **Consensus** | Rules for agreeing on valid history |
| 10 | **Mining/Validation** | How block producers are chosen (PoW, PoS, BFT) |
| 11 | **State Machine & VM** | Formal model for state transitions (e.g., EVM) |
| 12 | **Smart Contracts** | Programs that hold assets, enforce rules, update state |

#### Blockchain Types — Comparison Matrix

| Type | Openness | Control | Speed / Privacy | Best For |
|------|----------|---------|-----------------|----------|
| **Public** (Bitcoin, Ethereum) | High | Low | Lower speed, low privacy | Neutral global settlement |
| **Private** (Hyperledger Fabric) | Low | High | High speed, high privacy | Internal enterprise workflows |
| **Consortium** (R3 Corda) | Medium | Shared | Medium-high | Multi-organisation coordination |
| **Hybrid** (Quorum) | Configurable | Mixed | Configurable | Public proof + private data |

#### Key Questions for Type Selection
- **Access:** Who can read/submit transactions?
- **Validation:** Who can create/confirm blocks?
- **Governance:** Who can upgrade rules?

> **Rule:** Choose the minimum decentralisation needed to solve the trust problem. If a normal database works, don't force blockchain.

#### Common Misconceptions
| ❌ Wrong | ✅ Better |
|----------|-----------|
| "Blockchain means decentralised" | Not always — private chains can be centralised |
| "Many servers = decentralised" | Distributed ≠ decentralised |
| "Hashes encrypt data" | Hashes fingerprint; encryption hides content |
| "Smart contracts are automatically safe" | They execute exactly as written, bugs included |
| "Public is always better" | Enterprises may need privacy and control |

---

### Lesson 5.1 — What is Money?

#### Evolution of Money Forms

| Form | Pros | Cons |
|------|------|------|
| **Stone money (Yap)** | Durable, hard to counterfeit | Extremely heavy (up to 8 tons) |
| **Metallic coins** | Durable, portable, divisible | Heavy in bulk, clipping risk |
| **Paper money** | Light, convenient, works for large amounts | Can inflate, depends on central trust |
| **Plastic cards** | Fast, digital records, fraud protection | Fees, debt risk, needs terminals |
| **Mobile money** | Instant transfers, QR codes, financial inclusion | Needs battery/network, scams |
| **Cryptocurrency** | Borderless, transparent, no single issuer | Volatility, regulatory uncertainty, key loss |

#### Key Properties of Money
- **Fungibility:** one unit is interchangeable with another
- **Scarcity:** supply is limited (not infinite)
- **Durability, Portability, Divisibility, Recognisability** (classic properties)

---

### Lesson 5.2 — Value of Money

- Image-heavy deck covering the concept of **value** in money
- Emphasises **fungibility** and **scarcity** as core properties
- References Alden (2023) *Broken Money* and Ammous (2018) *The Bitcoin Standard*

---

## 🧠 Key Vocabulary & Definitions

| Term | Definition |
|------|------------|
| **Blockchain** | A peer-to-peer distributed ledger that is cryptographically secure, append-only, immutable, and updateable only via consensus |
| **Hash function** | A one-way function that maps any input to a fixed-size digest; deterministic, avalanche-sensitive, collision-resistant |
| **SHA-256** | Secure Hash Algorithm (256-bit); Bitcoin's workhorse hash (used as SHA256d = double SHA-256) |
| **Merkle tree** | Binary hash tree that summarises many transactions into one root hash; enables efficient proof-of-inclusion |
| **Digital signature** | Cryptographic proof that a message was authorised by the holder of a private key |
| **Public key** | Shared credential derived from a private key; used to verify signatures |
| **Private key** | Secret credential that authorises transactions; if lost, funds are unrecoverable |
| **Consensus** | The mechanism by which nodes agree on a single version of the ledger |
| **Proof of Work (PoW)** | Security through costly computation; miners compete to find a hash below a target |
| **Proof of Stake (PoS)** | Security through economic stake; validators lock collateral that can be penalised |
| **BFT** | Byzantine Fault Tolerance — consensus among known validators via voting |
| **Double-spending** | Spending the same digital coin twice; blockchain solves this without a trusted middleman |
| **Byzantine Generals Problem** | Classic problem: how to reach agreement when some participants may be unreliable or malicious |
| **CAP Theorem** | Distributed systems can only achieve 2 of 3: Consistency, Availability, Partition tolerance |
| **Peer-to-peer (P2P)** | Direct exchange between participants without a central intermediary |
| **Distributed ledger** | A ledger replicated across multiple nodes; no single keeper of truth |
| **Append-only** | New records can be added but old records cannot be edited or deleted |
| **Immutability** | Property that once data is written, it cannot be changed |
| **Nonce** | A one-time number miners vary to produce a valid block hash |
| **Salt** | Random per-user value added to passwords before hashing to prevent rainbow table attacks |
| **AES** | Advanced Encryption Standard; symmetric block cipher (128-bit blocks) |
| **RSA** | Rivest–Shamir–Adleman; widely used asymmetric (public-key) cryptosystem |
| **Smart contract** | Self-executing code on a blockchain that holds assets and enforces rules |
| **Validator / Miner** | A node that proposes or confirms new blocks |
| **Full node** | A node that stores and independently verifies the entire chain |
| **Light client** | A node that verifies with less data, often using proofs |
| **DAO** | Decentralized Autonomous Organisation — rules encoded as smart contracts, minimal human intervention |
| **DeFi** | Decentralized Finance — financial services without traditional intermediaries |
| **NFT** | Non-Fungible Token — unique digital asset representing ownership |
| **Fungibility** | Property that one unit of money is interchangeable with another |
| **Double SHA-256 (SHA256d)** | SHA-256 applied twice; used by Bitcoin to prevent length-extension attacks |
| **Avalanche effect** | Small change in input → large, unpredictable change in hash output |
| **Collision resistance** | Computational infeasibility of finding two different inputs with the same hash |
| **Preimage resistance** | Given a hash, infeasible to find the original input (one-way property) |

---

## 📝 Exam-Prep Section

### Likely Exam Questions by Topic

#### Topic: Blockchain Fundamentals
1. Explain the **double-spending problem** and how blockchain solves it.
2. Define blockchain using the **technical definition**. Explain all 5 keywords.
3. Describe the **Byzantine Generals Problem** and its relevance to blockchain.
4. What is the **CAP theorem**? Why can't distributed systems achieve all three?
5. Compare the **layman's definition** vs the **technical definition** of blockchain.
6. How do **peer-to-peer networks** differ from client-server architecture?

#### Topic: Hashing & Tamper-Evidence
1. List and explain the **6 properties** of a cryptographic hash function.
2. What is the **avalanche effect**? Why is it important?
3. How does **chaining hashes** make a blockchain tamper-evident?
4. What is a **Merkle tree**? How does it enable efficient transaction verification?
5. Why does Bitcoin use **SHA256d** (double SHA-256) instead of single SHA-256?
6. Explain **password salting**. Why is it necessary?
7. Why are **MD5 and SHA-1** considered broken?
8. How does **Proof-of-Work mining** use hash functions (varying the nonce)?

#### Topic: Keys & Digital Signatures
1. Distinguish between **symmetric and asymmetric cryptography**.
2. How does a **digital signature** provide authentication, integrity, and non-repudiation?
3. Explain the relationship between a **private key, public key, and address**.
4. What is the key distribution problem in symmetric cryptography?
5. How does AES encrypt data? Describe its structure (SubBytes, ShiftRows, MixColumns, AddRoundKey).
6. What happens in the **sign → verify** process if a message is tampered with?

#### Topic: Blockchain Components & Types
1. List and describe **12 components** of a blockchain system.
2. Distinguish **public, private, consortium, and hybrid** blockchains. Give real examples.
3. What is the difference between **distributed and decentralised** systems?
4. Explain the **Four-Question Framework** for evaluating decentralisation.
5. Compare **Proof of Work vs Proof of Stake vs BFT** consensus.
6. What is a **smart contract**? What are the risks?
7. Describe the types of **nodes** in a blockchain network.
8. What is the **state machine** model in blockchain?

#### Topic: Money & Digital Cash
1. Trace the **evolution of money** from stone to cryptocurrency.
2. What are the **properties of good money**? (fungibility, scarcity, durability, portability, divisibility, recognisability)
3. Compare **6 forms of money** with their pros and cons.
4. What makes cryptocurrency different from traditional forms of money?
5. Explain David Chaum's **DigiCash** and why it didn't fully solve digital cash.
6. How does **Bitcoin** fulfill the requirements of digital cash (accountability + anonymity)?

#### Topic: Decentralization
1. Explain: **distributed ≠ decentralised**.
2. Describe the **decentralization spectrum** (centralised → federated → distributed → decentralised → autonomous).
3. What are the **two methods of decentralisation** (disintermediation and contest-driven)?
4. Compare **DO, DAO, DAC, and DAS** organisations.
5. When would you choose a consortium blockchain over a public one?
6. What is the "brutal engineering rule" about databases vs blockchain?

#### Open-Ended / Essay Questions
1. "Blockchain is just a slow database." Critically evaluate this claim.
2. Explain how blockchain achieves **trust without a trusted third party**.
3. Analyse a real-world blockchain use case. Which layers are actually decentralised? (Use the 6-layer framework: Data, Validation, Governance, Access, Execution, Interface)
4. Compare **Bitcoin and Ethereum** as public blockchains. How do their design goals differ?
5. Discuss the **trade-offs** between openness, control, speed, and privacy across blockchain types.
6. How does the combination of **hashing, digital signatures, and consensus** make blockchain secure?

### Quick-Reference: Comparison Tables

#### Consensus Mechanisms

| Mechanism | Selection Method | Security | Trade-off |
|-----------|-----------------|----------|-----------|
| Proof of Work | Computational work | Energy expenditure | High openness, lower throughput |
| Proof of Stake | Locked collateral | Economic penalty | Energy efficient, governance concerns |
| BFT / Permissioned | Known validator voting | Voting finality | Fast, but selected membership |

#### Decentralized Organization Types

| Feature | DO | DAO | DAC | DAS |
|---------|----|-----|-----|-----|
| Autonomy | Low | High | High | Very High |
| Human Input | Required | Minimal | Minimal | Minimal |
| Profit-oriented | Optional | Usually No | Yes | Varies |
| Governance | Human-led | Token-based | Share-based | Complex |
| Complexitiy | Low | Medium | Medium | Very High |
| Legal Status | Unsettled | Unsettled | Unsettled | Unsettled |

---

## 🔗 Quick-Reference: Key Hash Functions

| Hash | Output Size | Status | Used In |
|------|-------------|--------|---------|
| MD5 | 128 bits | ❌ Broken | Legacy only |
| SHA-1 | 160 bits | ❌ Broken | Legacy only |
| SHA-256 | 256 bits | ✅ Secure | Bitcoin (SHA256d) |
| SHA-3 (Keccak) | Variable | ✅ Secure | Ethereum |
| RIPEMD-160 | 160 bits | ✅ Used | Bitcoin addresses |

---

*Study guide generated from ITX4518 lecture materials (Semester 1/2026). For full details, consult the lecture PDFs and Bashir (2023) "Mastering Blockchain" (4th ed.).*
