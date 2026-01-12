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
- **Episode 12**: [Normalization vs Denormalization](./episodes/12-normalization-denormalization/) ✓
- **Episode 13**: [Database Indexing Mastery](./episodes/13-indexing/) ✓
- **Episode 14**: [Sharding & Partitioning](./episodes/14-sharding-partitioning/) ✓
- **Episode 15**: [Database Transactions & ACID](./episodes/15-database-transactions/) ✓
- **Episode 16**: [CAP Theorem is Not Enough](./episodes/16-cap-theorem/) ✓
- **Episode 17**: [OSI Model Deep Dive](./episodes/17-osi-model/) ✓
- **Episode 18**: [TCP vs UDP - The Complete Engineering Deep Dive](./episodes/18-tcp-udp/) ✓
- **Episode 19**: [REST vs gRPC - The Complete Architecture Masterclass](./episodes/19-rest-grpc/) ✓
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

## Episode 12: Normalization vs Denormalization

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/12-normalization-denormalization/) | [View Presentation](./episodes/12-normalization-denormalization/presentation/)**

### What You'll Learn:
- What normalization is and why it ensures data integrity
- The three data anomalies: Insertion, Update, and Deletion
- Normal Forms progression: 1NF through 5NF
- Functional, partial, and transitive dependencies
- Boyce-Codd Normal Form (BCNF) and when to use it
- What denormalization is and why it improves read performance
- Denormalization techniques: redundant columns, table splitting, materialized views
- When to choose normalization (OLTP) vs denormalization (OLAP)
- The hybrid approach in modern system architecture

### Key Concepts Covered:
```
Database Design: Structure vs Performance
├── Data Anomalies (Why Normalize?)
│   ├── Insertion Anomaly: Cannot add data without other data
│   ├── Update Anomaly: Inconsistency from multiple copies
│   └── Deletion Anomaly: Losing data when deleting unrelated record
├── Normal Forms (Normalization)
│   ├── 1NF: Atomic values, no repeating groups
│   ├── 2NF: No partial dependency (full key required)
│   ├── 3NF: No transitive dependency
│   ├── BCNF: Every determinant is a superkey
│   ├── 4NF: No multi-valued dependency
│   └── 5NF: No join dependency (rare)
├── Denormalization Techniques
│   ├── Redundant Columns: Duplicate data to avoid JOINs
│   ├── Derived Columns: Pre-computed values
│   ├── Table Splitting: Horizontal/Vertical partitioning
│   └── Materialized Views: Pre-computed query results
└── Design Decisions
    ├── Normalize for: OLTP, data integrity, write-heavy
    ├── Denormalize for: OLAP, read-heavy, analytics
    └── Hybrid: Normalized source + denormalized views
```

## Episode 13: Database Indexing Mastery

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/13-indexing/) | [View Presentation](./episodes/13-indexing/presentation/)**

### What You'll Learn:
- What database indexes are and why they are critical for performance
- B-Tree and B+Tree data structures that power most database indexes
- The difference between clustered and non-clustered indexes
- How composite indexes work and the leftmost prefix rule
- What covering indexes are and when to use them
- Different index types: Hash, Bitmap, Full-Text, and PostgreSQL-specific indexes
- How to read and interpret execution plans with EXPLAIN
- Index maintenance: fragmentation, VACUUM, and fill factors
- Best practices for index design and avoiding common anti-patterns

### Key Concepts Covered:
```
Database Indexing Fundamentals
├── Index Basics
│   ├── B-Tree/B+Tree: Self-balancing tree data structure
│   ├── Trade-offs: Speed up reads, slow down writes
│   └── Cost: 20-30% storage overhead per index
├── Index Types
│   ├── Clustered: Data physically sorted, one per table
│   ├── Non-Clustered: Separate structure with row pointers
│   ├── Composite: Multiple columns, leftmost prefix rule
│   └── Covering: Query satisfied entirely from index
├── Advanced Index Types
│   ├── Hash: O(1) equality lookups, no range support
│   ├── Bitmap: Low-cardinality, data warehousing
│   ├── Full-Text: Inverted index for text search
│   └── PostgreSQL: GiST, GIN, BRIN specialized indexes
├── Index Design
│   ├── Selectivity: Higher is better (> 20% ideal)
│   ├── Column Order: Equality first, range last
│   ├── Functional Indexes: Index on expressions
│   └── Partial Indexes: Filtered conditions
├── Execution Plans
│   ├── EXPLAIN: Read query execution strategy
│   ├── Seq Scan: Full table scan (warning sign!)
│   ├── Index Scan: Index used + table lookup
│   └── Index Only Scan: Fastest (covering index)
└── Maintenance
    ├── Fragmentation: Internal and external
    ├── VACUUM: Reclaim space, update statistics
    ├── FILLFACTOR: Balance storage vs updates
    └── Monitoring: pg_stat_user_indexes usage stats
```

