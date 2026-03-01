# JS_PY-Fun: Cybersecurity Learning Journey

**JS_PY-Fun** is a comprehensive cybersecurity learning repository documenting my hands-on journey through network security and cryptography fundamentals using **Python** and **JavaScript**. This project transforms theoretical security concepts into practical implementations, featuring CLI tools, web interfaces, and security utilities that demonstrate core cybersecurity principles through code.

From classical cryptography to modern web security, from authentication systems to network reconnaissance, this repository showcases a progressive learning path focused on understanding security through implementation.

---

## Learning Journey Overview

This repository documents my hands-on exploration of cybersecurity fundamentals through practical implementations. The focus is on understanding security concepts by building them from scratch using Python and JavaScript.

### **Core Learning Areas**

**Authentication & Access Control** 
- Multi-user authentication system with brute force protection
- Account lockout mechanisms after 3 failed attempts
- Admin unlock functionality with comprehensive logging
- JSON-based persistent storage for locked users and failed attempts
- Timestamp-based security event tracking

**Cryptography & Encryption** 
- **Classical Ciphers**: Caesar, Rail Fence, Columnar Transposition, Substitution, Vernam
- **Modern Cryptography**: Diffie-Hellman key exchange implementation
- **Hash Functions**: SHA-256 CLI tool with file integrity verification
- Encryption/decryption with key management
- Understanding cryptographic foundations through implementation

**Password Security** 
- Cross-platform password validation (Python CLI + React web interface)
- Real-time strength analysis with visual feedback
- Regex-based pattern matching for security requirements
- Interactive web UI with modern design patterns

**Network Security** 
- Basic network reconnaissance and port scanning
- IP-based firewall rule implementation
- DoS attack detection and blocking (using Scapy)
- Socket programming for network communication

**Web Development & Security** 
- Express.js server with middleware architecture
- React-based security tools with modern UI/UX
- Cross-platform security logic implementation
- RESTful API patterns and routing

**System Security & Logging** 
- Comprehensive security event logging
- File and directory operations with OS modules
- JSON-based data persistence
- Error handling and exception management
- Unauthorized access detection and monitoring

---

## Key Implementations

### **Completed Projects**

**Password Security Suite**
- Python CLI validator with regex patterns and secure input (getpass)
- React web interface with real-time validation and visual strength meter
- Identical security logic across both platforms
- Requirements: 8+ characters, uppercase, lowercase, numbers, special characters

**Authentication System**
- Multi-user login with dictionary-based credential storage
- 3-attempt lockout mechanism with persistent tracking
- Admin unlock functionality for locked accounts
- Comprehensive logging: SUCCESS, FAILED, LOCKED, BLOCKED_ATTEMPT, ADMIN_UNLOCK
- JSON-based storage for failed attempts and locked users

**Cryptography Toolkit**
- **Caesar Cipher**: Classic shift cipher with encryption/decryption
- **Rail Fence Cipher**: Transposition cipher with zigzag pattern
- **Columnar Transposition**: Matrix-based transposition with padding
- **Substitution Cipher**: Monoalphabetic substitution implementation
- **Vernam Cipher**: One-time pad encryption
- **Diffie-Hellman**: Secure key exchange protocol demonstration
- **SHA-256 Tool**: CLI-based hash computation, verification, and file integrity checking

**Network Security Tools**
- **DoS Blocker**: Packet sniffing with Scapy, threshold-based blocking using iptables
- **Firewall**: IP-based rule matching and access control simulation
- **Network Scanner**: Basic port scanning and service detection using sockets

**Web Applications**
- **Express.js Server**: Basic middleware implementation and routing
- **React Password Checker**: Modern UI with gradient effects and real-time feedback
- **SHA-256 Web Tool**: HTML-based hash computation interface

**Security Logging & Monitoring**
- JSON-based structured logging with timestamps
- Event severity tracking (INFO, WARNING, ERROR)
- Unauthorized access detection framework
- File-based log persistence and analysis

### **Learning Lab Exercises**

**Week 1: Python Fundamentals**
- Functions, input/output, data structures
- Security-focused programming patterns
- Lists and dictionaries for user management

