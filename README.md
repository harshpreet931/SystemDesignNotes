# System Design Course

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
- **Episode 8**: [CDNs Explained](./episodes/08-cdns/) ✓
- **Episode 9**: [Databases Guide](./episodes/09-databases/) ✓
- **Episode 10**: [Vector Databases](./episodes/10-vector-databases/) ✓
- **Episode 11**: [Keys in DBMS](./episodes/11-keys-in-dbms/) ✓
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

## Episode 8: CDNs Explained

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/08-cdns/) | [View Presentation](./episodes/08-cdns/presentation/)**

### What You'll Learn:
- What a Content Delivery Network (CDN) is and its core purpose
- How CDNs solve the latency problem caused by geographic distance
- The CDN workflow: Cache hits, cache misses, and origin fetching
- The key benefits: Performance, availability, security, and cost savings
- What content is ideal for CDN caching (static vs dynamic)
- Cache control mechanisms: Headers, purging, and versioning
- How to choose a CDN provider based on features and pricing
- Real-world case studies: Netflix Open Connect, Facebook's infrastructure
- Edge computing concepts and modern CDN capabilities

### Key Concepts Covered:
```
CDN = Global Network for Fast Content Delivery
├── Core Concept
│   ├── Edge Servers / PoPs (Points of Presence)
│   ├── Geographic Distribution (global network)
│   └── Content Caching at the Edge
├── The Distance Problem
│   ├── Latency increases with distance
│   ├── Tokyo user from NYC: ~180ms without CDN
│   └── Tokyo user with CDN: ~5ms (36x faster!)
├── How CDNs Work
│   ├── DNS-based routing to nearest edge
│   ├── Cache HIT: Serve from edge (1-5ms)
│   ├── Cache MISS: Fetch from origin, cache, serve
│   └── TTL-based expiration with revalidation
├── Key Benefits
│   ├── Performance: 50-90% latency reduction
│   ├── Availability: Redundancy, fail-over
│   ├── Security: DDoS protection, WAF
│   └── Cost: 80% bandwidth savings
├── What to Cache
│   ├── Static Assets (Images, CSS, JS, Fonts)
│   ├── Videos (MP4, HLS, DASH streaming)
│   └── Dynamic Content (with care!)
├── Cache Control
│   ├── Cache-Control headers (max-age, public/private)
│   ├── ETags for conditional requests (304 Not Modified)
│   ├── Manual Purging (API or dashboard)
│   └── Filename Versioning (best practice)
└── Popular Providers
    ├── Cloudflare: Free tier, security included
    ├── AWS CloudFront: Deep AWS integration
    ├── Akamai: Enterprise scale (365K+ servers)
    ├── Fastly: Real-time purging, developer focus
    └── Google Cloud CDN: GCP ecosystem
```

## Episode 9: The Ultimate Guide to Databases

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/09-databases/) | [View Presentation](./episodes/09-databases/presentation/)**

### What You'll Learn:
- What a database and DBMS are
- Database design fundamentals: entities, attributes, relationships
- SQL (Relational) databases and ACID compliance
- Four core types of NoSQL databases
- Two emerging types: Time-Series and Vector databases
- How to choose the right database for your use case
- NewSQL: Bridging SQL and NoSQL
- Polyglot persistence in modern applications

### Key Concepts Covered:
```
Database Types Overview
├── SQL (Relational Databases)
│   ├── Data Model: Tables with strict schema
│   ├── Key Feature: ACID Compliance (Atomicity, Consistency, Isolation, Durability)
│   ├── Examples: PostgreSQL, MySQL, SQL Server
│   └── Best For: Transactions, financial data, structured data
├── NoSQL (Non-Relational) - Core Types
│   ├── Key-Value Stores: Simplest model (Redis, DynamoDB)
│   │   └── Best For: Caching, sessions, simple lookups
│   ├── Document Databases: Flexible JSON documents (MongoDB)
│   │   └── Best For: User profiles, product catalogs
│   ├── Column-Family Stores: Columnar storage (Cassandra)
│   │   └── Best For: Big data analytics, time-series, logging
│   └── Graph Databases: Nodes and relationships (Neo4j)
│       └── Best For: Social networks, recommendations, fraud detection
├── NoSQL - Emerging Types
│   ├── Time-Series Databases: Optimized for timestamps (InfluxDB)
│   │   └── Best For: IoT sensors, DevOps metrics, stock data
│   └── Vector Databases: Store embeddings for AI (Pinecone, Weaviate)
│       └── Best For: AI recommendations, semantic search, chatbots
├── NewSQL: Bridging SQL and NoSQL
│   ├── Concept: ACID guarantees + horizontal scaling
│   ├── Examples: CockroachDB, YugabyteDB, TiDB
│   └── Best For: Cloud-native apps needing SQL at scale
└── Polyglot Persistence
    ├── Use multiple databases for different needs
    ├── Example: PostgreSQL (orders) + MongoDB (catalog) + Redis (cache)
    └── Modern approach: Choose right tool for each job
```

