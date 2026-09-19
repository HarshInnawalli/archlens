from app.graph.workflow import build_graph


architectures = [

    # 1. Redis Pub/Sub
    """
    I am building a real-time collaborative document application.

    The frontend communicates with a REST API gateway.
    The gateway communicates synchronously with three backend services.
    PostgreSQL stores documents.
    Redis stores sessions and provides Pub/Sub.
    The system is expected to support 100,000 concurrent users.
    Low latency is more important than strong consistency.
    """,

    # 2. Kafka
    """
    I am building an event-driven order processing system.

    Clients communicate with an HTTP API gateway.
    The API publishes order events to Apache Kafka.
    Several backend services consume the Kafka topics asynchronously.
    Kafka is responsible for durable event delivery.
    PostgreSQL stores the transactional order data.
    The system must process 50,000 orders per second.
    Losing an order event is unacceptable.
    """,

    # 3. gRPC
    """
    I am designing a microservice architecture for a high-throughput
    financial analytics platform.

    External clients communicate through a REST API.
    Internal services communicate using gRPC.
    There are eight backend services.
    Each request may involve calls to several downstream services.
    The system prioritizes low latency and high internal throughput.
    """,

    # 4. PostgreSQL scalability
    """
    I am building a social media backend.

    All application data is stored in a single PostgreSQL database.
    The application has 2 million daily active users.
    Users can create posts, comments, likes, and notifications.
    The database is expected to handle 100,000 writes per second.
    The architecture prioritizes strong consistency.
    """,

    # 5. REST + synchronous microservices
    """
    I am building an e-commerce platform.

    The frontend communicates with a REST API gateway.
    The gateway synchronously calls the authentication,
    inventory, payment, and recommendation services.
    A checkout request may therefore involve all four services.
    The system must provide low checkout latency.
    The application is expected to handle 20,000 requests per second.
    """,

    # 6. Kafka vs synchronous communication
    """
    I am designing a video processing platform.

    Users upload videos through an HTTP API.
    The API synchronously calls the video processing service.
    Video processing jobs may take several minutes.
    The system uses Kafka to distribute processing events.
    Workers consume jobs from Kafka and process them asynchronously.
    Processing jobs must not be lost if a worker crashes.
    """,

    # 7. Redis as primary storage
    """
    I am designing a multiplayer game backend.

    The API servers use Redis as the primary storage system for
    player state.
    Redis also provides Pub/Sub for real-time game events.
    The system must support 500,000 concurrent players.
    Player state must survive server and process failures.
    Very low latency is the primary requirement.
    """,

    # 8. gRPC + high fan-out
    """
    I am building a large microservice platform.

    The API gateway communicates with backend services using gRPC.
    A single user request can trigger calls to 20 downstream services.
    All downstream calls are synchronous.
    The system must maintain low latency under heavy load.
    The architecture is expected to support 100,000 requests per second.
    """

        # 9. Kafka + PostgreSQL + Redis
    """
    I am building an event-driven e-commerce platform.

    Clients communicate with a REST API gateway.
    Backend services communicate synchronously using gRPC.
    Kafka is used for asynchronous order and payment events.
    PostgreSQL stores transactional data.
    Redis stores sessions and frequently accessed product data.
    The system must support 100,000 concurrent users.
    Orders and payments must not be lost.
    Low latency is important, but transactional consistency is required.
    """,

    # 10. REST + gRPC + Kafka + Redis + PostgreSQL
    """
    I am designing a large-scale food delivery platform.

    Mobile clients communicate with a REST API gateway.
    Internal services communicate using gRPC.
    Kafka handles asynchronous events such as order updates,
    driver location updates, and notifications.
    PostgreSQL stores orders and payments.
    Redis stores sessions, restaurant availability, and frequently
    accessed data.
    The system must support 200,000 concurrent users.
    Real-time updates should have very low latency.
    """,

    # 11. Synchronous + asynchronous hybrid architecture
    """
    I am building a financial transaction platform.

    Clients connect through a REST API.
    The API synchronously calls authentication and transaction
    services using gRPC.
    Completed transactions are published to Kafka for asynchronous
    fraud detection and analytics.
    PostgreSQL stores the authoritative transaction records.
    Redis caches user session information.
    Transaction processing requires strong consistency,
    while analytics can tolerate eventual consistency.
    """,

    # 12. High-scale mixed architecture
    """
    I am designing a real-time collaborative application.

    Clients connect through a REST API gateway.
    Internal services communicate using gRPC.
    Redis stores sessions and distributes real-time updates using Pub/Sub.
    Kafka stores durable events for asynchronous processing.
    PostgreSQL stores the authoritative document data.
    The system must support 500,000 concurrent users.
    The architecture prioritizes low latency while requiring
    durable processing of important events.
    """,
]


graph = build_graph()


for i, architecture in enumerate(architectures, start=1):

    print("\n\n")
    print("############################################################")
    print(f"TEST CASE {i}")
    print("############################################################")

    print("\nARCHITECTURE:")
    print(architecture.strip())

    result = graph.invoke({
        "architecture": architecture
    })

    print("\n==============================")
    print("EXTRACTED CLAIMS")
    print("==============================")

    for claim in result.get("claims", []):
        print(f"\nClaim: {claim['claim']}")
        print(f"Category: {claim['category']}")
        print(f"Importance: {claim['importance']}")

    print("\n==============================")
    print("CLAIM ASSESSMENTS")
    print("==============================")

    for assessment in result.get("claim_assessments", []):
        print(f"\nClaim: {assessment['claim']}")
        print(f"Verdict: {assessment['verdict']}")
        print(f"Reasoning: {assessment['reasoning']}")

    print("\n==============================")
    print("FINAL REPORT")
    print("==============================")

    print(result.get("final_report", "No final report generated."))