**Week 2: Advanced Python Concepts**
- Comprehensive authentication system with logging
- Exception handling and error management
- File I/O and JSON data persistence

**Week 3: System-Level Operations**
- OS module usage (getcwd, chdir, listdir, mkdir, remove, rename)
- File and directory management
- Safe file operations with existence checking

---

## Project Structure

```
├── NIS_PR/                                    # Network & Information Security Projects
│   ├── passwd_checker.py                        # CLI password validator with regex & getpass
│   ├── Caesar_cipher.py                         # Caesar cipher encryption/decryption
│   ├── Rail_fence.py                            # Rail fence transposition cipher
│   ├── Columnar_transposition.py                # Columnar transposition with padding
│   ├── Diffie-Hellman.py                        # Key exchange protocol implementation
│   ├── SHA256CLI.py                             # Hash computation & file integrity tool
│   ├── SHA256.html                              # Web-based SHA-256 hash tool
│   └── weak-password-checker/                   # React password strength analyzer
│       ├── src/App.jsx                          # Interactive UI with strength meter
│       ├── src/passwd_checker.js                # JavaScript validation logic
│       └── package.json                         # React + Vite dependencies
│
├── miscellaneous/                             # Cryptography & Security Tools
│   ├── Caesar_Cipher.py                         # Alternative Caesar implementation
│   ├── railFence_cipher.py                      # Rail fence cipher variant
│   ├── substitution_cipher.py                   # Monoalphabetic substitution
│   ├── vernam_cipher.py                         # One-time pad (Vernam cipher)
│   ├── DoS_blocker.py                           # Scapy-based DoS detection & blocking
│   ├── firewall.py                              # IP-based firewall rule engine
│   ├── pwd_Strength_Checker.py                  # Password strength analyzer
│   ├── worm_sim.py                              # Network reconnaissance simulation
│   └── cli.py                                   # HTTP server utilities
│
├── MEN/                                       # Express.js Web Server
│   ├── server.js                                # Express server with middleware
│   ├── package.json                             # Node.js dependencies
│   └── .env                                     # Environment configuration
│
├── unauthorized-access-detector/              # Access Monitoring Tools
│   ├── js_version/script.js                     # JavaScript access detection
│   └── py_version/                              # Python logging framework
│       ├── file.py                              # File access monitoring
│       └── logger_learn.py                      # JSON-based structured logging
│
├── Secure_System_lab/                         # Educational Security Exercises
│   ├── week1_pybasics/                          # Python fundamentals
│   │   ├── functions.py                         # Security-focused functions
│   │   ├── input_output.py                      # Secure input handling
│   │   └── lists_dicts.py                       # Data structure patterns
│   ├── week2_pybasics/                          # Advanced security concepts
│   │   ├── logger.py                            # Authentication with logging
│   │   ├── logs.txt                             # Security event logs
│   │   └── try_except.py                        # Exception handling
│   └── week3_pybasics/                          # System operations
│       └── os_modules.py                        # File/directory management
│
├── key.txt                                    # Cryptographic key storage
├── locked_users.json                          # User lockout tracking
└── logs.txt                                   # Security event logging
```

### **Implementation Status**

**Production-Ready:**
- Password validation (CLI + Web)
- Authentication system with lockout
- All cipher implementations
- SHA-256 hash tools
- Security logging framework

**Functional Prototypes:**
- DoS blocker (requires root/admin)
- Firewall rule engine
- Network scanner
- Express.js server

**Learning Exercises:**
- Week 1-3 Python labs
- Unauthorized access detector
- System operations practice

---

## Technologies & Skills

**Languages & Runtimes**
- Python 3.7+ (Core security tools, cryptography, CLI utilities)
- JavaScript ES6+ (Web interfaces, server-side logic)
- Node.js (Server applications, network tools)

**Frameworks & Libraries**
- React.js + Vite (Interactive security tools)
- Express.js (Web server, middleware)
- Scapy (Packet sniffing, network analysis)

**Security Concepts Implemented**
- Authentication & authorization
- Brute force protection
- Password strength validation
- Classical & modern cryptography
- Hash functions & integrity checking
- Network reconnaissance
- DoS detection & prevention
- Security logging & monitoring
- Input validation & sanitization

