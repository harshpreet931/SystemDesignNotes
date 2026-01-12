# System Design Mastery Course

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"What separates your weekend project from Netflix or Uber? It's not just more servers or code, it's the blueprint. It's system design. : )"**

Welcome to the most comprehensive, hands on system design course that takes you from zero to hero!

## **Episodes**
- **Episode 1**: [System Design Fundamentals](./episodes/01-fundamentals/) ✓
- **Episode 2**: [Monolith vs Microservices](./episodes/02-monolith-microservices/) ✓
- **Episode 3**: [Functional vs Non-Functional Requirements](./episodes/03-functional-nonfunctional-requirements/) ✓
- **Episode 4**: [Horizontal vs Vertical Scaling](./episodes/04-horizontal-vertical-scaling/) ✓
- **Episode 5**: [Stateless vs Stateful Systems](./episodes/05-stateless-stateful-systems/) ✓
- **Episode 6**: [Load Balancing](./episodes/06-load-balancing/) ✓
- **Episode 7**: [Caching](./episodes/07-caching/) ✓
- So on...

## Episode 1: System Design Fundamentals

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/01-fundamentals/) | [View Presentation](./episodes/01-fundamentals/presentation/)**

### What You'll Learn:
- What is System Design and why it matters
- High-Level Design (HLD) vs Low-Level Design (LLD)
- Real example: Designing a URL Shortener
- Hands-on: Build your first system architecture

### Key Concepts Covered:
```
System Design = Software Architecture Blueprint
├── High-Level Design (HLD) - The Big Picture
│   ├── Major Components & Services
│   ├── Technology Stack Decisions
│   ├── Data Flow Architecture
│   └── Third-party Integrations
└── Low-Level Design (LLD) - The Details
    ├── Classes, Methods & Data Structures
    ├── Database Schemas & Relationships
    ├── Algorithms & Implementation Logic
    └── Error Handling & Edge Cases
```

## Episode 2: Monoliths vs Microservices

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/02-monolith-microservices/)**

### What You'll Learn:
- What monolithic architecture is and when to use it
- What microservices architecture is and its benefits
- Real-world examples: Netflix's evolution and Uber's architecture
- Practical decision framework for choosing between approaches

### Key Concepts Covered:
```
Architecture Patterns Comparison
├── Monolithic Architecture
│   ├── Single Codebase & Deployable Unit
│   ├── Shared Resources & Database
│   ├── Advantages: Simple, Fast, Easy to Debug
│   └── Challenges: Scalability, Technology Lock-in
└── Microservices Architecture
    ├── Independent Services & Databases
    ├── Distributed System Architecture
    ├── Advantages: Scalability, Flexibility, Fault Isolation
    └── Challenges: Complexity, Operational Overhead
```

## Episode 3: Functional vs Non-Functional Requirements

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/03-functional-nonfunctional-requirements/)**

### What You'll Learn:
- What requirements are and why they're critical to system design
- The difference between functional and non-functional requirements
- How to identify and document both requirement types
- Real-world example: Online bookstore requirements breakdown
- The requirements elicitation process

### Key Concepts Covered:
```
Requirements = Foundation of System Design
├── Functional Requirements (WHAT the system does)
│   ├── User Actions & Features
│   ├── System Operations & Business Logic
│   ├── Data Processing & Integrations
│   └── Example: User can create account, add to cart, checkout
└── Non-Functional Requirements (HOW WELL it performs)
    ├── Performance: Response time, load time
    ├── Scalability: Concurrent users, data growth
    ├── Availability: Uptime (99.9%, 99.99%)
    ├── Security: Encryption, authentication, compliance
    ├── Usability: User experience, accessibility
    ├── Maintainability: Code quality, integration time
    └── Portability: Cross-platform, deployment flexibility
```

## Episode 4: Horizontal vs Vertical Scaling

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/04-horizontal-vertical-scaling/)**

### What You'll Learn:
- What scalability means across three dimensions (load, data, compute)
- Vertical scaling: Making one machine more powerful
- Horizontal scaling: Distributed systems engineering
- Real-world examples: Netflix's evolution and AWS instances
- Decision matrix and practical frameworks for choosing the right approach
- Monitoring, metrics, and autoscaling strategies

### Key Concepts Covered:
```
Scaling Strategies Comparison
├── Vertical Scaling (Scale Up)
│   ├── Upgrade CPU, RAM, Storage on single machine
│   ├── AWS Example: r6i.large → r6i.24xlarge (48x power)
│   ├── Advantages: Simple, no code changes, ACID consistency
│   └── Challenges: Physical limits, single point of failure, cost
├── Horizontal Scaling (Scale Out)
│   ├── Add more servers, distribute load
│   ├── Requires: Stateless architecture, load balancers
│   ├── Advantages: Unlimited scale, fault tolerance, flexibility
│   └── Challenges: CAP theorem, network latency, complexity
└── Hybrid Approach (Best of Both)
    ├── Vertical for databases, horizontal for app servers
    ├── Netflix: 1000+ microservices, 300M+ users
    └── Autoscaling: Reactive, predictive, serverless
```

## Episode 5: Stateless vs Stateful Systems

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/05-stateless-stateful-systems/)**

### What You'll Learn:
- What "state" means in software systems (memory and session data)
- Stateless systems: Vending machine analogy and REST APIs
- Stateful systems: Bank teller analogy and session management
- Hybrid architecture: Stateless app tier + external state stores
- Real-world examples: Netflix, Amazon, and WhatsApp architectures
- Decision framework for choosing the right approach