## Episode 14: Sharding & Partitioning

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/14-sharding-partitioning/) | [View Presentation](./episodes/14-sharding-partitioning/presentation/)**

### What You'll Learn:
- The critical distinction between partitioning and sharding
- Types of partitions: Range, List, Hash, and Composite
- How to select optimal shard keys (cardinality, uniformity, query alignment)
- Directory-based sharding and lookup strategies
- Cross-shard operations: transactions, joins, and aggregations
- Resharding strategies and zero-downtime migrations
- Real-world sharding patterns from Vitess, CockroachDB, and MongoDB

### Key Concepts Covered:
```
Scaling Databases: Distribution Strategies
├── Sharding vs Partitioning
│   ├── Partitioning: Splitting within ONE server/cluster
│   ├── Sharding: Splitting ACROSS multiple servers/nodes
│   └── Shared-Nothing Architecture
├── Partition Types
│   ├── Range: Consecutive ranges (dates, numeric)
│   ├── List: Specific values (regions, categories)
│   ├── Hash: Uniform distribution via hash function
│   └── Composite: Range-Hash, Range-List combinations
├── Shard Key Selection
│   ├── Cardinality: High cardinality required
│   ├── Uniformity: Even data and access distribution
│   └── Query Alignment: Target single shard when possible
├── Cross-Shard Operations
│   ├── Transactions: Two-Phase Commit (2PC)
│   ├── Joins: Data colocation vs scatter-gather
│   └── Aggregations: MapReduce-style distributed queries
├── Resharding
│   ├── Triggers: Growth, hotspots, capacity planning
│   ├── Strategies: Split vs Migrate approaches
│   └── Zero-Downtime: Dual-write, blue-green deployment
└── Platforms
    ├── Vitess: MySQL sharding middleware (YouTube)
    ├── CockroachDB: Automatic distributed SQL
    └── MongoDB: Document database sharding
```

## Episode 15: Database Replication & Leader Election

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/15-replication-leader-election/) | [View Presentation](./episodes/15-replication-leader-election/presentation/)**

### What You'll Learn:
- Database replication: Master-Slave patterns, binary logs, and GTIDs
- Synchronous vs asynchronous replication trade-offs
- Practical MySQL/MariaDB replication setup
- Leader election: Bully, Ring, Raft, and Paxos algorithms
- Distributed locking with leases and heartbeats
- Split brain prevention and fencing tokens
- Sharding to scale beyond single-master limitations

### Key Concepts Covered:
```
Distributed Coordination: Replication and Consensus
├── Replication Fundamentals
│   ├── Master-Slave: Single writer, multiple readers
│   ├── Binary Logs (MySQL) vs WAL (PostgreSQL)
│   ├── GTIDs for position tracking
│   └── Cascading replication
├── Consistency Trade-offs
│   ├── Synchronous: Strong consistency, high latency
│   ├── Asynchronous: High performance, eventual consistency
│   └── Semi-Synchronous: Hybrid approach
├── Leader Election
│   ├── Bully Algorithm: Highest ID wins
│   ├── Ring Algorithm: Ring topology messaging
│   └── Raft: Leader, Follower, Candidate states
├── Consensus Protocols
│   ├── Raft: Terms, heartbeats, log replication
│   ├── Paxos: Prepare and Accept phases
│   └── Real-world: etcd, Consul, Spanner
├── Distributed Coordination
│   ├── ZooKeeper: ZAB protocol, ephemeral znodes
│   ├── etcd: Strong consistency, Kubernetes backbone
│   ├── Consul: Service discovery, KV store
│   └── Cloud primitives: Azure Blob leases, DynamoDB Lock
├── Failure Scenarios
│   ├── Split brain: Dual leader prevention
│   ├── Fencing tokens for safe leader handoff
│   └── Idempotency for duplicate handling
└── Scaling Patterns
    ├── Sharding: Partitioning across masters
    └── Multi-shard operations and rebalancing
```

## Episode 16: CAP Theorem is Not Enough - The Truth About Distributed Systems

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/16-cap-theorem/) | [View Presentation](./episodes/16-cap-theorem/presentation/)**