**Development Tools**
- Git (Version control)
- npm/Node.js (Package management)
- JSON (Data persistence)
- Regular expressions (Pattern matching)

---

## Getting Started

### Prerequisites
- Python 3.7+ for security tools and cipher implementations
- Node.js 16+ for JavaScript projects and React interfaces
- pip for Python package management
- npm or yarn for JavaScript packages

### Quick Start Guide

**Password Security Suite**
```bash
# Python CLI - Secure password validation with hidden input
cd NIS_PR
python passwd_checker.py

# React Web Interface - Real-time strength analysis
cd NIS_PR/weak-password-checker
npm install
npm run dev
# Visit http://localhost:5173
```

**Cryptography Tools**
```bash
# Classical ciphers
cd NIS_PR
python Caesar_cipher.py              # Caesar cipher
python Rail_fence.py                 # Rail fence transposition
python Columnar_transposition.py     # Columnar transposition
python Diffie-Hellman.py             # Key exchange protocol

# Hash functions
python SHA256CLI.py                  # CLI hash tool with file integrity

# Additional cipher implementations
cd ../miscellaneous
python substitution_cipher.py        # Substitution cipher
python vernam_cipher.py              # One-time pad
```

**Network Security Tools**
```bash
cd miscellaneous
python worm_sim.py                   # Network reconnaissance
python firewall.py                   # Firewall simulation
sudo python DoS_blocker.py           # DoS detection (requires root)
```

**Web Applications**
```bash
# Express.js server
cd MEN
npm install
node server.js
# Visit http://localhost:3000

# SHA-256 web tool
cd NIS_PR
# Open SHA256.html in browser
```

**Authentication System**
```bash
cd Secure_System_lab/week2_pybasics
python logger.py
# Test with: admin/1234 or tanishq/pass
# Try failed attempts to see lockout mechanism
```

**Security Logging Framework**
```bash
cd unauthorized-access-detector/py_version
python logger_learn.py
# Creates structured JSON logs with timestamps
```

---

## Learning Philosophy

> **"Security through implementation - building cryptographic concepts from scratch creates deeper understanding than using libraries alone."**

### My Approach to Learning Cybersecurity

**Hands-On First**
- Build it to understand it deeply
- Implement algorithms from scratch before using libraries
- Learn by doing, not just reading

**Cross-Platform Mastery**
- Implement the same security logic in Python and JavaScript
- Understand language-specific security considerations
- Build both CLI and web interfaces for the same functionality

**Security-First Thinking**
- Consider security implications in every design decision
- Understand attack vectors by implementing defenses
- Learn from failures and iterate

**Progressive Complexity**
- Start with fundamentals (authentication, basic ciphers)
- Build on solid foundations incrementally
- Add sophistication as understanding deepens

**Documentation Through Code**
- Write clean, readable implementations
- Code that teaches concepts to others
- Comments that explain the "why" not just the "what"

### What I've Learned So Far

**Technical Skills**
- Cryptographic algorithm implementation (classical & modern)
- Authentication system design with security controls
- Network programming with sockets
- Web security patterns and validation
- Cross-platform security logic
- Structured logging and monitoring
- Error handling and exception management

**Security Concepts**
- Defense in depth (multiple layers of security)
- Principle of least privilege
- Input validation and sanitization
- Secure password storage and validation
- Brute force protection mechanisms
- Network reconnaissance and defense
- Hash functions and integrity verification

**Development Practices**
- Test security features thoroughly
- Handle edge cases and errors gracefully
- Log security events comprehensively
- Use secure coding patterns (getpass, regex validation)
- Persist security data properly (JSON, file I/O)

---

## Real-World Applications

These implementations demonstrate practical security concepts used in production systems:

**Password Validation**
- Enterprise password policies
- User registration systems
- Security compliance requirements

**Authentication & Lockout**
- Brute force attack prevention
- Account security mechanisms
- Admin management tools

**Cryptography**
- Understanding encryption fundamentals
- Educational cryptography tools
- Historical cipher analysis

**Network Security**
- Basic intrusion detection
- Firewall rule implementation
- Network monitoring and analysis

**Security Logging**
- Audit trail creation
- Incident response data
- Compliance and forensics

---