## Episode 10: Vector Databases

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/10-vector-databases/) | [View Presentation](./episodes/10-vector-databases/presentation/)**

### What You'll Learn:
- What vector embeddings are and why they matter
- How vector databases differ from traditional databases
- Approximate Nearest Neighbor (ANN) search algorithms
- Core use cases: semantic search, recommendations, RAG
- Popular vector databases: Pinecone, Weaviate, Milvus, Qdrant
- Embedding generation and model selection
- Hybrid search: combining vectors with metadata
- Performance considerations: HNSW, quantization, filtering

### Key Concepts Covered:
```
Vector Databases Fundamentals
├── Vector Embeddings
│   ├── Numerical representations of meaning
│   ├── 768-4096 dimensions (model-dependent)
│   └── Similar meanings → similar vectors
├── ANN Search Algorithms
│   ├── HNSW: Fastest for online queries
│   ├── IVF: Fast build, moderate memory
│   └── PQ: Compressed storage (80% smaller)
├── Use Cases
│   ├── Semantic Search: Meaning-based, not keyword
│   ├── RAG: Context for LLMs (most common!)
│   └── Recommendations: Similar items/users
├── Popular Vector DBs
│   ├── Pinecone: Managed, easy scaling
│   ├── Weaviate: Open source, multimodal
│   ├── Milvus: High scale, flexible
│   ├── Qdrant: Rust-based, fast, simple
│   └── Chroma: Lightweight, Python-native
└── Performance Optimization
    ├── Index tuning (HNSW m, efConstruction)
    ├── Quantization (Binary, Scalar, Product)
    └── Hybrid search (Vector + Metadata filtering)
```

## Episode 11: Keys in DBMS

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/11-keys-in-dbms/) | [View Presentation](./episodes/11-keys-in-dbms/presentation/)**

### What You'll Learn:
- The purpose of database keys in ensuring data integrity
- The difference between Super Keys, Candidate Keys, and Primary Keys
- How Primary Keys differ from Unique Keys (null handling)
- The role of Alternate Keys and Composite Keys
- Foreign Keys and referential integrity
- Surrogate vs Natural Keys and when to use each
- Performance implications: indexing Foreign Keys
- Modern distributed keys: ULIDs and Snowflake IDs
- Temporal keys for auditing and compliance

### Key Concepts Covered:
```
Database Keys Fundamentals
├── Key Hierarchy
│   ├── Super Key: Any unique set (may be redundant)
│   ├── Candidate Key: Minimal unique set (potential PKs)
│   ├── Primary Key: The chosen one (unique + NOT NULL)
│   ├── Alternate Key: Backup candidate keys
│   └── Foreign Key: Links tables, enforces referential integrity
├── Key Comparison
│   ├── Primary Key: 1 per table, NO nulls, auto-indexed
│   ├── Unique Key: Multiple allowed, 1 null typically OK
│   ├── Foreign Key: Can repeat, nullable, MUST index
│   └── Composite Key: 2+ columns form unique identifier
├── Key Types
│   ├── Natural Key: From business data (SSN, Email)
│   ├── Surrogate Key: System-generated (Auto-increment, UUID)
│   └── Temporal Key: Tracks when data was valid (auditing)
├── Modern Distributed Keys
│   ├── Snowflake ID: 64-bit, time-sortable, distributed
│   ├── ULID: Lexicographically sortable, 128-bit
│   └── Problem: UUIDv4 causes index fragmentation
└── Best Practices
    ├── Index all Foreign Keys (prevents slow JOINs)
    ├── Use Surrogate Keys for volatile data
    ├── Keep Natural Keys as Unique/Alternate Keys
    └── Every table needs a Primary Key
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