### What You'll Learn:
- The real meaning of CAP theorem and why "Pick Two" is misleading
- Why CA systems do not actually exist in distributed computing
- The critical difference between CAP Consistency and ACID Consistency
- How to use the PACELC framework for real-world system design
- How to classify databases as PA/EL vs PC/EC
- Practical decision framework for choosing the right consistency model

### Key Concepts Covered:
```
Distributed Consistency Trade-offs
├── CAP Theorem Fundamentals
│   ├── Consistency: Linearizability (everyone sees same data)
│   ├── Availability: Every request gets response
│   ├── Partition Tolerance: Non-negotiable in distributed systems
│   └── Reality: CA systems don't exist (P is mandatory)
├── The CAP Blind Spot
│   ├── Partitions are rare (1% of time)
│   ├── CAP says nothing about normal operations
│   └── Missing metric: Latency
├── PACELC Framework
│   ├── PAC: If Partition, choose Availability or Consistency
│   ├── ELC: Else (no partition), choose Latency or Consistency
│   └── Daniel Abadi (Yale), 2010
├── Database Classifications
│   ├── PA/EL: DynamoDB, Cassandra (Availability + Low Latency)
│   ├── PC/EC: BigTable, HBase, Spanner (Consistency + Consistency)
│   └── Tunable: Cosmos DB, MongoDB (adjustable per query)
└── Practical Decision Framework
    ├── Money involved? -> PC/EC (accuracy critical)
    ├── Speed is product? -> PA/EL (availability critical)
    └── Global distribution? -> Expect partitions
```

## Episode 17: The OSI Model

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/17-osi-model/) | [View Presentation](./episodes/17-osi-model/presentation/)**

### What You'll Learn:
- The 7 layers of the OSI model and their specific responsibilities
- How data flows through the network stack (encapsulation and decapsulation)
- The role of each layer in real-world protocols (Ethernet, IP, TCP, HTTP)
- How troubleshooting tools like ping, traceroute, and Wireshark map to layers
- Common misconceptions about the OSI model in modern networking
- How the TCP/IP model maps to the OSI model

### Key Concepts Covered:
```
OSI Model Fundamentals
├── 7 Layers Overview
│   ├── Physical (Layer 1): Bits, cables, signals
│   ├── Data Link (Layer 2): Frames, MAC addresses, switches
│   ├── Network (Layer 3): Packets, IP addresses, routers
│   ├── Transport (Layer 4): Segments, TCP/UDP, end-to-end
│   ├── Session (Layer 5): Connections, auth, sync
│   ├── Presentation (Layer 6): Format, encryption, compression
│   └── Application (Layer 7): HTTP, DNS, user protocols
├── Encapsulation Process
│   ├── Data: Application message
│   ├── Segment: Transport header (TCP/UDP)
│   ├── Packet: Network header (IP)
│   ├── Frame: Data Link header + trailer (Ethernet)
│   └── Bits: Physical transmission
├── Protocol Mapping
│   ├── Layer 7: HTTP, DNS, SMTP, FTP
│   ├── Layer 6: SSL/TLS, JPEG, ASCII
│   ├── Layer 5: RPC, SQL sessions
│   ├── Layer 4: TCP, UDP
│   ├── Layer 3: IP, ICMP, ARP
│   ├── Layer 2: Ethernet, MAC, Switch
│   └── Layer 1: Cables, Hubs, Signals
└── Modern Relevance
    ├── OSI as troubleshooting framework
    ├── TCP/IP as practical implementation
    ├── Why layers still matter
    └── Network virtualization and SDN
```

## Episode 18: TCP vs UDP

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/18-tcp-udp/) | [View Presentation](./episodes/18-tcp-udp/presentation/)**

### What You'll Learn:
- How TCP and UDP operate at the Transport Layer (Layer 4)
- The fundamental differences between connection-oriented and connectionless protocols
- TCP's reliability mechanisms: handshakes, sequencing, acknowledgments, and retransmissions
- UDP's minimalist design and why it excels in real-time scenarios
- The Head-of-Line Blocking problem and its impact on performance
- How QUIC and HTTP/3 leverage UDP for modern web performance
- Practical decision frameworks for choosing the right protocol

