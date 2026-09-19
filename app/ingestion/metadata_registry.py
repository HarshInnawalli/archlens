from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class DocumentRecord:
    document_id: str
    source: str
    technology: str
    topic: str
    document_type: str
    url: Optional[str]
    file_path: str


# ------------------------------------------------------------------
# DOCUMENT REGISTRY
# ------------------------------------------------------------------
#
# Add every document in data/ here.
#
# file_path must exactly match the actual file path.
#
# Example:
#
# "data/redis/pubsub.md"
#
# ------------------------------------------------------------------

DOCUMENTS = [
    # Redis official documentation
    DocumentRecord("redis_cluster_specification", "Redis cluster specification", "redis", "clustering", "official_documentation", "https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/", "data/redis/cluster-spec.md"),
    DocumentRecord("redis_key_eviction", "Redis key eviction", "redis", "caching", "official_documentation", "https://redis.io/docs/latest/develop/reference/eviction/", "data/redis/eviction.md"),
    DocumentRecord("redis_persistence", "Redis persistence", "redis", "storage", "official_documentation", "https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/", "data/redis/persistence.md"),
    DocumentRecord("redis_pubsub_messaging", "Redis pub/sub messaging", "redis", "messaging", "official_documentation", "https://redis.io/docs/latest/develop/use-cases/pub-sub/", "data/redis/pub-sub.md"),
    DocumentRecord("redis_pubsub", "Redis Pub/Sub", "redis", "messaging", "official_documentation", "https://redis.io/docs/latest/develop/pubsub/", "data/redis/pubsub.md"),
    DocumentRecord("redis_replication", "Redis replication", "redis", "replication", "official_documentation", "https://redis.io/docs/latest/operate/oss_and_stack/management/replication/", "data/redis/replication.md"),
    DocumentRecord("redis_scaling", "Scale with Redis Cluster", "redis", "scalability", "official_documentation", "https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/", "data/redis/scaling.md"),
    DocumentRecord("redis_sentinel", "High availability with Redis Sentinel", "redis", "high_availability", "official_documentation", "https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/", "data/redis/sentinel.md"),
    DocumentRecord("redis_streaming", "Redis streaming", "redis", "messaging", "official_documentation", "https://redis.io/docs/latest/develop/use-cases/streaming/", "data/redis/streaming.md"),
    DocumentRecord("redis_streams", "Redis Streams", "redis", "messaging", "official_documentation", "https://redis.io/docs/latest/develop/data-types/streams/", "data/redis/streams.md"),
    DocumentRecord("redis_transactions", "Redis Transactions", "redis", "transactions", "official_documentation", "https://redis.io/docs/latest/develop/interact/transactions/", "data/redis/transactions.md"),

    # Apache Kafka documentation. These source files do not identify stable per-page URLs.
    DocumentRecord("kafka_architecture", "Apache Kafka Architecture", "kafka", "architecture", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/streams/architecture.md", "data/kafka/architecture.md"),
    DocumentRecord("kafka_basic_operations", "Apache Kafka Basic Operations", "kafka", "operations", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/operations/basic-kafka-operations.md", "data/kafka/basic-kafka-operations.md"),
    DocumentRecord("kafka_compatibility", "Apache Kafka Compatibility", "kafka", "compatibility", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/getting-started/compatibility.md", "data/kafka/compatibility.md"),
    DocumentRecord("kafka_consumer_configs", "Apache Kafka Consumer and Share Consumer Configs", "kafka", "configuration", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/configuration/consumer-configs.md", "data/kafka/consumer-configs.md"),
    DocumentRecord("kafka_core_concepts", "Apache Kafka Core Concepts", "kafka", "messaging", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/streams/core-concepts.md", "data/kafka/core-concepts.md"),
    DocumentRecord("kafka_design", "Apache Kafka Design", "kafka", "architecture", "official_documentation", "https://github.com/apache/kafka-site//tree/markdown/content/en/43/design/design.md", "data/kafka/design.md"),
    DocumentRecord("kafka_docker", "Apache Kafka Docker", "kafka", "deployment", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/getting-started/docker.md", "data/kafka/docker.md"),
    DocumentRecord("kafka_distribution", "Apache Kafka Distribution", "kafka", "scalability", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/implementation/distribution.md", "data/kafka/distribution.md"),
    DocumentRecord("kafka_introduction", "Apache Kafka Introduction", "kafka", "messaging", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/getting-started/introduction.md", "data/kafka/introduction.md"),
    DocumentRecord("kafka_log", "Apache Kafka Log", "kafka", "storage", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/implementation/log.md", "data/kafka/log.md"),
    DocumentRecord("kafka_messages", "Apache Kafka Messages", "kafka", "messaging", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/implementation/messages.md", "data/kafka/messages.md"),
    DocumentRecord("kafka_network_layer", "Apache Kafka Network Layer", "kafka", "networking", "official_documentation", "https://kafka.apache.org/43/implementation/network-layer/", "data/kafka/network-layer.md"),
    DocumentRecord("kafka_overview", "Apache Kafka Overview", "kafka", "messaging", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/kafka-connect/overview.md", "data/kafka/overview.md"),
    DocumentRecord("kafka_use_cases", "Apache Kafka Use Cases", "kafka", "messaging", "official_documentation", "https://github.com/apache/kafka-site/blob/markdown/content/en/43/getting-started/uses.md", "data/kafka/uses.md"),

    # gRPC official documentation
    DocumentRecord("grpc_core_concepts", "gRPC Core concepts, architecture and lifecycle", "grpc", "rpc", "official_documentation", "https://grpc.io/docs/what-is-grpc/core-concepts/", "data/gRPC/core-concepts.md"),
    DocumentRecord("grpc_deadlines", "gRPC Deadlines", "grpc", "fault_tolerance", "official_documentation", "https://grpc.io/docs/guides/deadlines/", "data/gRPC/deadlines.md"),
    DocumentRecord("grpc_error_handling", "gRPC Error handling", "grpc", "fault_tolerance", "official_documentation", "https://grpc.io/docs/guides/error/", "data/gRPC/error.md"),
    DocumentRecord("grpc_flow_control", "gRPC Flow Control", "grpc", "flow_control", "official_documentation", "https://grpc.io/docs/guides/flow-control/", "data/gRPC/flow-control.md"),
    DocumentRecord("grpc_performance", "gRPC Performance Best Practices", "grpc", "performance", "official_documentation", "https://grpc.io/docs/guides/performance/", "data/gRPC/performance.md"),
    DocumentRecord("grpc_retry", "gRPC Retry", "grpc", "fault_tolerance", "official_documentation", "https://grpc.io/docs/guides/retry/", "data/gRPC/retry.md"),

    # MDN HTTP documentation
    DocumentRecord("http_caching", "MDN: HTTP caching", "http", "caching", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching", "data/REST_HTTP/HTTP caching - HTTP _ MDN.html"),
    DocumentRecord("http_conditional_requests", "MDN: HTTP conditional requests", "http", "caching", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Conditional_requests", "data/REST_HTTP/HTTP conditional requests - HTTP _ MDN.html"),
    DocumentRecord("http_messages", "MDN: HTTP messages", "http", "messaging", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages", "data/REST_HTTP/HTTP messages - HTTP _ MDN.html"),
    DocumentRecord("http_request_methods", "MDN: HTTP request methods", "http", "api_design", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods", "data/REST_HTTP/HTTP request methods - HTTP _ MDN.html"),
    DocumentRecord("http_response_status_codes", "MDN: HTTP response status codes", "http", "api_design", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status", "data/REST_HTTP/HTTP response status codes - HTTP _ MDN.html"),
    DocumentRecord("http_connection_management", "MDN: Connection management in HTTP/1.x", "http", "networking", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x", "data/REST_HTTP/Connection management in HTTP_1.x - HTTP _ MDN.html"),
    DocumentRecord("http_overview", "MDN: Overview of HTTP", "http", "networking", "official_documentation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview", "data/REST_HTTP/Overview of HTTP - HTTP _ MDN.html"),

    # PostgreSQL 18 official documentation
    DocumentRecord("postgresql_index_introduction", "PostgreSQL: Indexes Introduction", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-intro.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.1. Introduction.html"),
    DocumentRecord("postgresql_index_types", "PostgreSQL: Index Types", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-types.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.2. Index Types.html"),
    DocumentRecord("postgresql_multicolumn_indexes", "PostgreSQL: Multicolumn Indexes", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-multicolumn.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.3. Multicolumn Indexes.html"),
    DocumentRecord("postgresql_indexes_order_by", "PostgreSQL: Indexes and ORDER BY", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-ordering.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.4. Indexes and ORDER BY.html"),
    DocumentRecord("postgresql_combining_indexes", "PostgreSQL: Combining Multiple Indexes", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-bitmap-scans.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.5. Combining Multiple Indexes.html"),
    DocumentRecord("postgresql_unique_indexes", "PostgreSQL: Unique Indexes", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-unique.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.6. Unique Indexes.html"),
    DocumentRecord("postgresql_expression_indexes", "PostgreSQL: Indexes on Expressions", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-expressional.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.7. Indexes on Expressions.html"),
    DocumentRecord("postgresql_partial_indexes", "PostgreSQL: Partial Indexes", "postgresql", "indexing", "official_documentation", "https://www.postgresql.org/docs/18/indexes-partial.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 11.8. Partial Indexes.html"),
    DocumentRecord("postgresql_mvcc_introduction", "PostgreSQL: Concurrency Control Introduction", "postgresql", "transactions", "official_documentation", "https://www.postgresql.org/docs/18/mvcc-intro.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 13.1. Introduction.html"),
    DocumentRecord("postgresql_transaction_isolation", "PostgreSQL: Transaction Isolation", "postgresql", "transactions", "official_documentation", "https://www.postgresql.org/docs/18/transaction-iso.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 13.2. Transaction Isolation.html"),
    DocumentRecord("postgresql_explicit_locking", "PostgreSQL: Explicit Locking", "postgresql", "transactions", "official_documentation", "https://www.postgresql.org/docs/18/explicit-locking.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 13.3. Explicit Locking.html"),
    DocumentRecord("postgresql_application_consistency", "PostgreSQL: Application-Level Data Consistency Checks", "postgresql", "consistency", "official_documentation", "https://www.postgresql.org/docs/18/applevel-consistency.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 13.4. Data Consistency Checks at the Application Level.html"),
    DocumentRecord("postgresql_explain", "PostgreSQL: Using EXPLAIN", "postgresql", "query_planning", "official_documentation", "https://www.postgresql.org/docs/18/using-explain.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 14.1. Using EXPLAIN.html"),
    DocumentRecord("postgresql_planner_statistics", "PostgreSQL: Statistics Used by the Planner", "postgresql", "query_planning", "official_documentation", "https://www.postgresql.org/docs/18/planner-stats.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 14.2. Statistics Used by the Planner.html"),
    DocumentRecord("postgresql_explicit_joins", "PostgreSQL: Controlling the Planner with Explicit JOIN Clauses", "postgresql", "query_planning", "official_documentation", "https://www.postgresql.org/docs/18/explicit-joins.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 14.3. Controlling the Planner with Explicit JOIN Clauses.html"),
    DocumentRecord("postgresql_populating_database", "PostgreSQL: Populating a Database", "postgresql", "storage", "official_documentation", "https://www.postgresql.org/docs/18/populate.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 14.4. Populating a Database.html"),
    DocumentRecord("postgresql_non_durable_settings", "PostgreSQL: Non-Durable Settings", "postgresql", "durability", "official_documentation", "https://www.postgresql.org/docs/18/non-durability.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 14.5. Non-Durable Settings.html"),
    DocumentRecord("postgresql_connections_authentication", "PostgreSQL: Connections and Authentication", "postgresql", "security", "official_documentation", "https://www.postgresql.org/docs/18/runtime-config-connection.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 19.3. Connections and Authentication.html"),
    DocumentRecord("postgresql_resource_consumption", "PostgreSQL: Resource Consumption", "postgresql", "performance", "official_documentation", "https://www.postgresql.org/docs/18/runtime-config-resource.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 19.4. Resource Consumption.html"),
    DocumentRecord("postgresql_replication_solutions", "PostgreSQL: Comparison of Replication Solutions", "postgresql", "replication", "official_documentation", "https://www.postgresql.org/docs/18/different-replication-solutions.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 26.1. Comparison of Different Solutions.html"),
    DocumentRecord("postgresql_log_shipping", "PostgreSQL: Log-Shipping Standby Servers", "postgresql", "replication", "official_documentation", "https://www.postgresql.org/docs/18/warm-standby.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 26.2. Log-Shipping Standby Servers.html"),
    DocumentRecord("postgresql_failover", "PostgreSQL: Failover", "postgresql", "high_availability", "official_documentation", "https://www.postgresql.org/docs/18/warm-standby-failover.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 26.3. Failover.html"),
    DocumentRecord("postgresql_hot_standby", "PostgreSQL: Hot Standby", "postgresql", "high_availability", "official_documentation", "https://www.postgresql.org/docs/18/hot-standby.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 26.4. Hot Standby.html"),
    DocumentRecord("postgresql_high_availability", "PostgreSQL: High Availability, Load Balancing, and Replication", "postgresql", "high_availability", "official_documentation", "https://www.postgresql.org/docs/18/high-availability.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ Chapter 26. High Availability, Load Balancing, and Replication.html"),
    DocumentRecord("postgresql_documentation_18", "PostgreSQL 18.6 Documentation", "postgresql", "general", "official_documentation", "https://www.postgresql.org/docs/18/index.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ PostgreSQL 18.6 Documentation.html"),
    DocumentRecord("postgresql_table_partitioning", "PostgreSQL: Table Partitioning", "postgresql", "partitioning", "official_documentation", "https://www.postgresql.org/docs/18/ddl-partitioning.html", "data/postgreSQL/PostgreSQL_ Documentation_ 18_ 5.12. Table Partitioning.html"),

    # Root-level engineering articles and research papers
    DocumentRecord("discord_authentication_outage_2023", "Discord: 25% or 6 to 4: The 11/6/23 Authentication Outage", "distributed_systems", "incident_response", "engineering_case_study", "https://discord.com/blog/authentication-outage?utm_source=chatgpt.com", "data/25% or 6 to 4_ The 11_6_23 Authentication Outage.html"),
    DocumentRecord("discord_indexes_trillions_messages", "Discord: How Discord Indexes Trillions of Messages", "distributed_systems", "indexing", "engineering_case_study", "https://discord.com/blog/how-discord-indexes-trillions-of-messages?utm_source=chatgpt.com", "data/How Discord Indexes Trillions of Messages.html"),
    DocumentRecord("discord_automates_scylladb_clusters", "Discord: How Discord Automates ScyllaDB Clusters at Scale", "distributed_systems", "operations", "engineering_case_study", "https://discord.com/blog/how-discord-automates-scylladb-clusters-at-scale?utm_source=chatgpt.com", "data/How Discord Automates ScyllaDB Clusters at Scale.html"),
    DocumentRecord("discord_stores_trillions_messages", "Discord: How Discord Stores Trillions of Messages", "distributed_systems", "storage", "engineering_case_study", "https://discord.com/blog/how-discord-indexes-trillions-of-messages?utm_source=chatgpt.com", "data/How Discord Stores Trillions of Messages.html"),
    DocumentRecord("discord_go_to_rust", "Discord: Why Discord is switching from Go to Rust", "distributed_systems", "performance", "engineering_case_study", "https://discord.com/blog/why-discord-is-switching-from-go-to-rust?utm_source=chatgpt.com", "data/Why Discord is switching from Go to Rust.html"),
    DocumentRecord("stripe_idempotency", "Stripe: Designing robust and predictable APIs with idempotency", "http", "api_design", "technical_article", "https://stripe.com/blog/idempotency", "data/Designing robust and predictable APIs with idempotency.html"),
    DocumentRecord("healthcare_fog_cloud_monitoring", "Hybrid Workload Enabled and Secure Healthcare Monitoring Sensing Framework in Distributed Fog-Cloud Network", "distributed_systems", "fault_tolerance", "research_paper", "https://doi.org/10.3390/electronics10161974", "data/1974.pdf"),
    DocumentRecord("raft_understandable_consensus", "In Search of an Understandable Consensus Algorithm", "distributed_systems", "consensus", "research_paper", "https://www.usenix.org/conference/atc14/technical-sessions/presentation/ongaro", "data/atc14-paper-ongaro.pdf"),
    DocumentRecord("craft_erasure_coded_raft", "CRaft: An Erasure-coding-supported Version of Raft for Reducing Storage Cost and Network Cost", "distributed_systems", "consensus", "research_paper", "https://www.usenix.org/conference/fast20/presentation/wang-zizhong", "data/fast20-wang_zizhong.pdf"),
    DocumentRecord("raft_read_scalability", "Leader or Majority: Improving Read Scalability in Raft-like Consensus Protocols", "distributed_systems", "scalability", "research_paper", "https://www.usenix.org/system/files/conference/hotcloud17/hotcloud17-paper-arora.pdf", "data/hotcloud17-paper-arora.pdf"),
    DocumentRecord("hotcloud19_ahn", "HotCloud 2019 paper by Ahn et al.", "distributed_systems", "general", "research_paper", "https://www.usenix.org/system/files/hotcloud19-paper-ahn.pdf", "data/hotcloud19-paper-ahn.pdf"),
    DocumentRecord("jetpack_consensus", "Jetpack: Consensus Made Generally Fast", "distributed_systems", "consensus", "research_paper", "https://www.usenix.org/conference/osdi26/presentation/tang", "data/osdi26-tang.pdf"),
    DocumentRecord("rajomon_overload_control", "Rajomon: Decentralized and Coordinated Overload Control for Latency-Sensitive Microservices", "distributed_systems", "fault_tolerance", "research_paper", "https://www.usenix.org/conference/nsdi25/presentation/xing", "data/nsdi25-xing.pdf"),
    DocumentRecord("mongodb_pull_based_replication", "Fault-Tolerant Replication with Pull-Based Consensus in MongoDB", "distributed_systems", "replication", "research_paper", "https://www.usenix.org/conference/nsdi21/presentation/zhou", "data/nsdi21-zhou.pdf"),
    DocumentRecord("scalability_fault_tolerance_distributed_systems", "Scalability and Fault Tolerance in Distributed Systems", "distributed_systems", "fault_tolerance", "technical_article", "https://www.researchgate.net/publication/395012635_Scalability_and_Fault_Tolerance_in_Distributed_Systems", "data/ScalabilityandFaultToleranceinDistributedSystems.docxRumi.pdf"),
]


def get_registry() -> dict[str, DocumentRecord]:
    """
    Return the document registry indexed by file path.
    """

    return {
        record.file_path: record
        for record in DOCUMENTS
    }


def get_document_by_path(
    file_path: str,
) -> Optional[DocumentRecord]:
    """
    Retrieve metadata for a specific file.
    """

    registry = get_registry()

    return registry.get(file_path)