### Key Concepts Covered:
```
State Management Strategies
├── Stateless Systems (Amnesia Design)
│   ├── No server memory between requests
│   ├── Every request includes full context (tokens, auth)
│   ├── Advantages: Perfect clones, easy scaling, fault tolerance
│   └── Challenges: Chattier requests, external state needed
├── Stateful Systems (Memory Design)
│   ├── Server remembers session context
│   ├── Requires: Sticky sessions, session storage
│   ├── Advantages: Efficient, fast (in-memory), simple client
│   └── Challenges: Sticky sessions, fragile, scaling hard
└── Hybrid Architecture (Modern Approach)
    ├── Stateless application servers
    ├── Centralized state in Redis/DynamoDB/Cassandra
    ├── Netflix: Stateless microservices + Cassandra
    ├── Amazon: Stateless servers + DynamoDB carts
    └── WhatsApp: Stateful connections for real-time (2B users)
```

## Episode 6: Load Balancing

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/06-load-balancing/)**

### What You'll Learn:
- What load balancing is and its critical role in distributed systems
- Primary objectives: Scalability and High Availability
- 9 load balancing algorithms and when to use each
- Health monitoring: L4 (TCP) vs L7 (HTTP) checks
- Session persistence strategies (IP Hash vs Cookie-Based)
- Real-world example: Netflix's multi-layer architecture
- Load balancer types: Hardware, Software, and Cloud
- L4 vs L7 load balancing and their trade-offs

### Key Concepts Covered:
```
Load Balancing Strategies
├── Primary Objectives
│   ├── Scalability: Horizontal scaling with commodity servers
│   └── High Availability: 99.99% uptime, health checks, failover
├── Load Balancing Algorithms (9 total)
│   ├── Round Robin: Simple, zero overhead, default
│   ├── Weighted Round Robin: Heterogeneous hardware capacity
│   ├── Least Connections: Dynamic, state-aware
│   ├── Weighted Least Connections: Best of both worlds
│   ├── Least Response Time: Latency + connections
│   ├── Resource-Based: CPU/memory monitoring with agents
│   ├── Geographic (GSLB): DNS-based, multi-region
│   ├── IP Hash: Sticky sessions (L4)
│   └── Cookie-Based: Sticky sessions (L7)
├── Session Persistence
│   ├── IP Hash: Simple but NAT/proxy issues
│   └── Cookie-Based: Robust L7 solution
├── Real-World Architecture
│   ├── Netflix: GSLB → AWS ELB → Zuul → Microservices
│   ├── 300M subscribers, 1000+ microservices
│   └── Path-based routing (/play, /browse)
├── Load Balancer Types
│   ├── Hardware: F5 BIG-IP, specialized silicon
│   ├── Software: HAProxy, NGINX (flexible, cheap)
│   └── Cloud: AWS ALB/NLB (managed, auto-scaling)
└── L4 vs L7 Load Balancing
    ├── L4: IP/port level, fast (<1ms), simple
    └── L7: Content-based routing, SSL termination, microservices
```

## Episode 7: Caching

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/07-caching/) | [View Presentation](./episodes/07-caching/presentation/)**

### What You'll Learn:
- What caching is and why it's fundamental to high-performance systems
- The benefits: reduced latency, increased throughput, lower costs
- Client-side vs. server-side caching strategies
- CDN caching for global content delivery
- Application-level caching with Redis and Memcached
- Database caching mechanisms
- Cache eviction policies: LRU, LFU, FIFO
- Cache invalidation strategies: TTL, Write-Through, Write-Behind
- The Thundering Herd problem and mitigation strategies
- Real-world case studies: Facebook, Netflix, and Amazon

### Key Concepts Covered:
```
Caching = Smart Memory for Faster Systems
├── Core Benefits
│   ├── 10-100x faster response times
│   ├── 50-90% reduction in database queries
│   └── Lower infrastructure costs
├── Caching Locations
│   ├── Client-Side: Browser cache, DNS cache, mobile storage
│   ├── CDN Caching: Edge locations globally
│   ├── Application Cache: Redis, Memcached, local memory
│   └── Database Cache: Buffer pool, query result cache
├── Eviction Policies (decide what to remove)
│   ├── LRU: Least Recently Used (most common)
│   ├── LFU: Least Frequently Used
│   └── FIFO: First In, First Out
├── Invalidation Strategies (keep data fresh)
│   ├── Write-Through: Write both cache and DB
│   ├── Write-Behind: Async writes to DB
│   ├── TTL: Time-based automatic expiration
│   └── Active: Explicit invalidation on updates
├── Design Patterns
│   ├── Cache-Aside: Application manages cache
│   ├── Read-Through: Cache loads itself on miss
│   └── Refresh-Ahead: Proactive refresh
└── Real-World Case Studies
    ├── Facebook: Multi-level caching with Memcached + Tao
    ├── Netflix: Cache everything, cache everywhere (EVCache)
    └── Amazon: DAX for microsecond DynamoDB reads
```

## Contributing

We love contributions! Here's how you can help make this course even better:

- [Report bugs or issues](./CONTRIBUTING.md)
- [Suggest new topics or improvements](./CONTRIBUTING.md)
- [Improve documentation](./CONTRIBUTING.md)
- [Create better diagrams](./CONTRIBUTING.md)
- [Add more examples](./CONTRIBUTING.md)

## Follow the Journey

- **YouTube**: [Subscribe for new episodes](http://youtube.com/@ThatNotesGuy)
- **LinkedIn**: [Connect with Harsh](https://www.linkedin.com/in/harshpreet931/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">Made with ❤️ by Harshpreet Singh</div>