### Key Concepts Covered:
```
Transport Layer Protocols: TCP vs UDP
├── TCP Fundamentals
│   ├── Connection-oriented: 3-way handshake
│   ├── Reliable: ACKs, retransmissions
│   ├── Ordered: Guaranteed packet sequencing
│   ├── Flow control: Sliding window
│   └── Congestion control: Adapts to network
├── UDP Fundamentals
│   ├── Connectionless: No handshake
│   ├── Fast: Minimal 8-byte header
│   ├── Stateless: No connection tracking
│   └── Best-effort: No guarantees
├── Key Differences
│   ├── Overhead: TCP 20-60 bytes vs UDP 8 bytes
│   ├── Latency: TCP handshake cost vs UDP immediate
│   ├── Ordering: TCP blocks vs UDP independent
│   └── Use cases: TCP web/email vs UDP gaming/streaming
├── Head-of-Line Blocking
│   ├── TCP: Lost packet 1 blocks 2, 3, 4
│   ├── Impact: Jitter in real-time apps
│   └── Solution: QUIC per-stream reliability
├── Modern Evolution
│   ├── QUIC: Reliability on UDP (HTTP/3)
│   ├── Benefits: 0-RTT, no HoL blocking
│   ├── Migration: Survives WiFi to 5G
│   └── Adoption: 30%+ of web traffic
└── Decision Framework
    ├── TCP: Web, email, files (reliability first)
    ├── UDP: Gaming, VoIP, streaming (speed first)
    └── QUIC: Best of both worlds
```

## Episode 19: REST vs gRPC

**[Watch the Video](http://youtube.com/@ThatNotesGuy) | [Read the Notes](./episodes/19-rest-grpc/) | [View Presentation](./episodes/19-rest-grpc/presentation/)**

### What You'll Learn:
- What RPC (Remote Procedure Call) is and how it enables distributed communication
- The definition and constraints of REST as an architectural style
- The Richardson Maturity Model and HATEOAS principles
- What gRPC is and why Google open-sourced it in 2015
- Protocol Buffers (Protobuf) as a binary serialization format
- HTTP/2 vs HTTP/1.1 and the performance implications
- The four types of gRPC: Unary, Server Streaming, Client Streaming, Bidirectional
- When to choose REST vs gRPC based on your use case
- Load balancing complexities with both approaches
- Real-world code examples for both paradigms

### Key Concepts Covered:
```
Communication Patterns: REST vs gRPC
├── RPC Foundation
│   ├── Remote Procedure Call: Execute code on remote machine
│   ├── Client Stub: Proxy that hides network complexity
│   ├── Marshalling: Serializing parameters
│   └── Network Transparency: Looks like local function call
├── REST Architecture
│   ├── Roy Fielding (2000), architectural style, NOT protocol
│   ├── Constraints: Stateless, Cacheable, Uniform Interface
│   ├── Everything is a Resource (identified by URI)
│   ├── HTTP Methods: GET, POST, PUT, PATCH, DELETE
│   └── Richardson Maturity Model: Levels 0-3 (HATEOAS)
├── gRPC Framework
│   ├── Google (2015), part of CNCF
│   ├── HTTP/2 for transport (multiplexing, binary)
│   ├── Protocol Buffers for serialization (binary, efficient)
│   ├── Contract-First: Define .proto before coding
│   └── Four RPC Types: Unary, Server, Client, Bidirectional
├── Performance Comparison
│   ├── Payload: Protobuf 50-70% smaller than JSON
│   ├── Speed: Protobuf 3-10x faster parsing
│   ├── Latency: HTTP/2 multiplexing reduces overhead
│   └── Winner: gRPC 7-10x faster for internal services
├── Protocol Buffers
│   ├── Binary serialization, not human-readable
│   ├── Field tags (1, 2, 3...) identify fields
│   ├── Single source of truth in .proto files
│   └── Schema evolution support
├── HTTP/2 Advantages
│   ├── Multiplexing: Multiple streams over single TCP
│   ├── Header Compression (HPACK)
│   ├── Binary framing (not text)
│   └── Bidirectional communication
├── gRPC RPC Types
│   ├── Unary: Simple request/response (like REST)
│   ├── Server Streaming: Request, stream responses
│   ├── Client Streaming: Stream requests, single response
│   └── Bidirectional: Both sides stream independently
├── Decision Framework
│   ├── REST: Browser clients, public APIs, simple CRUD
│   ├── gRPC: Internal services, polyglot, streaming, low latency
│   ├── Flowchart: Browser? -> REST | Latency critical? -> gRPC
└── Challenges
    ├── REST: Universally supported, easy debugging
    ├── gRPC: Browser support requires proxy (gRPC-Web)
    ├── Load Balancing: gRPC needs L7, HTTP/2 persistent connections
    └── Debugging: gRPC requires deserialization tools
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