## Who This Repository Is For

**Cybersecurity Students**
- Practical implementations of theoretical concepts
- Hands-on learning materials
- Code examples for security algorithms

**Self-Taught Developers**
- Structured learning path through security topics
- Progressive complexity in implementations
- Real projects to build and experiment with

**Security Enthusiasts**
- Understanding security through implementation
- Cross-platform security development
- Building security tools from scratch

**Career Changers**
- Portfolio demonstrating security programming skills
- Practical experience with security concepts
- Evidence of hands-on learning

**Fellow Learners**
- Inspiration for your own security projects
- Code to study and learn from
- Ideas for hands-on practice

---

## Future Learning Goals

**Short-Term**
- Advanced network scanning tools
- Web application security testing
- More modern cryptographic implementations
- Enhanced logging and monitoring systems

**Medium-Term**
- Penetration testing tools
- Vulnerability scanners
- Security automation scripts
- API security implementations

**Long-Term**
- Complete SOC (Security Operations Center) toolkit
- Threat detection and response systems
- Machine learning for anomaly detection
- Comprehensive security framework integration

---

## Contributing & Learning Together

This repository documents my personal cybersecurity learning journey, but learning is always better together!

**Ways to Engage**
- ⭐ Star this repository to follow my learning progress
- 🔀 Fork and experiment with your own implementations
- 💡 Suggest improvements or additional security features
- 🐛 Report bugs or security issues
- 📚 Share learning resources that have helped you
- 🤝 Connect if you're on a similar learning path

**Contribution Guidelines**
- Security-focused suggestions welcome
- Code reviews and optimization recommendations appreciated
- Additional cipher implementations or security tools
- Documentation improvements
- Educational resources and tutorials

**Important Notes**
- All tools are for **educational purposes only**
- Use responsibly and ethically
- Follow applicable laws and regulations
- Never use these tools on systems you don't own or have permission to test
- Some tools (like DoS_blocker.py) require root/admin privileges

---

## Learning Resources

**What Has Helped Me**
- Implementing algorithms from scratch
- Building the same functionality in multiple languages
- Reading security documentation and RFCs
- Experimenting with different approaches
- Learning from failures and debugging
- Engaging with cybersecurity communities

**Recommended Practice**
- Start with authentication and password security
- Implement classical ciphers to understand encryption
- Build CLI tools before web interfaces
- Add logging to understand program flow
- Test edge cases and error conditions
- Read and understand existing security code

---

## Project Highlights

**Most Valuable Learning Experiences**

1. **Authentication System** - Understanding brute force protection and lockout mechanisms
2. **Cross-Platform Password Validation** - Implementing identical logic in Python and JavaScript
3. **Diffie-Hellman Key Exchange** - Grasping public key cryptography fundamentals
4. **SHA-256 Implementation** - Understanding hash functions and integrity verification
5. **DoS Blocker** - Learning packet analysis and network security
6. **Security Logging** - Building comprehensive audit trails

**Code I'm Most Proud Of**
- Clean, readable cipher implementations
- Robust authentication with persistent storage
- Modern React UI with real-time validation
- Comprehensive error handling in logger.py
- Cross-platform security logic consistency

---

## Connect & Collaborate

I'm always interested in connecting with fellow learners and security enthusiasts!

**Let's Learn Together**
- Share your own security learning projects
- Discuss implementation approaches
- Exchange learning resources
- Collaborate on security tools
- Build a community of learners

**Feedback Welcome**
- Constructive code reviews
- Security best practices
- Performance optimizations
- Better implementation approaches
- Learning resource recommendations

---

## Acknowledgments

This learning journey has been shaped by:
- Open source security tools and documentation
- Cybersecurity communities and forums
- Educational resources and tutorials
- Trial, error, and persistence
- The principle that the best way to learn is by doing

---

**Ready to Start Your Own Security Learning Journey?**

Star ⭐ this repository to follow along with my progress and find inspiration for your own hands-on security projects!

**Happy Learning & Secure Coding!**  
*Learn. Implement. Secure. Share. Repeat.*

---

*Last Updated: March 2026*  
*Focus: Network Security & Cryptography with Python and JavaScript*  
*Status: Active Learning & Development*
