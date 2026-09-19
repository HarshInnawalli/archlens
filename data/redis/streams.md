# Redis Streams

```json metadata
{
  "schema_version": 2,
  "title": "Redis Streams",
  "description": "Introduction to Redis streams",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"performance","title":"Performance"},{"children":[{"id":"entry-ids","title":"Entry IDs"}],"id":"streams-basics","title":"Streams basics"},{"children":[{"id":"querying-by-range-xrange-and-xrevrange","title":"Querying by range: XRANGE and XREVRANGE"}],"id":"getting-data-from-streams","title":"Getting data from Streams"},{"id":"listening-for-new-items-with-xread","title":"Listening for new items with XREAD"},{"id":"consumer-groups","title":"Consumer groups"},{"id":"creating-a-consumer-group","title":"Creating a consumer group"},{"id":"recovering-from-permanent-failures","title":"Recovering from permanent failures"},{"id":"automatic-claiming","title":"Automatic claiming"},{"id":"claiming-and-the-delivery-counter","title":"Claiming and the delivery counter"},{"id":"releasing-messages-back-to-the-group-xnack","title":"Releasing messages back to the group: XNACK"},{"children":[{"id":"enhanced-deletion-control-in-redis-82","title":"Enhanced deletion control in Redis 8.2"}],"id":"working-with-multiple-consumer-groups","title":"Working with multiple consumer groups"},{"id":"streams-observability","title":"Streams observability"},{"id":"differences-with-kafka-tm-partitions","title":"Differences with Kafka (TM) partitions"},{"children":[{"id":"trimming-with-consumer-group-awareness","title":"Trimming with consumer group awareness"}],"id":"capped-streams","title":"Capped Streams"},{"id":"special-ids-in-the-streams-api","title":"Special IDs in the streams API"},{"id":"persistence-replication-and-message-safety","title":"Persistence, replication and message safety"},{"children":[{"id":"enhanced-deletion-with-xdelex","title":"Enhanced deletion with XDELEX"}],"id":"removing-single-items-from-a-stream","title":"Removing single items from a stream"},{"id":"zero-length-streams","title":"Zero length streams"},{"id":"total-latency-of-consuming-a-message","title":"Total latency of consuming a message"},{"id":"how-serving-blocked-consumers-works","title":"How serving blocked consumers works"},{"id":"latency-tests-results","title":"Latency tests results"},{"id":"learn-more","title":"Learn more"}]}

,
  "codeExamples": [{"codetabsId":"stream_tutorial-stepxadd","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"}],"description":"Foundational: Add entries to a stream using XADD with auto-generated IDs (creates new entries with field-value pairs)","difficulty":"beginner","id":"xadd","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxadd"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxadd"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxadd"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxadd"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxadd"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxadd"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxadd"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxadd"}]},{"codetabsId":"stream_tutorial-stepxrange","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Foundational: Retrieve stream entries within a range of IDs using XRANGE when you need to access historical data","difficulty":"beginner","id":"xrange","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange"}]},{"codetabsId":"stream_tutorial-stepxread_block","commands":[{"acl_categories":["@read","@stream","@slow","@blocking"],"name":"XREAD"}],"description":"Use XREAD with BLOCK to wait for new entries when you need to consume messages as they arrive","difficulty":"intermediate","id":"xread_block","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxread_block"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxread_block"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxread_block"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxread_block"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxread_block"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxread_block"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxread_block"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxread_block"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxread_block"}]},{"codetabsId":"stream_tutorial-stepxadd_2","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"}],"description":"Foundational: Add a single entry to a stream with multiple field-value pairs using XADD","difficulty":"beginner","id":"xadd_2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxadd_2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxadd_2"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxadd_2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxadd_2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxadd_2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxadd_2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxadd_2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxadd_2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxadd_2"}]},{"codetabsId":"stream_tutorial-stepxlen","commands":[{"acl_categories":["@read","@stream","@fast"],"complexity":"O(1)","name":"XLEN"}],"description":"Foundational: Get the total number of entries in a stream using XLEN","difficulty":"beginner","id":"xlen","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxlen"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxlen"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxlen"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxlen"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxlen"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxlen"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxlen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxlen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxlen"}]},{"codetabsId":"stream_tutorial-stepxadd_id","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"}],"description":"Specify explicit stream entry IDs instead of auto-generated ones when you need to use external system IDs","difficulty":"advanced","id":"xadd_id","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxadd_id"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxadd_id"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxadd_id"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxadd_id"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxadd_id"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxadd_id"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxadd_id"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxadd_id"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxadd_id"}]},{"codetabsId":"stream_tutorial-stepxadd_bad_id","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"}],"description":"Understand ID validation - XADD rejects IDs that are not monotonically increasing","difficulty":"advanced","id":"xadd_bad_id","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxadd_bad_id"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxadd_bad_id"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxadd_bad_id"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxadd_bad_id"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxadd_bad_id"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxadd_bad_id"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxadd_bad_id"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxadd_bad_id"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxadd_bad_id"}]},{"codetabsId":"stream_tutorial-stepxadd_7","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"}],"description":"Use partial explicit IDs with XADD to specify milliseconds while letting Redis auto-generate the sequence number","difficulty":"intermediate","id":"xadd_7","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxadd_7"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxadd_7"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxadd_7"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxadd_7"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxadd_7"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxadd_7"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxadd_7"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxadd_7"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxadd_7"}]},{"codetabsId":"stream_tutorial-stepxrange_all","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Foundational: Retrieve all entries in a stream using XRANGE with - and \u0026#43; special IDs","difficulty":"beginner","id":"xrange_all","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange_all"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange_all"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange_all"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange_all"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange_all"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange_all"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange_all"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange_all"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange_all"}]},{"codetabsId":"stream_tutorial-stepxrange_time","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Query stream entries by time range using millisecond timestamps instead of full IDs","difficulty":"intermediate","id":"xrange_time","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange_time"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange_time"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange_time"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange_time"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange_time"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange_time"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange_time"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange_time"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange_time"}]},{"codetabsId":"stream_tutorial-stepxrange_step_1","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Practical pattern: Paginate stream entries using XRANGE with COUNT to retrieve results in batches","difficulty":"intermediate","id":"xrange_step_1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange_step_1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange_step_1"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange_step_1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange_step_1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange_step_1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange_step_1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange_step_1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange_step_1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange_step_1"}]},{"codetabsId":"stream_tutorial-stepxrange_step_2","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Practical pattern: Continue pagination using exclusive range syntax with ( prefix to skip the last retrieved entry","difficulty":"intermediate","id":"xrange_step_2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange_step_2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange_step_2"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange_step_2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange_step_2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange_step_2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange_step_2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange_step_2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange_step_2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange_step_2"}]},{"codetabsId":"stream_tutorial-stepxrange_empty","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Practical pattern: Handle empty results when pagination reaches the end of the stream","difficulty":"intermediate","id":"xrange_empty","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange_empty"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange_empty"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange_empty"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange_empty"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange_empty"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange_empty"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange_empty"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange_empty"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange_empty"}]},{"codetabsId":"stream_tutorial-stepxrevrange","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XREVRANGE"}],"description":"Foundational: Retrieve stream entries in reverse order using XREVRANGE when you need the most recent entries first","difficulty":"beginner","id":"xrevrange","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrevrange"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrevrange"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrevrange"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrevrange"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrevrange"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrevrange"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrevrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrevrange"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrevrange"}]},{"codetabsId":"stream_tutorial-stepxread","commands":[{"acl_categories":["@read","@stream","@slow","@blocking"],"name":"XREAD"}],"description":"Foundational: Read entries from a stream starting from a specific ID using XREAD (non-blocking form)","difficulty":"beginner","id":"xread","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxread"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxread"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxread"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxread"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxread"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxread"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxread"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxread"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxread"}]},{"codetabsId":"stream_tutorial-stepxgroup_create","commands":[{"acl_categories":["@slow"],"complexity":"Depends on subcommand","name":"XGROUP"}],"description":"Foundational: Create a consumer group for a stream using XGROUP CREATE to enable coordinated message consumption","difficulty":"beginner","id":"xgroup_create","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxgroup_create"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxgroup_create"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxgroup_create"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxgroup_create"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxgroup_create"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxgroup_create"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxgroup_create"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxgroup_create"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxgroup_create"}]},{"codetabsId":"stream_tutorial-stepxgroup_create_mkstream","commands":[{"acl_categories":["@slow"],"complexity":"Depends on subcommand","name":"XGROUP"}],"description":"Create a consumer group and stream atomically using XGROUP CREATE with MKSTREAM option","difficulty":"intermediate","id":"xgroup_create_mkstream","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxgroup_create_mkstream"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxgroup_create_mkstream"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxgroup_create_mkstream"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxgroup_create_mkstream"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxgroup_create_mkstream"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxgroup_create_mkstream"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxgroup_create_mkstream"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxgroup_create_mkstream"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxgroup_create_mkstream"}]},{"codetabsId":"stream_tutorial-stepxgroup_read","description":"Foundational: Read new messages from a stream using a consumer group with XREADGROUP and the \u0026amp;gt; special ID","difficulty":"beginner","id":"xgroup_read","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxgroup_read"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxgroup_read"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxgroup_read"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxgroup_read"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxgroup_read"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxgroup_read"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxgroup_read"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxgroup_read"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxgroup_read"}]},{"codetabsId":"stream_tutorial-stepxgroup_read_id","commands":[{"acl_categories":["@write","@stream","@slow","@blocking"],"name":"XREADGROUP"}],"description":"Access pending message history using XREADGROUP with a specific ID to retrieve unacknowledged messages","difficulty":"intermediate","id":"xgroup_read_id","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxgroup_read_id"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxgroup_read_id"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxgroup_read_id"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxgroup_read_id"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxgroup_read_id"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxgroup_read_id"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxgroup_read_id"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxgroup_read_id"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxgroup_read_id"}]},{"codetabsId":"stream_tutorial-stepxack","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XACK"},{"acl_categories":["@write","@stream","@slow","@blocking"],"name":"XREADGROUP"}],"description":"Foundational: Acknowledge processed messages using XACK to mark them as handled by a consumer","difficulty":"beginner","id":"xack","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxack"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxack"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxack"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxack"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxack"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxack"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxack"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxack"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxack"}]},{"codetabsId":"stream_tutorial-stepxgroup_read_bob","commands":[{"acl_categories":["@write","@stream","@slow","@blocking"],"name":"XREADGROUP"}],"description":"Practical pattern: Demonstrate consumer group load balancing where different consumers receive different messages from the same stream","difficulty":"intermediate","id":"xgroup_read_bob","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxgroup_read_bob"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxgroup_read_bob"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxgroup_read_bob"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxgroup_read_bob"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxgroup_read_bob"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxgroup_read_bob"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxgroup_read_bob"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxgroup_read_bob"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxgroup_read_bob"}]},{"codetabsId":"stream_tutorial-stepxpending","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XPENDING"}],"description":"View pending message summary for a consumer group using XPENDING to monitor unacknowledged messages","difficulty":"intermediate","id":"xpending","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxpending"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxpending"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxpending"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxpending"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxpending"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxpending"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxpending"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxpending"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxpending"}]},{"codetabsId":"stream_tutorial-stepxpending_plus_minus","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XPENDING"}],"description":"Get detailed pending message information including idle time and delivery count using XPENDING with range","difficulty":"advanced","id":"xpending_plus_minus","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxpending_plus_minus"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxpending_plus_minus"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxpending_plus_minus"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxpending_plus_minus"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxpending_plus_minus"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxpending_plus_minus"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxpending_plus_minus"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxpending_plus_minus"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxpending_plus_minus"}]},{"codetabsId":"stream_tutorial-stepxrange_pending","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Retrieve the content of pending messages using XRANGE to inspect what needs to be processed","difficulty":"intermediate","id":"xrange_pending","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxrange_pending"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxrange_pending"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxrange_pending"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxrange_pending"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxrange_pending"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxrange_pending"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxrange_pending"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxrange_pending"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxrange_pending"}]},{"codetabsId":"stream_tutorial-stepxclaim","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(log N)","name":"XCLAIM"}],"description":"Claim pending messages from another consumer using XCLAIM when a consumer fails to process messages","difficulty":"advanced","id":"xclaim","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxclaim"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxclaim"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxclaim"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxclaim"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxclaim"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxclaim"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxclaim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxclaim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxclaim"}]},{"codetabsId":"stream_tutorial-stepxautoclaim","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XAUTOCLAIM"}],"description":"Practical pattern: Automatically claim idle pending messages using XAUTOCLAIM for simplified consumer failure recovery","difficulty":"advanced","id":"xautoclaim","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxautoclaim"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxautoclaim"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxautoclaim"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxautoclaim"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxautoclaim"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxautoclaim"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxautoclaim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxautoclaim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxautoclaim"}]},{"codetabsId":"stream_tutorial-stepxautoclaim_cursor","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XAUTOCLAIM"}],"description":"Continue automatic claiming using the cursor returned by XAUTOCLAIM to iterate through pending messages","difficulty":"advanced","id":"xautoclaim_cursor","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxautoclaim_cursor"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxautoclaim_cursor"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxautoclaim_cursor"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxautoclaim_cursor"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxautoclaim_cursor"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxautoclaim_cursor"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxautoclaim_cursor"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxautoclaim_cursor"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxautoclaim_cursor"}]},{"codetabsId":"stream_tutorial-stepxinfo","commands":[{"acl_categories":["@slow"],"complexity":"Depends on subcommand","name":"XINFO"}],"description":"Get detailed stream information including length, encoding, and consumer groups using XINFO STREAM","difficulty":"intermediate","id":"xinfo","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxinfo"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxinfo"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxinfo"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxinfo"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxinfo"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxinfo"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxinfo"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxinfo"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxinfo"}]},{"codetabsId":"stream_tutorial-stepxinfo_groups","commands":[{"acl_categories":["@slow"],"complexity":"Depends on subcommand","name":"XINFO"}],"description":"List all consumer groups for a stream using XINFO GROUPS to see group status and pending message counts","difficulty":"intermediate","id":"xinfo_groups","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxinfo_groups"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxinfo_groups"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxinfo_groups"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxinfo_groups"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxinfo_groups"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxinfo_groups"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxinfo_groups"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxinfo_groups"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxinfo_groups"}]},{"codetabsId":"stream_tutorial-stepxinfo_consumers","commands":[{"acl_categories":["@slow"],"complexity":"Depends on subcommand","name":"XINFO"}],"description":"Get detailed consumer information for a group using XINFO CONSUMERS to monitor individual consumer status","difficulty":"advanced","id":"xinfo_consumers","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxinfo_consumers"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxinfo_consumers"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxinfo_consumers"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxinfo_consumers"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxinfo_consumers"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxinfo_consumers"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxinfo_consumers"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxinfo_consumers"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxinfo_consumers"}]},{"codetabsId":"stream_tutorial-stepmaxlen","commands":[{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XADD"},{"acl_categories":["@read","@stream","@fast"],"complexity":"O(1)","name":"XLEN"},{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"}],"description":"Limit stream size using MAXLEN option with XADD to automatically evict old entries and maintain constant memory usage","difficulty":"intermediate","id":"maxlen","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepmaxlen"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepmaxlen"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepmaxlen"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepmaxlen"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepmaxlen"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepmaxlen"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepmaxlen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepmaxlen"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepmaxlen"}]},{"codetabsId":"stream_tutorial-stepxtrim","commands":[{"acl_categories":["@write","@stream","@slow"],"complexity":"O(N)","name":"XTRIM"}],"description":"Trim a stream to a maximum length using XTRIM MAXLEN to remove old entries","difficulty":"intermediate","id":"xtrim","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxtrim"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxtrim"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxtrim"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxtrim"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxtrim"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxtrim"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxtrim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxtrim"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxtrim"}]},{"codetabsId":"stream_tutorial-stepxtrim2","commands":[{"acl_categories":["@write","@stream","@slow"],"complexity":"O(N)","name":"XTRIM"}],"description":"Use approximate trimming with XTRIM MAXLEN ~ for more efficient memory management","difficulty":"intermediate","id":"xtrim2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxtrim2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxtrim2"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxtrim2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxtrim2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxtrim2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxtrim2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxtrim2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxtrim2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxtrim2"}]},{"codetabsId":"stream_tutorial-stepxdel","commands":[{"acl_categories":["@read","@stream","@slow"],"complexity":"O(N)","name":"XRANGE"},{"acl_categories":["@write","@stream","@fast"],"complexity":"O(1)","name":"XDEL"}],"description":"Delete specific entries from a stream by ID using XDEL for privacy or data cleanup purposes","difficulty":"advanced","id":"xdel","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_stream_tutorial-stepxdel"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_stream_tutorial-stepxdel"},{"id":"Node-js","panelId":"panel_Nodejs_stream_tutorial-stepxdel"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_stream_tutorial-stepxdel"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_stream_tutorial-stepxdel"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_stream_tutorial-stepxdel"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_stream_tutorial-stepxdel"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_stream_tutorial-stepxdel"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_stream_tutorial-stepxdel"}]}]
}
```

## Code Examples Legend

The code examples below show how to perform the same operations in different programming languages and client libraries:

- **Redis CLI**: Command-line interface for Redis
- **C# (Synchronous)**: StackExchange.Redis synchronous client
- **C# (Asynchronous)**: StackExchange.Redis asynchronous client
- **Go**: go-redis client
- **Java (Synchronous - Jedis)**: Jedis synchronous client
- **Java (Asynchronous - Lettuce)**: Lettuce asynchronous client
- **Java (Reactive - Lettuce)**: Lettuce reactive/streaming client
- **JavaScript (Node.js)**: node-redis client
- **PHP**: Predis client
- **Python**: redis-py client
- **Rust (Synchronous)**: redis-rs synchronous client
- **Rust (Asynchronous)**: redis-rs asynchronous client

Each code example demonstrates the same basic operation across different languages. The specific syntax and patterns vary based on the language and client library, but the underlying Redis commands and behavior remain consistent.

---


### Stream command summary

**30 commands in this group:**

[View all stream commands](https://redis.io/commands/?group=stream)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [XACK](https://redis.io/commands/xack/) | Returns the number of messages that were successfully acknowledged by the consumer group member of a stream. | O(1) for each message ID processed. | 5.0.0 |
| [XACKDEL](https://redis.io/commands/xackdel/) | Acknowledges and deletes one or multiple messages for a stream consumer group. | O(1) for each message ID processed. | 8.2.0 |
| [XADD](https://redis.io/commands/xadd/) | Appends a new message to a stream. Creates the key if it doesn't exist. | O(1) when adding a new entry, O(N) when trimmin... | 5.0.0 |
| [XAUTOCLAIM](https://redis.io/commands/xautoclaim/) | Changes, or acquires, ownership of messages in a consumer group, as if the messages were delivered to as consumer group member. | O(1) if COUNT is small. | 6.2.0 |
| [XCFGSET](https://redis.io/commands/xcfgset/) | Sets the IDMP configuration parameters for a stream. | O(1) | 8.6.0 |
| [XCLAIM](https://redis.io/commands/xclaim/) | Changes, or acquires, ownership of a message in a consumer group, as if the message was delivered a consumer group member. | O(log N) with N being the number of messages in... | 5.0.0 |
| [XDEL](https://redis.io/commands/xdel/) | Returns the number of messages after removing them from a stream. | O(1) for each single item to delete in the stre... | 5.0.0 |
| [XDELEX](https://redis.io/commands/xdelex/) | Deletes one or multiple entries from the stream. | O(1) for each single item to delete in the stre... | 8.2.0 |
| [XGROUP](https://redis.io/commands/xgroup/) | A container for consumer groups commands. | Depends on subcommand. | 5.0.0 |
| [XGROUP CREATE](https://redis.io/commands/xgroup-create/) | Creates a consumer group. | O(1) | 5.0.0 |

#### Stream command summary (part 2)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [XGROUP CREATECONSUMER](https://redis.io/commands/xgroup-createconsumer/) | Creates a consumer in a consumer group. | O(1) | 6.2.0 |
| [XGROUP DELCONSUMER](https://redis.io/commands/xgroup-delconsumer/) | Deletes a consumer from a consumer group. | O(1) | 5.0.0 |
| [XGROUP DESTROY](https://redis.io/commands/xgroup-destroy/) | Destroys a consumer group. | O(N) where N is the number of entries in the gr... | 5.0.0 |
| [XGROUP HELP](https://redis.io/commands/xgroup-help/) | Returns helpful text about the different subcommands. | O(1) | 5.0.0 |
| [XGROUP SETID](https://redis.io/commands/xgroup-setid/) | Sets the last-delivered ID of a consumer group. | O(1) | 5.0.0 |
| [XIDMPRECORD](https://redis.io/commands/xidmprecord/) | An internal command for setting IDMP metadata on an existing stream message. | O(1) | 8.6.2 |
| [XINFO](https://redis.io/commands/xinfo/) | A container for stream introspection commands. | Depends on subcommand. | 5.0.0 |
| [XINFO CONSUMERS](https://redis.io/commands/xinfo-consumers/) | Returns a list of the consumers in a consumer group. | O(1) | 5.0.0 |
| [XINFO GROUPS](https://redis.io/commands/xinfo-groups/) | Returns a list of the consumer groups of a stream. | O(1) | 5.0.0 |
| [XINFO HELP](https://redis.io/commands/xinfo-help/) | Returns helpful text about the different subcommands. | O(1) | 5.0.0 |

#### Stream command summary (part 3)

| Command | Summary | Complexity | Since |
|---------|---------|------------|-------|
| [XINFO STREAM](https://redis.io/commands/xinfo-stream/) | Returns information about a stream. | O(1) | 5.0.0 |
| [XLEN](https://redis.io/commands/xlen/) | Return the number of messages in a stream. | O(1) | 5.0.0 |
| [XNACK](https://redis.io/commands/xnack/) | Releases claimed messages back to the group's PEL without acknowledging them, making them available for re-delivery. | O(1) for each message ID processed. | 8.8.0 |
| [XPENDING](https://redis.io/commands/xpending/) | Returns the information and entries from a stream consumer group's pending entries list. | O(N) with N being the number of elements return... | 5.0.0 |
| [XRANGE](https://redis.io/commands/xrange/) | Returns the messages from a stream within a range of IDs. | O(N) with N being the number of elements being ... | 5.0.0 |
| [XREAD](https://redis.io/commands/xread/) | Returns messages from multiple streams with IDs greater than the ones requested. Blocks until a message is available otherwise. | N/A | 5.0.0 |
| [XREADGROUP](https://redis.io/commands/xreadgroup/) | Returns new or historical messages from a stream for a consumer in a group. Blocks until a message is available otherwise. | For each stream mentioned: O(M) with M being th... | 5.0.0 |
| [XREVRANGE](https://redis.io/commands/xrevrange/) | Returns the messages from a stream within a range of IDs in reverse order. | O(N) with N being the number of elements return... | 5.0.0 |
| [XSETID](https://redis.io/commands/xsetid/) | An internal command for replicating stream values. | O(1) | 5.0.0 |
| [XTRIM](https://redis.io/commands/xtrim/) | Deletes messages from the beginning of a stream. | O(N), with N being the number of evicted entrie... | 5.0.0 |



A Redis stream is a data structure that acts like an append-only log but also implements several operations to overcome some of the limits of a typical append-only log. These include random access in O(1) time and complex consumption strategies, such as consumer groups.
You can use streams to record and simultaneously syndicate events in real time.
Examples of Redis stream use cases include:

* Event sourcing (e.g., tracking user actions, clicks, etc.)
* Sensor monitoring (e.g., readings from devices in the field)
* Notifications (e.g., storing a record of each user's notifications in a separate stream)

Redis generates a unique ID for each stream entry.
You can use these IDs to retrieve their associated entries later or to read and process all subsequent entries in the stream. Note that because these IDs are related to time, the ones shown here may vary and will be different from the IDs you see in your own Redis instance.

Redis streams support several trimming strategies (to prevent streams from growing unbounded) and more than one consumption strategy (see [`XREAD`](https://redis.io/docs/latest/commands/xread), [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup), and [`XRANGE`](https://redis.io/docs/latest/commands/xrange)). Starting with Redis 8.2, the `XACKDEL`, `XDELEX`, `XADD`, and `XTRIM` commands provide fine-grained control over how stream operations interact with multiple consumer groups, simplifying the coordination of message processing across different applications.

Beginning with Redis 8.6, Redis streams support idempotent message processing (at-most-once production) to prevent duplicate entries when using at-least-once delivery patterns. This feature enables reliable message submission with automatic deduplication. See [Idempotent Message Processing](https://redis.io/docs/latest/develop/data-types/streams/idempotency) for more information.

## Examples

* When our racers pass a checkpoint, we add a stream entry for each racer that includes the racer's name, speed, position, and location ID:
Foundational: Add entries to a stream using XADD with auto-generated IDs (creates new entries with field-value pairs)

**Commands:** XADD

**Complexity:**
- XADD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD race:france * rider Castilla speed 30.2 position 1 location_id 1
"1692632086370-0"
> XADD race:france * rider Norem speed 28.8 position 3 location_id 1
"1692632094485-0"
> XADD race:france * rider Prickett speed 29.7 position 2 location_id 1
"1692632102976-0"
```

##### C#

```csharp
        RedisValue res1 = db.StreamAdd(
            "race:france",
            [
                new("rider", "Castilla"),
                new("speed", 30.2),
                new("position", 1),
                new("location_id", 1)
            ]
        );
        Console.WriteLine(res1);    // >>> 1712668482289-0

        RedisValue res2 = db.StreamAdd(
            "race:france",
            [
                new("rider", "Norem"),
                new("speed", 28.8),
                new("position", 3),
                new("location_id", 1)
            ]
        );
        Console.WriteLine(res2);    // >>> 1712668766534-1

        RedisValue res3 = db.StreamAdd(
            "race:france",
            [
                new("rider", "Prickett"),
                new("speed", 29.7),
                new("position", 2),
                new("location_id", 1)
            ]
        );
        Console.WriteLine(res3);    // >>> 1712669055705-0

```

##### Go

```go
	res1, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:france",
		Values: map[string]interface{}{
			"rider":       "Castilla",
			"speed":       30.2,
			"position":    1,
			"location_id": 1,
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res1) // >>> 1692632086370-0

	res2, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:france",
		Values: map[string]interface{}{
			"rider":       "Norem",
			"speed":       28.8,
			"position":    3,
			"location_id": 1,
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.PrintLn(res2) // >>> 1692632094485-0

	res3, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:france",
		Values: map[string]interface{}{
			"rider":       "Prickett",
			"speed":       29.7,
			"position":    2,
			"location_id": 1,
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res3) // >>> 1692632102976-0
```

##### Java (Synchronous - Jedis)

```java
    StreamEntryID res1 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Castilla");put("speed","30.2");put("position","1");put("location_id","1");}} , XAddParams.xAddParams());

    System.out.println(res1); // >>> 1701760582225-0

    StreamEntryID res2 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Norem");put("speed","28.8");put("position","3");put("location_id","1");}} , XAddParams.xAddParams());

    System.out.println(res2); // >>> 1701760582225-1

    StreamEntryID res3 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Prickett");put("speed","29.7");put("position","2");put("location_id","1");}} , XAddParams.xAddParams());

    System.out.println(res3); // >>> 1701760582226-0
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.xAdd(
  'race:france', '*', {
    'rider': 'Castilla',
    'speed': '30.2',
    'position': '1',
    'location_id': '1'
  }
);
console.log(res1); // >>> 1700073067968-0 N.B. actual values will differ from these examples

const res2 = await client.xAdd(
  'race:france', '*', {
    'rider': 'Norem',
    'speed': '28.8',
    'position': '3',
    'location_id': '1'
  },
);
console.log(res2); // >>> 1692629594113-0

const res3 = await client.xAdd(
  'race:france', '*', {
    'rider': 'Prickett',
    'speed': '29.7',
    'position': '2',
    'location_id': '1'
  },
);
console.log(res3); // >>> 1692629613374-0
```

##### Python

```python
res1 = r.xadd(
    "race:france",
    {"rider": "Castilla", "speed": 30.2, "position": 1, "location_id": 1},
)
print(res1)  # >>> 1692629576966-0

res2 = r.xadd(
    "race:france",
    {"rider": "Norem", "speed": 28.8, "position": 3, "location_id": 1},
)
print(res2)  # >>> 1692629594113-0

res3 = r.xadd(
    "race:france",
    {"rider": "Prickett", "speed": 29.7, "position": 2, "location_id": 1},
)
print(res3)  # >>> 1692629613374-0
```

##### Ruby

```ruby
res1 = r.xadd('race:france', {
  'rider' => 'Castilla',
  'speed' => 30.2,
  'position' => 1,
  'location_id' => 1
})
puts res1 # >>> 1692632086370-0, for example

res2 = r.xadd('race:france', {
  'rider' => 'Norem',
  'speed' => 28.8,
  'position' => 3,
  'location_id' => 1
})
puts res2 # >>> 1692632094485-0, for example

res3 = r.xadd('race:france', {
  'rider' => 'Prickett',
  'speed' => 29.7,
  'position' => 2,
  'location_id' => 1
})
puts res3 # >>> 1692632102976-0, for example
```

##### Rust (Asynchronous)

```rust
        let res1: Option<String> = r
            .xadd(
                "race:france",
                "*",
                &[
                    ("rider", "Castilla"),
                    ("speed", "30.2"),
                    ("position", "1"),
                    ("location_id", "1"),
                ],
            )
            .await
            .expect("xadd 1");
        let res1 = res1.expect("missing stream id");
        println!("{res1}"); // >>> 1692632086370-0

        let res2: Option<String> = r
            .xadd(
                "race:france",
                "*",
                &[
                    ("rider", "Norem"),
                    ("speed", "28.8"),
                    ("position", "3"),
                    ("location_id", "1"),
                ],
            )
            .await
            .expect("xadd 2");
        let res2 = res2.expect("missing stream id");
        println!("{res2}"); // >>> 1692632094485-0

        let res3: Option<String> = r
            .xadd(
                "race:france",
                "*",
                &[
                    ("rider", "Prickett"),
                    ("speed", "29.7"),
                    ("position", "2"),
                    ("location_id", "1"),
                ],
            )
            .await
            .expect("xadd 3");
        let res3 = res3.expect("missing stream id");
        println!("{res3}"); // >>> 1692632102976-0
```

##### Rust (Synchronous)

```rust
        let res1 = {
            let res: Option<String> = r
                .xadd(
                    "race:france",
                    "*",
                    &[
                        ("rider", "Castilla"),
                        ("speed", "30.2"),
                        ("position", "1"),
                        ("location_id", "1"),
                    ],
                )
                .expect("xadd 1");
            res.expect("missing stream id")
        };
        println!("{res1}"); // >>> 1692632086370-0

        let res2 = {
            let res: Option<String> = r
                .xadd(
                    "race:france",
                    "*",
                    &[
                        ("rider", "Norem"),
                        ("speed", "28.8"),
                        ("position", "3"),
                        ("location_id", "1"),
                    ],
                )
                .expect("xadd 2");
            res.expect("missing stream id")
        };
        println!("{res2}"); // >>> 1692632094485-0

        let res3 = {
            let res: Option<String> = r
                .xadd(
                    "race:france",
                    "*",
                    &[
                        ("rider", "Prickett"),
                        ("speed", "29.7"),
                        ("position", "2"),
                        ("location_id", "1"),
                    ],
                )
                .expect("xadd 3");
            res.expect("missing stream id")
        };
        println!("{res3}"); // >>> 1692632102976-0
```



* Read two stream entries starting at ID `1692632086370-0`:
Foundational: Retrieve stream entries within a range of IDs using XRANGE when you need to access historical data

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:france 1692632086370-0 + COUNT 2
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
2) 1) "1692632094485-0"
   2) 1) "rider"
      2) "Norem"
      3) "speed"
      4) "28.8"
      5) "position"
      6) "3"
      7) "location_id"
      8) "1"
```

##### C#

```csharp
        StreamEntry[] res4 = db.StreamRange("race:france", "1712668482289-0", "+", 2);

        foreach (StreamEntry entry in res4)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }

        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
```

##### Go

```go
	res4, err := rdb.XRangeN(ctx, "race:france", "1691765278160-0", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res4)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla...
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res4 = jedis.xrange("race:france","1701760582225-0","+",2);

    System.out.println(res4); // >>> [1701760841292-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701760841292-1 {rider=Norem, speed=28.8, location_id=1, position=3}]
```

##### JavaScript (Node.js)

```javascript
const res4 = await client.xRange('race:france', '1691765278160-0', '+', {COUNT: 2});
console.log(res4); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }]
```

##### Python

```python
res4 = r.xrange("race:france", "1691765278160-0", "+", 2)
print(
    res4
)  # >>> [
#   ('1692629576966-0',
#       {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#   ),
#   ('1692629594113-0',
#       {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#   )
# ]
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {
  'rider' => 'Castilla',
  'speed' => '30.2',
  'position' => '1',
  'location_id' => '1'
}, id: '1692632086370-0')
r.xadd('race:france', {
  'rider' => 'Norem',
  'speed' => '28.8',
  'position' => '3',
  'location_id' => '1'
}, id: '1692632094485-0')
r.xadd('race:france', {
  'rider' => 'Prickett',
  'speed' => '29.7',
  'position' => '2',
  'location_id' => '1'
}, id: '1692632102976-0')
r.xadd('race:france', {
  'rider' => 'Castilla',
  'speed' => '29.9',
  'position' => '1',
  'location_id' => '2'
}, id: '1692632147973-0')
res4 = r.xrange('race:france', '1692632086370-0', '+', count: 2)
puts res4.inspect
# >>> [["1692632086370-0", {"rider" => "Castilla", "speed" => "30.2", "position" => "1", "location_id" => "1"}],
#  ["1692632094485-0", {"rider" => "Norem", "speed" => "28.8", "position" => "3", "location_id" => "1"}]]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xrange_count("race:france", "1692632086370-0", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange_count("race:france", "1692632086370-0", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])]
        }
```



* Read up to 100 new stream entries, starting at the end of the stream, and block for up to 300 ms if no entries are being written:
Use XREAD with BLOCK to wait for new entries when you need to consume messages as they arrive

**Difficulty:** Intermediate

**Commands:** XREAD

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XREAD COUNT 100 BLOCK 300 STREAMS race:france $
(nil)
```

##### C#

```csharp
        StreamEntry[] res5 = db.StreamRead("race:france", 0, 100);

        foreach (StreamEntry entry in res4)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }

        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
        // >>> 1712669055705-0: [rider: Prickett, speed: 29.699999999999999, position: 2, location_id: 1]
```

##### Go

```go
	res5, err := rdb.XRead(ctx, &redis.XReadArgs{
		Streams: []string{"race:france", "0"},
		Count:   100,
		Block:   300,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res5)
	// >>> // [{race:france [{1692632086370-0 map[location_id:1 position:1...
```

##### Java (Synchronous - Jedis)

```java
    List<Map.Entry<String, List<StreamEntry>>> res5= jedis.xread(XReadParams.xReadParams().block(300).count(100),new HashMap<String,StreamEntryID>(){{put("race:france",new StreamEntryID());}});
    System.out.println(
      res5
    ); // >>> [race:france=[1701761996660-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701761996661-0 {rider=Norem, speed=28.8, location_id=1, position=3}, 1701761996661-1 {rider=Prickett, speed=29.7, location_id=1, position=2}]]
```

##### JavaScript (Node.js)

```javascript
const res5 = await client.xRead({
  key: 'race:france',
  id: '0-0'
}, {
  COUNT: 100,
  BLOCK: 300
});
console.log(res5); // >>> [{ name: 'race:france', messages: [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }, { id: '1692629613374-0', message: { rider: 'Prickett', speed: '29.7', position: '2', location_id: '1' } }] }]
```

##### Python

```python
res5 = r.xread(streams={"race:france": 0}, count=100, block=300)
print(
    res5
)
# >>> [
#   ['race:france',
#       [('1692629576966-0',
#           {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#       ),
#       ('1692629594113-0',
#           {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#       ),
#       ('1692629613374-0',
#           {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}
#       )]
# ]
# ]
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632086370-0')
res5 = r.xread(['race:france'], ['$'], count: 100, block: 300)
puts res5.inspect # >>> {}
```

##### Rust (Asynchronous)

```rust
        let opts = StreamReadOptions::default().count(100).block(300);
        if let Ok(res) = r.xread_options(&["race:france"], &["$"], &opts).await {
            let res: Option<StreamReadReply> = res;
            println!("{res:?}"); // >>> None
        }
```

##### Rust (Synchronous)

```rust
        let opts = StreamReadOptions::default().count(100).block(300);
        if let Ok(res) = r.xread_options(&["race:france"], &["$"], &opts) {
            let res: Option<StreamReadReply> = res;
            println!("{res:?}"); // >>> None
        }
```



## Performance

Adding an entry to a stream is O(1).
Accessing any single entry is O(n), where _n_ is the length of the ID.
Since stream IDs are typically short and of a fixed length, this effectively reduces to a constant time lookup.
For details on why, note that streams are implemented as [radix trees](https://en.wikipedia.org/wiki/Radix_tree).

Simply put, Redis streams provide highly efficient inserts and reads.
See each command's time complexity for the details.

## Streams basics

Streams are an append-only data structure. The fundamental write command, called [`XADD`](https://redis.io/docs/latest/commands/xadd), appends a new entry to the specified stream.

Each stream entry consists of one or more field-value pairs, somewhat like a dictionary or a Redis hash:

Foundational: Add a single entry to a stream with multiple field-value pairs using XADD

**Commands:** XADD

**Complexity:**
- XADD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD race:france * rider Castilla speed 29.9 position 1 location_id 2
"1692632147973-0"
```

##### C#

```csharp
        RedisValue res6 = db.StreamAdd(
            "race:france",
            [
                new("rider", "Castilla"),
                new("speed", 29.9),
                new("position", 1),
                new("location_id", 2)
            ]
        );

        Console.WriteLine(res6);    // >>> 1712675674750-0
```

##### Go

```go
	res6, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:france",
		Values: map[string]interface{}{
			"rider":       "Castilla",
			"speed":       29.9,
			"position":    1,
			"location_id": 2,
		},
	}).Result()

	if err != nil {
		panic(err)
	}

	//fmt.Println(res6) // >>> 1692632147973-0
```

##### Java (Synchronous - Jedis)

```java
    StreamEntryID res6 = jedis.xadd("race:france",new HashMap<String,String>(){{put("rider","Castilla");put("speed","29.9");put("position","2");put("location_id","1");}} , XAddParams.xAddParams());
    System.out.println(res6); // >>> 1701762285679-0
```

##### JavaScript (Node.js)

```javascript
const res6 = await client.xAdd(
  'race:france', '*', {
    'rider': 'Castilla',
    'speed': '29.9',
    'position': '1',
    'location_id': '2'
  }
);
console.log(res6); // >>> 1692629676124-0
```

##### Python

```python
res6 = r.xadd(
    "race:france",
    {"rider": "Castilla", "speed": 29.9, "position": 1, "location_id": 2},
)
print(res6)  # >>> 1692629676124-0
```

##### Ruby

```ruby
res6 = r.xadd('race:france', {
  'rider' => 'Castilla',
  'speed' => 29.9,
  'position' => 1,
  'location_id' => 2
})
puts res6 # >>> 1692632147973-0, for example
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .xadd(
                "race:france",
                "*",
                &[
                    ("rider", "Castilla"),
                    ("speed", "29.9"),
                    ("position", "1"),
                    ("location_id", "2"),
                ],
            )
            .await
        {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 1692632147973-0
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xadd(
            "race:france",
            "*",
            &[
                ("rider", "Castilla"),
                ("speed", "29.9"),
                ("position", "1"),
                ("location_id", "2"),
            ],
        ) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 1692632147973-0
        }
```



The above call to the [`XADD`](https://redis.io/docs/latest/commands/xadd) command adds an entry `rider: Castilla, speed: 29.9, position: 1, location_id: 2` to the stream at key `race:france`, using an auto-generated entry ID, which is the one returned by the command, specifically `1692632147973-0`. It gets as its first argument the key name `race:france`, the second argument is the entry ID that identifies every entry inside a stream. However, in this case, we passed `*` because we want the server to generate a new ID for us. Every new ID will be monotonically increasing, so in more simple terms, every new entry added will have a higher ID compared to all the past entries. Auto-generation of IDs by the server is almost always what you want, and the reasons for specifying an ID explicitly are very rare. We'll talk more about this later. The fact that each Stream entry has an ID is another similarity with log files, where line numbers, or the byte offset inside the file, can be used in order to identify a given entry. Returning back at our [`XADD`](https://redis.io/docs/latest/commands/xadd) example, after the key name and ID, the next arguments are the field-value pairs composing our stream entry.

It is possible to get the number of items inside a Stream just using the [`XLEN`](https://redis.io/docs/latest/commands/xlen) command:

Foundational: Get the total number of entries in a stream using XLEN

**Commands:** XLEN

**Complexity:**
- XLEN: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XLEN race:france
(integer) 4
```

##### C#

```csharp
        long res7 = db.StreamLength("race:france");
        Console.WriteLine(res7);    // >>> 4
```

##### Go

```go
	res7, err := rdb.XLen(ctx, "race:france").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res7) // >>> 4
```

##### Java (Synchronous - Jedis)

```java
    long res7 = jedis.xlen("race:france");
    System.out.println(res7); // >>> 4
```

##### JavaScript (Node.js)

```javascript
const res7 = await client.xLen('race:france');
console.log(res7); // >>> 4
```

##### Python

```python
res7 = r.xlen("race:france")
print(res7)  # >>> 4
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632147973-0')
res7 = r.xlen('race:france')
puts res7 # >>> 4
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xlen("race:france").await {
            let res: usize = res;
            println!("{res}"); // >>> 4
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xlen("race:france") {
            let res: usize = res;
            println!("{res}"); // >>> 4
        }
```



### Entry IDs

The entry ID returned by the [`XADD`](https://redis.io/docs/latest/commands/xadd) command, and identifying univocally each entry inside a given stream, is composed of two parts:

```
<millisecondsTime>-<sequenceNumber>
```

The milliseconds time part is actually the local time in the local Redis node generating the stream ID, however if the current milliseconds time happens to be smaller than the previous entry time, then the previous entry time is used instead, so if a clock jumps backward the monotonically incrementing ID property still holds. The sequence number is used for entries created in the same millisecond. Since the sequence number is 64 bit wide, in practical terms there is no limit to the number of entries that can be generated within the same millisecond.

The format of such IDs may look strange at first, and the gentle reader may wonder why the time is part of the ID. The reason is that Redis streams support range queries by ID. Because the ID is related to the time the entry is generated, this gives the ability to query for time ranges basically for free. We will see this soon while covering the [`XRANGE`](https://redis.io/docs/latest/commands/xrange) command.

If for some reason the user needs incremental IDs that are not related to time but are actually associated to another external system ID, as previously mentioned, the [`XADD`](https://redis.io/docs/latest/commands/xadd) command can take an explicit ID instead of the `*` wildcard ID that triggers auto-generation, like in the following examples:

Specify explicit stream entry IDs instead of auto-generated ones when you need to use external system IDs

**Difficulty:** Advanced

**Commands:** XADD

**Complexity:**
- XADD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD race:usa 0-1 racer Castilla
0-1
> XADD race:usa 0-2 racer Norem
0-2
```

##### C#

```csharp
        RedisValue res8 = db.StreamAdd(
            "race:usa",
            [
                new("racer", "Castilla")
            ],
            "0-1"
        );
        Console.WriteLine(res8);    // >>> 0-1

        RedisValue res9 = db.StreamAdd(
            "race:usa",
            [
                new("racer", "Norem")
            ],
            "0-2"
        );
        Console.WriteLine(res9);    // >>> 0-2
```

##### Go

```go
	res8, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:usa",
		Values: map[string]interface{}{
			"racer": "Castilla",
		},
		ID: "0-1",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res8) // >>> 0-1

	res9, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:usa",
		Values: map[string]interface{}{
			"racer": "Norem",
		},
		ID: "0-2",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res9) // >>> 0-2
```

##### Java (Synchronous - Jedis)

```java
    StreamEntryID res8 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Castilla");}},XAddParams.xAddParams().id("0-1"));
    System.out.println(res8); // >>> 0-1

    StreamEntryID res9 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Norem");}},XAddParams.xAddParams().id("0-2"));
    System.out.println(res9); // >>> 0-2
```

##### JavaScript (Node.js)

```javascript
const res8 = await client.xAdd('race:usa', '0-1', {
  'racer': 'Castilla'
});
console.log(res8); // >>> 0-1

const res9 = await client.xAdd('race:usa', '0-2', {
  'racer': 'Norem'
});
console.log(res9); // >>> 0-2
```

##### Python

```python
res8 = r.xadd("race:usa", {"racer": "Castilla"}, id="0-1")
print(res8)  # >>> 0-1

res9 = r.xadd("race:usa", {"racer": "Norem"}, id="0-2")
print(res9)  # >>> 0-2
```

##### Ruby

```ruby
r.del('race:usa')
res8 = r.xadd('race:usa', {'racer' => 'Castilla'}, id: '0-1')
puts res8 # >>> 0-1

res9 = r.xadd('race:usa', {'racer' => 'Norem'}, id: '0-2')
puts res9 # >>> 0-2
```

##### Rust (Asynchronous)

```rust
        delete_keys(&mut r, &["race:usa"]).await;
        if let Ok(res) = r.xadd("race:usa", "0-1", &[("racer", "Castilla")]).await {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-1
        }
        if let Ok(res) = r.xadd("race:usa", "0-2", &[("racer", "Norem")]).await {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-2
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xadd("race:usa", "0-1", &[("racer", "Castilla")]) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-1
        }

        if let Ok(res) = r.xadd("race:usa", "0-2", &[("racer", "Norem")]) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-2
        }
```



Note that in this case, the minimum ID is 0-1 and that the command will not accept an ID equal or smaller than a previous one:

Understand ID validation - XADD rejects IDs that are not monotonically increasing

**Difficulty:** Advanced

**Commands:** XADD

**Complexity:**
- XADD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD race:usa 0-1 racer Prickett
(error) ERR The ID specified in XADD is equal or smaller than the target stream top item
```

##### C#

```csharp
        try
        {
            RedisValue res10 = db.StreamAdd(
                "race:usa",
                [
                    new("racer", "Prickett")
                ],
                "0-1"
            );
        }
        catch (RedisServerException ex)
        {
            Console.WriteLine(ex);  // >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
        }
```

##### Go

```go
	res10, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Values: map[string]interface{}{
			"racer": "Prickett",
		},
		ID: "0-1",
	}).Result()

	if err != nil {
		// fmt.Println(err)
		// >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
	}
```

##### Java (Synchronous - Jedis)

```java
    try {
      StreamEntryID res10 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Prickett");}},XAddParams.xAddParams().id("0-1"));
      System.out.println(res10); // >>> 0-1
    }
    catch (JedisDataException e){
      System.out.println(e); // >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
    }
```

##### JavaScript (Node.js)

```javascript
try {
  const res10 = await client.xAdd('race:usa', '0-1', {
    'racer': 'Prickett'
  });
  console.log(res10); // >>> 0-1
} catch (error) {
  console.error(error); // >>> [SimpleError: ERR The ID specified in XADD is equal or smaller than the target stream top item]
}
```

##### Python

```python
try:
    res10 = r.xadd("race:usa", {"racer": "Prickett"}, id="0-1")
    print(res10)  # >>> 0-1
except redis.exceptions.ResponseError as e:
    print(e)  # >>> WRONGID
```

##### Ruby

```ruby
begin
  r.xadd('race:usa', {'racer' => 'Prickett'}, id: '0-1')
rescue Redis::CommandError => e
  puts e.message
  # >>> ERR The ID specified in XADD is equal or smaller than the target stream top item
end
```

##### Rust (Asynchronous)

```rust
        let res: redis::RedisResult<Option<String>> =
            r.xadd("race:usa", "0-1", &[("racer", "Prickett")]).await;
        match res {
            Ok(_) => {}
            Err(e) => {
                let msg = e.to_string();
                println!("{msg}");
                // >>> An error was signalled by the server - ResponseError: The ID specified in XADD is equal or smaller than the target stream top item
            }
        }
```

##### Rust (Synchronous)

```rust
        let res: redis::RedisResult<Option<String>> =
            r.xadd("race:usa", "0-1", &[("racer", "Prickett")]);
        match res {
            Ok(_) => {}
            Err(e) => {
                let msg = e.to_string();
                println!("{msg}");
                // >>> An error was signalled by the server - ResponseError: The ID specified in XADD is equal or smaller than the target stream top item
            }
        }
```



If you're running Redis 7 or later, you can also provide an explicit ID consisting of the milliseconds part only. In this case, the sequence portion of the ID will be automatically generated. To do this, use the syntax below:

Use partial explicit IDs with XADD to specify milliseconds while letting Redis auto-generate the sequence number

**Difficulty:** Intermediate

**Commands:** XADD

**Complexity:**
- XADD: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD race:usa 0-* racer Prickett
0-3
```

##### C#

```csharp
        RedisValue res11 = "";
        Version version = muxer.GetServer("localhost:6379").Version;
        if (version.Major >= 7)
        {
            res11 = db.StreamAdd(
                "race:usa",
                [
                    new("rider", "Norem")
                ],
                "0-*"
            );

            Console.WriteLine(res11);   // >>> "0-3"
        }
```

##### Go

```go
	res11, err := rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:usa",
		Values: map[string]interface{}{
			"racer": "Prickett",
		},
		ID: "0-*",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res11) // >>> 0-3
```

##### Java (Synchronous - Jedis)

```java
    StreamEntryID res11 = jedis.xadd("race:usa", new HashMap<String,String>(){{put("racer","Norem");}},XAddParams.xAddParams().id("0-*"));
    System.out.println(res11);
```

##### JavaScript (Node.js)

```javascript
const res11a = await client.xAdd('race:usa', '0-*', { racer: 'Norem' });
console.log(res11a); // >>> 0-3
```

##### Python

```python
# Not yet implemented
```

##### Ruby

```ruby
r.del('race:usa')
r.xadd('race:usa', {'racer' => 'Castilla'}, id: '0-1')
r.xadd('race:usa', {'racer' => 'Norem'}, id: '0-2')
res10 = r.xadd('race:usa', {'racer' => 'Prickett'}, id: '0-*')
puts res10 # >>> 0-3
```

##### Rust (Asynchronous)

```rust
        seed_usa_fixed(&mut r).await;
        if let Ok(res) = r.xadd("race:usa", "0-*", &[("racer", "Prickett")]).await {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-3
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xadd("race:usa", "0-*", &[("racer", "Prickett")]) {
            let res: Option<String> = res;
            let res = res.expect("missing stream id");
            println!("{res}"); // >>> 0-3
        }
```



## Getting data from Streams

Now we are finally able to append entries in our stream via [`XADD`](https://redis.io/docs/latest/commands/xadd). However, while appending data to a stream is quite obvious, the way streams can be queried in order to extract data is not so obvious. If we continue with the analogy of the log file, one obvious way is to mimic what we normally do with the Unix command `tail -f`, that is, we may start to listen in order to get the new messages that are appended to the stream. Note that unlike the blocking list operations of Redis, where a given element will reach a single client which is blocking in a *pop style* operation like [`BLPOP`](https://redis.io/docs/latest/commands/blpop), with streams we want multiple consumers to see the new messages appended to the stream (the same way many `tail -f` processes can see what is added to a log). Using the traditional terminology we want the streams to be able to *fan out* messages to multiple clients.

However, this is just one potential access mode. We could also see a stream in quite a different way: not as a messaging system, but as a *time series store*. In this case, maybe it's also useful to get the new messages appended, but another natural query mode is to get messages by ranges of time, or alternatively to iterate the messages using a cursor to incrementally check all the history. This is definitely another useful access mode.

Finally, if we see a stream from the point of view of consumers, we may want to access the stream in yet another way, that is, as a stream of messages that can be partitioned to multiple consumers that are processing such messages, so that groups of consumers can only see a subset of the messages arriving in a single stream. In this way, it is possible to scale the message processing across different consumers, without single consumers having to process all the messages: each consumer will just get different messages to process. This is basically what Kafka (TM) does with consumer groups. Reading messages via consumer groups is yet another interesting mode of reading from a Redis Stream.

Redis Streams support all three of the query modes described above via different commands. The next sections will show them all, starting from the simplest and most direct to use: range queries.

### Querying by range: XRANGE and XREVRANGE

To query the stream by range we are only required to specify two IDs, *start* and *end*. The range returned will include the elements having start or end as ID, so the range is inclusive. The two special IDs `-` and `+` respectively mean the smallest and the greatest ID possible.

Foundational: Retrieve all entries in a stream using XRANGE with - and + special IDs

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:france - +
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
... output truncated for AI-facing Markdown ...
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```

##### C#

```csharp
        StreamEntry[] res12 = db.StreamRange("race:france", "-", "+");

        foreach (StreamEntry entry in res12)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
        // >>> 1712669055705-0: [rider: Prickett, speed: 29.699999999999999, position: 2, location_id: 1]
        // >>> 1712675674750-0: [rider: Castilla, speed: 29.899999999999999, position: 1, location_id: 2]
```

##### Go

```go
	res12, err := rdb.XRange(ctx, "race:france", "-", "+").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res12)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla...
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res12 = jedis.xrange("race:france","-","+");
    System.out.println(
      res12
    ); // >>> [1701764734160-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764734160-1 {rider=Norem, speed=28.8, location_id=1, position=3}, 1701764734161-0 {rider=Prickett, speed=29.7, location_id=1, position=2}, 1701764734162-0 {rider=Castilla, speed=29.9, location_id=1, position=2}]
```

##### JavaScript (Node.js)

```javascript
const res11 = await client.xRange('race:france', '-', '+');
console.log(res11); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }, { id: '1692629613374-0', message: { rider: 'Prickett', speed: '29.7', position: '2', location_id: '1' } }, { id: '1692629676124-0', message: { rider: 'Castilla', speed: '29.9', position: '1', location_id: '2' } }]
```

##### Python

```python
res11 = r.xrange("race:france", "-", "+")
print(
    res11
)
# >>> [
#   ('1692629576966-0',
#       {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#   ),
#   ('1692629594113-0',
#       {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#   ),
#   ('1692629613374-0',
#       {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}
#   ),
#   ('1692629676124-0',
#       {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'}
#   )
# ]
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2'}, id: '1692632147973-0')
res11 = r.xrange('race:france', '-', '+')
puts res11.inspect
# >>> [["1692632086370-0", {"rider" => "Castilla", "speed" => "30.2", "position" => "1", "location_id" => "1"}],
#  ["1692632094485-0", {"rider" => "Norem", "speed" => "28.8", "position" => "3", "location_id" => "1"}],
#  ["1692632102976-0", {"rider" => "Prickett", "speed" => "29.7", "position" => "2", "location_id" => "1"}],
#  ["1692632147973-0", {"rider" => "Castilla", "speed" => "29.9", "position" => "1", "location_id" => "2"}]]
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_all("race:france").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")]), ("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange_all("race:france") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")]), ("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```



Each entry returned is an array of two items: the ID and the list of field-value pairs. We already said that the entry IDs have a relation with the time, because the part at the left of the `-` character is the Unix time in milliseconds of the local node that created the stream entry, at the moment the entry was created (however note that streams are replicated with fully specified [`XADD`](https://redis.io/docs/latest/commands/xadd) commands, so the replicas will have identical IDs to the master). This means that I could query a range of time using [`XRANGE`](https://redis.io/docs/latest/commands/xrange). In order to do so, however, I may want to omit the sequence part of the ID: if omitted, in the start of the range it will be assumed to be 0, while in the end part it will be assumed to be the maximum sequence number available. This way, querying using just two milliseconds Unix times, we get all the entries that were generated in that range of time, in an inclusive way. For instance, if I want to query a two milliseconds period I could use:

Query stream entries by time range using millisecond timestamps instead of full IDs

**Difficulty:** Intermediate

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:france 1692632086369 1692632086371
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
```

##### C#

```csharp
        StreamEntry[] res13 = db.StreamRange("race:france", 1712668482289, 1712668482291);

        foreach (StreamEntry entry in res13)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
```

##### Go

```go
	res13, err := rdb.XRange(ctx, "race:france",
		"1692632086369", "1692632086371",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res13)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla speed:30.2] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res13 = jedis.xrange("race:france",String.valueOf(System.currentTimeMillis()-1000),String.valueOf(System.currentTimeMillis()+1000));
    System.out.println(
      res13
    ); // >>> [1701764734160-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764734160-1 {rider=Norem, speed=28.8, location_id=1, position=3}, 1701764734161-0 {rider=Prickett, speed=29.7, location_id=1, position=2}, 1701764734162-0 {rider=Castilla, speed=29.9, location_id=1, position=2}]
```

##### JavaScript (Node.js)

```javascript
const res12 = await client.xRange('race:france', '1692629576965', '1692629576967');
console.log(res12); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }]
```

##### Python

```python
res12 = r.xrange("race:france", 1692629576965, 1692629576967)
print(
    res12
)
# >>> [
#       ('1692629576966-0',
#           {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#       )
# ]
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
res12 = r.xrange('race:france', '1692632086369', '1692632086371')
puts res12.inspect
# >>> [["1692632086370-0", {"rider" => "Castilla", "speed" => "30.2", "position" => "1", "location_id" => "1"}]]
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange("race:france", "1692632086369", "1692632086371").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange("race:france", "1692632086369", "1692632086371") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")])]
        }
```



I have only a single entry in this range. However in real data sets, I could query for ranges of hours, or there could be many items in just two milliseconds, and the result returned could be huge. For this reason, [`XRANGE`](https://redis.io/docs/latest/commands/xrange) supports an optional **COUNT** option at the end. By specifying a count, I can just get the first *N* items. If I want more, I can get the last ID returned, increment the sequence part by one, and query again. Let's see this in the following example. Let's assume that the stream `race:france` was populated with 4 items. To start my iteration, getting 2 items per command, I start with the full range, but with a count of 2.

Practical pattern: Paginate stream entries using XRANGE with COUNT to retrieve results in batches

**Difficulty:** Intermediate

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:france - + COUNT 2
1) 1) "1692632086370-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "30.2"
      5) "position"
      6) "1"
      7) "location_id"
      8) "1"
2) 1) "1692632094485-0"
   2) 1) "rider"
      2) "Norem"
      3) "speed"
      4) "28.8"
      5) "position"
      6) "3"
      7) "location_id"
      8) "1"
```

##### C#

```csharp
        StreamEntry[] res14 = db.StreamRange("race:france", "-", "+", 2);

        foreach (StreamEntry entry in res14)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
```

##### Go

```go
	res14, err := rdb.XRangeN(ctx, "race:france", "-", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res14)
	// >>> [{1692632086370-0 map[location_id:1 position:1 rider:Castilla speed:30.2] 0 0} {1692632094485-0 map[location_id:1 position:3 rider:Norem speed:28.8] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res14 = jedis.xrange("race:france","-","+",2);
    System.out.println(res14); // >>> [1701764887638-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764887638-1 {rider=Norem, speed=28.8, location_id=1, position=3}]
```

##### JavaScript (Node.js)

```javascript
const res13 = await client.xRange('race:france', '-', '+', {COUNT: 2});
console.log(res13); // >>> [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }]
```

##### Python

```python
res13 = r.xrange("race:france", "-", "+", 2)
print(
    res13
)
# >>> [
#   ('1692629576966-0',
#       {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#   ),
#   ('1692629594113-0',
#       {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#   )
# ]
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2'}, id: '1692632147973-0')
res13 = r.xrange('race:france', '-', '+', count: 2)
puts res13.inspect
# >>> [["1692632086370-0", {"rider" => "Castilla", "speed" => "30.2", "position" => "1", "location_id" => "1"}],
#  ["1692632094485-0", {"rider" => "Norem", "speed" => "28.8", "position" => "3", "location_id" => "1"}]]
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_count("race:france", "-", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange_count("race:france", "-", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])]
        }
```



To continue the iteration with the next two items, I have to pick the last ID returned, that is `1692632094485-0`, and add the prefix `(` to it. The resulting exclusive range interval, that is `(1692632094485-0` in this case, can now be used as the new *start* argument for the next [`XRANGE`](https://redis.io/docs/latest/commands/xrange) call:

Practical pattern: Continue pagination using exclusive range syntax with ( prefix to skip the last retrieved entry

**Difficulty:** Intermediate

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:france (1692632094485-0 + COUNT 2
1) 1) "1692632102976-0"
   2) 1) "rider"
      2) "Prickett"
      3) "speed"
      4) "29.7"
      5) "position"
      6) "2"
      7) "location_id"
      8) "1"
2) 1) "1692632147973-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```

##### C#

```csharp
        StreamEntry[] res15 = db.StreamRange("race:france", "(1712668766534-1", "+", 2);

        foreach (StreamEntry entry in res15)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712669055705-0: [rider: Prickett, speed: 29.699999999999999, position: 2, location_id: 1]
        // >>> 1712675674750-0: [rider: Castilla, speed: 29.899999999999999, position: 1, location_id: 2]
```

##### Go

```go
	res15, err := rdb.XRangeN(ctx, "race:france",
		"(1692632094485-0", "+", 2,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res15)
	// >>> [{1692632102976-0 map[location_id:1 position:2 rider:Prickett speed:29.7] 0 0} {1692632147973-0 map[location_id:2 position:1 rider:Castilla speed:29.9] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res15 = jedis.xrange("race:france",String.valueOf(System.currentTimeMillis()-1000)+"-0","+",2);
    System.out.println(res15); // >>> [1701764887638-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701764887638-1 {rider=Norem, speed=28.8, location_id=1, position=3}]
```

##### JavaScript (Node.js)

```javascript
const res14 = await client.xRange('race:france', '(1692629594113-0', '+', {COUNT: 2});
console.log(res14); // >>> [{ id: '1692629613374-0', message: { rider: 'Prickett', speed: '29.7', position: '2', location_id: '1' } }, { id: '1692629676124-0', message: { rider: 'Castilla', speed: '29.9', position: '1', location_id: '2' } }]
```

##### Python

```python
res14 = r.xrange("race:france", "(1692629594113-0", "+", 2)
print(
    res14
)
# >>> [
#   ('1692629613374-0',
#       {'rider': 'Prickett', 'speed': '29.7', 'position': '2', 'location_id': '1'}
#   ),
#   ('1692629676124-0',
#       {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'}
#   )
# ]
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '30.2', 'position' => '1', 'location_id' => '1'}, id: '1692632086370-0')
r.xadd('race:france', {'rider' => 'Norem', 'speed' => '28.8', 'position' => '3', 'location_id' => '1'}, id: '1692632094485-0')
r.xadd('race:france', {'rider' => 'Prickett', 'speed' => '29.7', 'position' => '2', 'location_id' => '1'}, id: '1692632102976-0')
r.xadd('race:france', {'rider' => 'Castilla', 'speed' => '29.9', 'position' => '1', 'location_id' => '2'}, id: '1692632147973-0')
res14 = r.xrange('race:france', '(1692632094485-0', '+', count: 2)
puts res14.inspect
# >>> [["1692632102976-0", {"rider" => "Prickett", "speed" => "29.7", "position" => "2", "location_id" => "1"}],
#  ["1692632147973-0", {"rider" => "Castilla", "speed" => "29.9", "position" => "1", "location_id" => "2"}]]
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_count("race:france", "(1692632094485-0", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange_count("race:france", "(1692632094485-0", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632102976-0", [("rider", "Prickett"), ("speed", "29.7"), ("position", "2"), ("location_id", "1")]), ("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```



Now that we've retrieved 4 items out of a stream that only had 4 entries in it, if we try to retrieve more items, we'll get an empty array:

Practical pattern: Handle empty results when pagination reaches the end of the stream

**Difficulty:** Intermediate

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:france (1692632147973-0 + COUNT 2
(empty array)
```

##### C#

```csharp
        StreamEntry[] res16 = db.StreamRange("race:france", "(1712675674750-0", "+", 2);

        foreach (StreamEntry entry in res16)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> <empty array>
```

##### Go

```go
	res16, err := rdb.XRangeN(ctx, "race:france",
		"(1692632147973-0", "+", 2,
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res16)
	// >>> []
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res16 = jedis.xrange("race:france",String.valueOf(System.currentTimeMillis()+1000)+"-0","+",2);
    System.out.println(res16); // >>> []
```

##### JavaScript (Node.js)

```javascript
const res15 = await client.xRange('race:france', '(1692629676124-0', '+', {COUNT: 2});
console.log(res15); // >>> []
```

##### Python

```python
res15 = r.xrange("race:france", "(1692629676124-0", "+", 2)
print(res15)  # >>> []
```

##### Ruby

```ruby
res15 = r.xrange('race:france', '(1692632147973-0', '+', count: 2)
puts res15.inspect # >>> []
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrange_count("race:france", "(1692632147973-0", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> []
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange_count("race:france", "(1692632147973-0", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> []
        }
```



Since [`XRANGE`](https://redis.io/docs/latest/commands/xrange) complexity is *O(log(N))* to seek, and then *O(M)* to return M elements, with a small count the command has a logarithmic time complexity, which means that each step of the iteration is fast. So [`XRANGE`](https://redis.io/docs/latest/commands/xrange) is also the de facto *streams iterator* and does not require an **XSCAN** command.

The command [`XREVRANGE`](https://redis.io/docs/latest/commands/xrevrange) is the equivalent of [`XRANGE`](https://redis.io/docs/latest/commands/xrange) but returning the elements in inverted order, so a practical use for [`XREVRANGE`](https://redis.io/docs/latest/commands/xrevrange) is to check what is the last item in a Stream:

Foundational: Retrieve stream entries in reverse order using XREVRANGE when you need the most recent entries first

**Commands:** XREVRANGE

**Complexity:**
- XREVRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XREVRANGE race:france + - COUNT 1
1) 1) "1692632147973-0"
   2) 1) "rider"
      2) "Castilla"
      3) "speed"
      4) "29.9"
      5) "position"
      6) "1"
      7) "location_id"
      8) "2"
```

##### C#

```csharp
        StreamEntry[] res17 = db.StreamRange("race:france", "+", "-", 1, Order.Descending);

        foreach (StreamEntry entry in res17)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712675674750-0: [rider: Castilla, speed: 29.899999999999999, position: 1, location_id: 2]
```

##### Go

```go
	res17, err := rdb.XRevRangeN(ctx, "race:france", "+", "-", 1).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res17)
	// >>> [{1692632147973-0 map[location_id:2 position:1 rider:Castilla speed:29.9] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res17 = jedis.xrevrange("race:france","+","-",1);
    System.out.println(res17); // >>> [1701765218592-0 {rider=Castilla, speed=29.9, location_id=1, position=2}]
```

##### JavaScript (Node.js)

```javascript
const res16 = await client.xRevRange('race:france', '+', '-', {COUNT: 1});
console.log(
  res16
); // >>> [{ id: '1692629676124-0', message: { rider: 'Castilla', speed: '29.9', position: '1', location_id: '2' } }]
```

##### Python

```python
res16 = r.xrevrange("race:france", "+", "-", 1)
print(
    res16
)
# >>> [
#       ('1692629676124-0',
#           {'rider': 'Castilla', 'speed': '29.9', 'position': '1', 'location_id': '2'}
#       )
# ]
```

##### Ruby

```ruby
res16 = r.xrevrange('race:france', '+', '-', count: 1)
puts res16.inspect
# >>> [["1692632147973-0", {"rider" => "Castilla", "speed" => "29.9", "position" => "1", "location_id" => "2"}]]
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xrevrange_count("race:france", "+", "-", 1).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrevrange_count("race:france", "+", "-", 1) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![
                            ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                            ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                            ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                            (
                                "location_id".to_string(),
                                entry.get::<String>("location_id").expect("missing location_id"),
                            ),
                        ],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632147973-0", [("rider", "Castilla"), ("speed", "29.9"), ("position", "1"), ("location_id", "2")])]
        }
```



Note that the [`XREVRANGE`](https://redis.io/docs/latest/commands/xrevrange) command takes the *start* and *stop* arguments in reverse order.

## Listening for new items with XREAD

When we do not want to access items by a range in a stream, usually what we want instead is to *subscribe* to new items arriving to the stream. This concept may appear related to Redis Pub/Sub, where you subscribe to a channel, or to Redis blocking lists, where you wait for a key to get new elements to fetch, but there are fundamental differences in the way you consume a stream:

1. A stream can have multiple clients (consumers) waiting for data. Every new item, by default, will be delivered to *every consumer* that is waiting for data in a given stream. This behavior is different than blocking lists, where each consumer will get a different element. However, the ability to *fan out* to multiple consumers is similar to Pub/Sub.
2. While in Pub/Sub messages are *fire and forget* and are never stored anyway, and while when using blocking lists, when a message is received by the client it is *popped* (effectively removed) from the list, streams work in a fundamentally different way. All the messages are appended in the stream indefinitely (unless the user explicitly asks to delete entries): different consumers will know what is a new message from its point of view by remembering the ID of the last message received.
3. Streams Consumer Groups provide a level of control that Pub/Sub or blocking lists cannot achieve, with different groups for the same stream, explicit acknowledgment of processed items, ability to inspect the pending items, claiming of unprocessed messages, and coherent history visibility for each single client, that is only able to see its private past history of messages.

The command that provides the ability to listen for new messages arriving into a stream is called [`XREAD`](https://redis.io/docs/latest/commands/xread). It's a bit more complex than [`XRANGE`](https://redis.io/docs/latest/commands/xrange), so we'll start showing simple forms, and later the whole command layout will be provided.

Foundational: Read entries from a stream starting from a specific ID using XREAD (non-blocking form)

**Commands:** XREAD

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XREAD COUNT 2 STREAMS race:france 0
1) 1) "race:france"
   2) 1) 1) "1692632086370-0"
         2) 1) "rider"
            2) "Castilla"
            3) "speed"
            4) "30.2"
            5) "position"
            6) "1"
            7) "location_id"
... output truncated for AI-facing Markdown ...
         2) 1) "rider"
            2) "Norem"
            3) "speed"
            4) "28.8"
            5) "position"
            6) "3"
            7) "location_id"
            8) "1"
```

##### C#

```csharp
        StreamEntry[] res18 = db.StreamRead("race:france", 0, 2);

        foreach (StreamEntry entry in res18)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712668482289-0: [rider: Castilla, speed: 30.199999999999999, position: 1, location_id: 1]
        // >>> 1712668766534-1: [rider: Norem, speed: 28.800000000000001, position: 3, location_id: 1]
```

##### Go

```go
	res18, err := rdb.XRead(ctx, &redis.XReadArgs{
		Streams: []string{"race:france", "0"},
		Count:   2,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res18)
	// >>> [{race:france [{1692632086370-0 map[location_id:1 position:1 rider:Castilla speed:30.2] 0 0} {1692632094485-0 map[location_id:1 position:3 rider:Norem speed:28.8] 0 0}]}]
```

##### Java (Synchronous - Jedis)

```java
    List<Map.Entry<String, List<StreamEntry>>> res18= jedis.xread(XReadParams.xReadParams().count(2),new HashMap<String,StreamEntryID>(){{put("race:france",new StreamEntryID());}});
    System.out.println(
      res18
    ); // >>> [race:france=[1701765384638-0 {rider=Castilla, speed=30.2, location_id=1, position=1}, 1701765384638-1 {rider=Norem, speed=28.8, location_id=1, position=3}]]
```

##### JavaScript (Node.js)

```javascript
const res17 = await client.xRead({
  key: 'race:france',
  id: '0-0'
}, {
  COUNT: 2
});
console.log(res17); // >>> [{ name: 'race:france', messages: [{ id: '1692629576966-0', message: { rider: 'Castilla', speed: '30.2', position: '1', location_id: '1' } }, { id: '1692629594113-0', message: { rider: 'Norem', speed: '28.8', position: '3', location_id: '1' } }] }]
```

##### Python

```python
res17 = r.xread(streams={"race:france": 0}, count=2)
print(
    res17
)
# >>> [
#       ['race:france', [
#       ('1692629576966-0',
#           {'rider': 'Castilla', 'speed': '30.2', 'position': '1', 'location_id': '1'}
#       ),
#       ('1692629594113-0',
#           {'rider': 'Norem', 'speed': '28.8', 'position': '3', 'location_id': '1'}
#       )
#       ]
#       ]
#   ]
```

##### Ruby

```ruby
res17 = r.xread(['race:france'], ['0'], count: 2)
puts res17.inspect
# >>> {"race:france"=>[["1692632086370-0", {"rider" => "Castilla", "speed" => "30.2", "position" => "1", "location_id" => "1"}],
#                  ["1692632094485-0", {"rider" => "Norem", "speed" => "28.8", "position" => "3", "location_id" => "1"}]]}
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        let opts = StreamReadOptions::default().count(2);
        if let Ok(res) = r.xread_options(&["race:france"], &["0"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xread should return data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![
                                        ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                                        ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                                        ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                                        (
                                            "location_id".to_string(),
                                            entry.get::<String>("location_id").expect("missing location_id"),
                                        ),
                                    ],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:france", [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])])]
        }
```

##### Rust (Synchronous)

```rust
        let opts = StreamReadOptions::default().count(2);
        if let Ok(res) = r.xread_options(&["race:france"], &["0"], &opts) {
            let res: Option<StreamReadReply> = res;
            let reply = res.expect("xread should return data");
            let view: Vec<_> = reply
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![
                                        ("rider".to_string(), entry.get::<String>("rider").expect("missing rider")),
                                        ("speed".to_string(), entry.get::<String>("speed").expect("missing speed")),
                                        ("position".to_string(), entry.get::<String>("position").expect("missing position")),
                                        (
                                            "location_id".to_string(),
                                            entry.get::<String>("location_id").expect("missing location_id"),
                                        ),
                                    ],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:france", [("1692632086370-0", [("rider", "Castilla"), ("speed", "30.2"), ("position", "1"), ("location_id", "1")]), ("1692632094485-0", [("rider", "Norem"), ("speed", "28.8"), ("position", "3"), ("location_id", "1")])])]
        }
```



The above is the non-blocking form of [`XREAD`](https://redis.io/docs/latest/commands/xread). Note that the **COUNT** option is not mandatory, in fact the only mandatory option of the command is the **STREAMS** option, that specifies a list of keys together with the corresponding maximum ID already seen for each stream by the calling consumer, so that the command will provide the client only with messages with an ID greater than the one we specified.

In the above command we wrote `STREAMS race:france 0` so we want all the messages in the Stream `race:france` having an ID greater than `0-0`. As you can see in the example above, the command returns the key name, because actually it is possible to call this command with more than one key to read from different streams at the same time. I could write, for instance: `STREAMS race:france race:italy 0 0`. Note how after the **STREAMS** option we need to provide the key names, and later the IDs. For this reason, the **STREAMS** option must always be the last option.
Any other options must come before the **STREAMS** option.

Apart from the fact that [`XREAD`](https://redis.io/docs/latest/commands/xread) can access multiple streams at once, and that we are able to specify the last ID we own to just get newer messages, in this simple form the command is not doing something so different compared to [`XRANGE`](https://redis.io/docs/latest/commands/xrange). However, the interesting part is that we can turn [`XREAD`](https://redis.io/docs/latest/commands/xread) into a *blocking command* easily, by specifying the **BLOCK** argument:

```
> XREAD BLOCK 0 STREAMS race:france $
```

Note that in the example above, other than removing **COUNT**, I specified the new **BLOCK** option with a timeout of 0 milliseconds (that means to never timeout). Moreover, instead of passing a normal ID for the stream `race:france` I passed the special ID `$`. This special ID means that [`XREAD`](https://redis.io/docs/latest/commands/xread) should use as last ID the maximum ID already stored in the stream `race:france`, so that we will receive only *new* messages, starting from the time we started listening. This is similar to the `tail -f` Unix command in some way.

Note that when the **BLOCK** option is used, we do not have to use the special ID `$`. We can use any valid ID. If the command is able to serve our request immediately without blocking, it will do so, otherwise it will block. Normally if we want to consume the stream starting from new entries, we start with the ID `$`, and after that we continue using the ID of the last message received to make the next call, and so forth.

The blocking form of [`XREAD`](https://redis.io/docs/latest/commands/xread) is also able to listen to multiple Streams, just by specifying multiple key names. If the request can be served synchronously because there is at least one stream with elements greater than the corresponding ID we specified, it returns with the results. Otherwise, the command will block and will return the items of the first stream which gets new data (according to the specified ID).

Similarly to blocking list operations, blocking stream reads are *fair* from the point of view of clients waiting for data, since the semantics is FIFO style. The first client that blocked for a given stream will be the first to be unblocked when new items are available.

[`XREAD`](https://redis.io/docs/latest/commands/xread) has no other options than **COUNT** and **BLOCK**, so it's a pretty basic command with a specific purpose to attach consumers to one or multiple streams. More powerful features to consume streams are available using the consumer groups API, however reading via consumer groups is implemented by a different command called [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup), covered in the next section of this guide.

## Consumer groups

When the task at hand is to consume the same stream from different clients, then [`XREAD`](https://redis.io/docs/latest/commands/xread) already offers a way to *fan-out* to N clients, potentially also using replicas in order to provide more read scalability. However in certain problems what we want to do is not to provide the same stream of messages to many clients, but to provide a *different subset* of messages from the same stream to many clients. An obvious case where this is useful is that of messages which are slow to process: the ability to have N different workers that will receive different parts of the stream allows us to scale message processing, by routing different messages to different workers that are ready to do more work.

In practical terms, if we imagine having three consumers C1, C2, C3, and a stream that contains the messages 1, 2, 3, 4, 5, 6, 7 then what we want is to serve the messages according to the following diagram:

```
1 -> C1
2 -> C2
3 -> C3
4 -> C1
5 -> C2
6 -> C3
7 -> C1
```

In order to achieve this, Redis uses a concept called *consumer groups*. It is very important to understand that Redis consumer groups have nothing to do, from an implementation standpoint, with Kafka (TM) consumer groups. Yet they are similar in functionality, so I decided to keep Kafka's (TM) terminology, as it originally popularized this idea.

A consumer group is like a *pseudo consumer* that gets data from a stream, and actually serves multiple consumers, providing certain guarantees:

1. Each message is served to a different consumer so that it is not possible that the same message will be delivered to multiple consumers.
2. Consumers are identified, within a consumer group, by a name, which is a case-sensitive string that the clients implementing consumers must choose. This means that even after a disconnect, the stream consumer group retains all the state, since the client will claim again to be the same consumer. However, this also means that it is up to the client to provide a unique identifier.
3. Each consumer group has the concept of the *first ID never consumed* so that, when a consumer asks for new messages, it can provide just messages that were not previously delivered.
4. Consuming a message, however, requires an explicit acknowledgment using a specific command. Redis interprets the acknowledgment as: this message was correctly processed so it can be evicted from the consumer group.
5. A consumer group tracks all the messages that are currently pending, that is, messages that were delivered to some consumer of the consumer group, but are yet to be acknowledged as processed. Thanks to this feature, when accessing the message history of a stream, each consumer *will only see messages that were delivered to it*.

In a way, a consumer group can be imagined as some *amount of state* about a stream:

```
+----------------------------------------+
| consumer_group_name: mygroup           |
| consumer_group_stream: somekey         |
| last_delivered_id: 1292309234234-92    |
|                                        |
| consumers:                             |
|    "consumer-1" with pending messages  |
|       1292309234234-4                  |
|       1292309234232-8                  |
|    "consumer-42" with pending messages |
|       ... (and so forth)               |
+----------------------------------------+
```

If you see this from this point of view, it is very simple to understand what a consumer group can do, how it is able to just provide consumers with their history of pending messages, and how consumers asking for new messages will just be served with message IDs greater than `last_delivered_id`. At the same time, if you look at the consumer group as an auxiliary data structure for Redis streams, it is obvious that a single stream can have multiple consumer groups, that have a different set of consumers. Actually, it is even possible for the same stream to have clients reading without consumer groups via [`XREAD`](https://redis.io/docs/latest/commands/xread), and clients reading via [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) in different consumer groups.

Now it's time to zoom in to see the fundamental consumer group commands. They are the following:

* [`XGROUP`](https://redis.io/docs/latest/commands/xgroup) is used in order to create, destroy and manage consumer groups.
* [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) is used to read from a stream via a consumer group.
* [`XACK`](https://redis.io/docs/latest/commands/xack) is the command that allows a consumer to mark a pending message as correctly processed.
* [`XNACK`](https://redis.io/docs/latest/commands/xnack) is the command that allows a consumer to release pending messages back to the group without acknowledging them, making them immediately available for re-delivery to other consumers.
* [`XACKDEL`](https://redis.io/docs/latest/commands/xackdel) combines acknowledgment and deletion in a single atomic operation with enhanced control over consumer group references.

## Creating a consumer group

Assuming I have a key `race:france` of type stream already existing, in order to create a consumer group I just need to do the following:

Foundational: Create a consumer group for a stream using XGROUP CREATE to enable coordinated message consumption

**Commands:** XGROUP

**Complexity:**
- XGROUP: Depends on subcommand

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XGROUP CREATE race:france france_riders $
OK
```

##### C#

```csharp
        bool res19 = db.StreamCreateConsumerGroup("race:france", "france_riders", "$");
        Console.WriteLine(res19);   // >>> true
```

##### Go

```go
	res19, err := rdb.XGroupCreate(ctx, "race:france", "france_riders", "$").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res19) // >>> OK
```

##### Java (Synchronous - Jedis)

```java
    String res19 = jedis.xgroupCreate("race:france","france_riders",StreamEntryID.LAST_ENTRY,false);
    System.out.println(res19); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res18 = await client.xGroupCreate('race:france', 'france_riders', '$');
console.log(res18); // >>> OK
```

##### Python

```python
res18 = r.xgroup_create("race:france", "france_riders", "$")
print(res18)  # >>> True
```

##### Ruby

```ruby
r.del('race:france')
r.xadd('race:france', {'rider' => 'Castilla'}, id: '1692632086370-0')
res18 = r.xgroup(:create, 'race:france', 'france_riders', '$')
puts res18 # >>> OK
```

##### Rust (Asynchronous)

```rust
        add_france_fixed(&mut r).await;
        if let Ok(res) = r.xgroup_create("race:france", "france_riders", "$").await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xgroup_create("race:france", "france_riders", "$") {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```



As you can see in the command above when creating the consumer group we have to specify an ID, which in the example is just `$`. This is needed because the consumer group, among the other states, must have an idea about what message to serve next at the first consumer connecting, that is, what was the *last message ID* when the group was just created. If we provide `$` as we did, then only new messages arriving in the stream from now on will be provided to the consumers in the group. If we specify `0` instead the consumer group will consume *all* the messages in the stream history to start with. Of course, you can specify any other valid ID. What you know is that the consumer group will start delivering messages that are greater than the ID you specify. Because `$` means the current greatest ID in the stream, specifying `$` will have the effect of consuming only new messages.

[`XGROUP CREATE`](https://redis.io/docs/latest/commands/xgroup-create) also supports creating the stream automatically, if it doesn't exist, using the optional `MKSTREAM` subcommand as the last argument:

Create a consumer group and stream atomically using XGROUP CREATE with MKSTREAM option

**Difficulty:** Intermediate

**Commands:** XGROUP

**Complexity:**
- XGROUP: Depends on subcommand

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XGROUP CREATE race:italy italy_riders $ MKSTREAM
OK
```

##### C#

```csharp
        bool res20 = db.StreamCreateConsumerGroup("race:italy", "italy_riders", "$", true);
        Console.WriteLine(res20);   // >>> true
```

##### Go

```go
	res20, err := rdb.XGroupCreateMkStream(ctx,
		"race:italy", "italy_riders", "$",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res20) // >>> OK
```

##### Java (Synchronous - Jedis)

```java
    String res20 = jedis.xgroupCreate("race:italy","italy_riders",StreamEntryID.LAST_ENTRY,true);
    System.out.println(res20); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res19 = await client.xGroupCreate('race:italy', 'italy_riders', '$', {
  MKSTREAM: true
});
console.log(res19); // >>> OK
```

##### Python

```python
res19 = r.xgroup_create("race:italy", "italy_riders", "$", mkstream=True)
print(res19)  # >>> True
```

##### Ruby

```ruby
r.del('race:italy')
res19 = r.xgroup(:create, 'race:italy', 'italy_riders', '$', mkstream: true)
puts res19 # >>> OK
```

##### Rust (Asynchronous)

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        if let Ok(res) = r.xgroup_create_mkstream("race:italy", "italy_riders", "$").await {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xgroup_create_mkstream("race:italy", "italy_riders", "$") {
            let res: () = res;
            let _ = res;
            println!("OK"); // >>> OK
        }
```



Now that the consumer group is created we can immediately try to read messages via the consumer group using the [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) command. We'll read from consumers, that we will call Alice and Bob, to see how the system will return different messages to Alice or Bob.

[`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) is very similar to [`XREAD`](https://redis.io/docs/latest/commands/xread) and provides the same **BLOCK** option, otherwise it is a synchronous command. However there is a *mandatory* option that must be always specified, which is **GROUP** and has two arguments: the name of the consumer group, and the name of the consumer that is attempting to read. The option **COUNT** is also supported and is identical to the one in [`XREAD`](https://redis.io/docs/latest/commands/xread).

We'll add riders to the race:italy stream and try reading something using the consumer group:
Note: *here rider is the field name, and the name is the associated value. Remember that stream items are small dictionaries.*

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
special ID" try_it="false" runnable="false" >}}
> XADD race:italy * rider Castilla
"1692632639151-0"
> XADD race:italy * rider Royce
"1692632647899-0"
> XADD race:italy * rider Sam-Bodden
"1692632662819-0"
> XADD race:italy * rider Prickett
"1692632670501-0"
> XADD race:italy * rider Norem
"1692632678249-0"
> XREADGROUP GROUP italy_riders Alice COUNT 1 STREAMS race:italy >
1) 1) "race:italy"
   2) 1) 1) "1692632639151-0"
         2) 1) "rider"
            2) "Castilla"
```

##### C#

```csharp
        RedisValue groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Castilla")]
        ); // 1712744323758-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Royce")]
        ); // 1712744358384-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Sam-Bodden")]
        ); // 1712744379676-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Prickett")]
        ); // 1712744399401-0

        groupRes = db.StreamAdd(
            "race:italy",
            [new("rider", "Norem")]
        ); // 1712744413117-0

        StreamEntry[] res21 = db.StreamReadGroup("race:italy", "italy_riders", "Alice", ">", 1);

        foreach (StreamEntry entry in res21)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744323758-0: [rider: Castilla]
```

##### Go

```go
	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Castilla"},
	}).Result()
	// >>> 1692632639151-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Royce"},
	}).Result()
	// >>> 1692632647899-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Sam-Bodden"},
	}).Result()
	// >>> 1692632662819-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Prickett"},
	}).Result()
	// >>> 1692632670501-0

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		Values: map[string]interface{}{"rider": "Norem"},
	}).Result()
	// >>> 1692632678249-0

	if err != nil {
		panic(err)
	}

	// fmt.Println(res25)

	res21, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", ">"},
		Group:    "italy_riders",
		Consumer: "Alice",
		Count:    1,
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res21)
	// >>> [{race:italy [{1692632639151-0 map[rider:Castilla] 0 0}]}]
```

##### Java (Synchronous - Jedis)

```java
    StreamEntryID id1 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Castilaa");}},XAddParams.xAddParams());
    StreamEntryID id2 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Royce");}},XAddParams.xAddParams());
    StreamEntryID id3 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Sam-Bodden");}},XAddParams.xAddParams());
    StreamEntryID id4 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Prickett");}},XAddParams.xAddParams());
    StreamEntryID id5 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Norem");}},XAddParams.xAddParams());

    List<Map.Entry<String, List<StreamEntry>>> res21 = jedis.xreadGroup("italy_riders","Alice", XReadGroupParams.xReadGroupParams().count(1),new HashMap<String,StreamEntryID>(){{put("race:italy",StreamEntryID.UNRECEIVED_ENTRY);}});
    System.out.println(res21); // >>> [race:italy=[1701766299006-0 {rider=Castilaa}]]
```

##### JavaScript (Node.js)

```javascript
await client.xAdd('race:italy', '*', {
  'rider': 'Castilla'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Royce'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Sam-Bodden'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Prickett'
});
await client.xAdd('race:italy', '*', {
  'rider': 'Norem'
});

const res20 = await client.xReadGroup(
  'italy_riders',
  'Alice', {
    key: 'race:italy',
    id: '>'
  }, {
    COUNT: 1
  }
);
console.log(res20); // >>> [{ name: 'race:italy', messages: [{ id: '1692629925771-0', message: { rider: 'Castilla' } }] }]
```

##### Python

```python
r.xadd("race:italy", {"rider": "Castilla"})
r.xadd("race:italy", {"rider": "Royce"})
r.xadd("race:italy", {"rider": "Sam-Bodden"})
r.xadd("race:italy", {"rider": "Prickett"})
r.xadd("race:italy", {"rider": "Norem"})

res20 = r.xreadgroup(
    streams={"race:italy": ">"},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res20)  # >>> [['race:italy', [('1692629925771-0', {'rider': 'Castilla'})]]]
```

##### Ruby

```ruby
r.del('race:italy')
r.xgroup(:create, 'race:italy', 'italy_riders', '$', mkstream: true)
r.xadd('race:italy', {'rider' => 'Castilla'}, id: '1692632639151-0')
r.xadd('race:italy', {'rider' => 'Royce'}, id: '1692632647899-0')
r.xadd('race:italy', {'rider' => 'Sam-Bodden'}, id: '1692632662819-0')
r.xadd('race:italy', {'rider' => 'Prickett'}, id: '1692632670501-0')
r.xadd('race:italy', {'rider' => 'Norem'}, id: '1692632678249-0')

res20 = r.xreadgroup('italy_riders', 'Alice', ['race:italy'], ['>'], count: 1)
puts res20.inspect
# >>> {"race:italy"=>[["1692632639151-0", {"rider" => "Castilla"}]]}
```

##### Rust (Asynchronous)

```rust
        let italy_1: Option<String> = r
            .xadd("race:italy", "1692632639151-0", &[("rider", "Castilla")])
            .await
            .expect("italy1");
        let italy_1 = italy_1.expect("missing stream id");
        println!("{italy_1}"); // >>> 1692632639151-0
        let italy_2: Option<String> = r
            .xadd("race:italy", "1692632647899-0", &[("rider", "Royce")])
            .await
            .expect("italy2");
        let italy_2 = italy_2.expect("missing stream id");
        println!("{italy_2}"); // >>> 1692632647899-0
        let italy_3: Option<String> = r
            .xadd("race:italy", "1692632662819-0", &[("rider", "Sam-Bodden")])
            .await
            .expect("italy3");
        let italy_3 = italy_3.expect("missing stream id");
        println!("{italy_3}"); // >>> 1692632662819-0
        let italy_4: Option<String> = r
            .xadd("race:italy", "1692632670501-0", &[("rider", "Prickett")])
            .await
            .expect("italy4");
        let italy_4 = italy_4.expect("missing stream id");
        println!("{italy_4}"); // >>> 1692632670501-0
        let italy_5: Option<String> = r
            .xadd("race:italy", "1692632678249-0", &[("rider", "Norem")])
            .await
            .expect("italy5");
        let italy_5 = italy_5.expect("missing stream id");
        println!("{italy_5}"); // >>> 1692632678249-0
        let opts = StreamReadOptions::default().group("italy_riders", "Alice").count(1);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup read should return data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```

##### Rust (Synchronous)

```rust
        let italy_1: Option<String> = r
            .xadd("race:italy", "1692632639151-0", &[("rider", "Castilla")])
            .expect("italy1");
        let italy_1 = italy_1.expect("missing stream id");
        println!("{italy_1}"); // >>> 1692632639151-0
        let italy_2: Option<String> = r
            .xadd("race:italy", "1692632647899-0", &[("rider", "Royce")])
            .expect("italy2");
        let italy_2 = italy_2.expect("missing stream id");
        println!("{italy_2}"); // >>> 1692632647899-0
        let italy_3: Option<String> = r
            .xadd("race:italy", "1692632662819-0", &[("rider", "Sam-Bodden")])
            .expect("italy3");
        let italy_3 = italy_3.expect("missing stream id");
        println!("{italy_3}"); // >>> 1692632662819-0
        let italy_4: Option<String> = r
            .xadd("race:italy", "1692632670501-0", &[("rider", "Prickett")])
            .expect("italy4");
        let italy_4 = italy_4.expect("missing stream id");
        println!("{italy_4}"); // >>> 1692632670501-0
        let italy_5: Option<String> = r
            .xadd("race:italy", "1692632678249-0", &[("rider", "Norem")])
            .expect("italy5");
        let italy_5 = italy_5.expect("missing stream id");
        println!("{italy_5}"); // >>> 1692632678249-0

        let opts = StreamReadOptions::default().group("italy_riders", "Alice").count(1);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup read should return data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```



[`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) replies are just like [`XREAD`](https://redis.io/docs/latest/commands/xread) replies. Note however the `GROUP <group-name> <consumer-name>` provided above. It states that I want to read from the stream using the consumer group `mygroup` and I'm the consumer `Alice`. Every time a consumer performs an operation with a consumer group, it must specify its name, uniquely identifying this consumer inside the group.

There is another very important detail in the command line above, after the mandatory **STREAMS** option the ID requested for the key `race:italy` is the special ID `>`. This special ID is only valid in the context of consumer groups, and it means: **messages never delivered to other consumers so far**.

This is almost always what you want, however it is also possible to specify a real ID, such as `0` or any other valid ID, in this case, however, what happens is that we request from [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) to just provide us with the **history of pending messages**, and in such case, will never see new messages in the group. So basically [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) has the following behavior based on the ID we specify:

* If the ID is the special ID `>` then the command will return only new messages never delivered to other consumers so far, and as a side effect, will update the consumer group's *last ID*.
* If the ID is any other valid numerical ID, then the command will let us access our *history of pending messages*. That is, the set of messages that were delivered to this specified consumer (identified by the provided name), and never acknowledged so far with [`XACK`](https://redis.io/docs/latest/commands/xack).

We can test this behavior immediately specifying an ID of 0, without any **COUNT** option: we'll just see the only pending message, that is, the one about Castilla:

Access pending message history using XREADGROUP with a specific ID to retrieve unacknowledged messages

**Difficulty:** Intermediate

**Commands:** XREADGROUP

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XREADGROUP GROUP italy_riders Alice STREAMS race:italy 0
1) 1) "race:italy"
   2) 1) 1) "1692632639151-0"
         2) 1) "rider"
            2) "Castilla"
```

##### C#

```csharp
        StreamEntry[] res22 = db.StreamReadGroup("race:italy", "italy_riders", "Alice", "0");

        foreach (StreamEntry entry in res22)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
            // >>> 1712744323758-0: [rider: Castilla]
        }
```

##### Go

```go
	res22, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", "0"},
		Group:    "italy_riders",
		Consumer: "Alice",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res22)
	// >>> [{race:italy [{1692632639151-0 map[rider:Castilla] 0 0}]}]
```

##### Java (Synchronous - Jedis)

```java
    List<Map.Entry<String, List<StreamEntry>>> res22 = jedis.xreadGroup("italy_riders","Alice", XReadGroupParams.xReadGroupParams().count(1),new HashMap<String,StreamEntryID>(){{put("race:italy",new StreamEntryID());}});
    System.out.println(res22); // >>> [race:italy=[1701766299006-0 {rider=Castilaa}]]
```

##### JavaScript (Node.js)

```javascript
const res21 = await client.xReadGroup(
  'italy_riders',
  'Alice', {
    key: 'race:italy',
    id: '0'
  }, {
    COUNT: 1
  }
);
console.log(res21); // >>> [{ name: 'race:italy', messages: [{ id: '1692629925771-0', message: { rider: 'Castilla' } }] }]
```

##### Python

```python
res21 = r.xreadgroup(
    streams={"race:italy": 0},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res21)  # >>> [['race:italy', [('1692629925771-0', {'rider': 'Castilla'})]]]
```

##### Ruby

```ruby
res21 = r.xreadgroup('italy_riders', 'Alice', ['race:italy'], ['0'], count: 1)
puts res21.inspect
# >>> {"race:italy"=>[["1692632639151-0", {"rider" => "Castilla"}]]}
```

##### Rust (Asynchronous)

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```

##### Rust (Synchronous)

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632639151-0", [("rider", "Castilla")])])]
        }
```



However, if we acknowledge the message as processed, it will no longer be part of the pending messages history, so the system will no longer report anything:

Foundational: Acknowledge processed messages using XACK to mark them as handled by a consumer

**Commands:** XACK, XREADGROUP

**Complexity:**
- XACK: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XACK race:italy italy_riders 1692632639151-0
(integer) 1
> XREADGROUP GROUP italy_riders Alice STREAMS race:italy 0
1) 1) "race:italy"
   2) (empty array)
```

##### C#

```csharp
        long res23 = db.StreamAcknowledge("race:italy", "italy_riders", "1712744323758-0");
        Console.WriteLine(res23);   // >>> 1

        StreamEntry[] res24 = db.StreamReadGroup("race:italy", "italy_riders", "Alice", "0");

        foreach (StreamEntry entry in res24)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> <empty array>
```

##### Go

```go
	res23, err := rdb.XAck(ctx,
		"race:italy", "italy_riders", "1692632639151-0",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res23) // >>> 1

	res24, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", "0"},
		Group:    "italy_riders",
		Consumer: "Alice",
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res24)
	// >>> [{race:italy []}]
```

##### Java (Synchronous - Jedis)

```java
    long res23 = jedis.xack("race:italy","italy_riders",id1);
    System.out.println(res23); // >>> 1

    List<Map.Entry<String, List<StreamEntry>>> res24 = jedis.xreadGroup("italy_riders","Alice", XReadGroupParams.xReadGroupParams().count(1),new HashMap<String,StreamEntryID>(){{put("race:italy",new StreamEntryID());}});
    System.out.println(res24); // >>> [race:italy=[]]
```

##### JavaScript (Node.js)

```javascript
const res22 = await client.xAck('race:italy', 'italy_riders', '1692629925771-0')
console.log(res22); // >>> 1

const res23 = await client.xReadGroup(
  'italy_riders',
  'Alice', {
    key: 'race:italy',
    id: '0'
  }, {
    COUNT: 1
  }
);
console.log(res23); // >>> [{ name: 'race:italy', messages: [] }]
```

##### Python

```python
res22 = r.xack("race:italy", "italy_riders", "1692629925771-0")
print(res22)  # >>> 1

res23 = r.xreadgroup(
    streams={"race:italy": 0},
    consumername="Alice",
    groupname="italy_riders",
    count=1,
)
print(res23)  # >>> [['race:italy', []]]
```

##### Ruby

```ruby
res22 = r.xack('race:italy', 'italy_riders', '1692632639151-0')
puts res22 # >>> 1

res23 = r.xreadgroup('italy_riders', 'Alice', ['race:italy'], ['0'])
puts res23.inspect
# >>> {"race:italy"=>[]}
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xack("race:italy", "italy_riders", &["1692632639151-0"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }
        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("race:italy", [])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xack("race:italy", "italy_riders", &["1692632639151-0"]) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        let opts = StreamReadOptions::default().group("italy_riders", "Alice");
        if let Ok(res) = r.xread_options(&["race:italy"], &["0"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("xgroup history")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("race:italy", [])]
        }
```



Don't worry if you yet don't know how [`XACK`](https://redis.io/docs/latest/commands/xack) works, the idea is just that processed messages are no longer part of the history that we can access.

Now it's Bob's turn to read something:

Practical pattern: Demonstrate consumer group load balancing where different consumers receive different messages from the same stream

**Difficulty:** Intermediate

**Commands:** XREADGROUP

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XREADGROUP GROUP italy_riders Bob COUNT 2 STREAMS race:italy >
1) 1) "race:italy"
   2) 1) 1) "1692632647899-0"
         2) 1) "rider"
            2) "Royce"
      2) 1) "1692632662819-0"
         2) 1) "rider"
            2) "Sam-Bodden"
```

##### C#

```csharp
        StreamEntry[] res25 = db.StreamReadGroup("race:italy", "italy_riders", "Bob", ">", 2);

        foreach (StreamEntry entry in res25)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744358384-0: [rider: Royce]
        // >>> 1712744379676-0: [rider: Sam-Bodden]
```

##### Go

```go
	res25, err := rdb.XReadGroup(ctx, &redis.XReadGroupArgs{
		Streams:  []string{"race:italy", ">"},
		Group:    "italy_riders",
		Consumer: "Bob",
		Count:    2,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res25)
	// >>> [{race:italy [{1692632647899-0 map[rider:Royce] 0 0} {1692632662819-0 map[rider:Sam-Bodden] 0 0}]}]

```

##### Java (Synchronous - Jedis)

```java
    List<Map.Entry<String, List<StreamEntry>>> res25 = jedis.xreadGroup("italy_riders","Bob", XReadGroupParams.xReadGroupParams().count(2),new HashMap<String,StreamEntryID>(){{put("race:italy",StreamEntryID.UNRECEIVED_ENTRY);}});
    System.out.println(res25); // >>> [race:italy=[1701767632261-1 {rider=Royce}, 1701767632262-0 {rider=Sam-Bodden}]]
```

##### JavaScript (Node.js)

```javascript
const res24 = await client.xReadGroup(
  'italy_riders',
  'Bob', {
    key: 'race:italy',
    id: '>'
  }, {
    COUNT: 2
  }
);
console.log(res24); // >>> [{ name: 'race:italy', messages: [{ id: '1692629925789-0', message: { rider: 'Royce' } }, { id: '1692629925790-0', message: { rider: 'Sam-Bodden' } }] }]
```

##### Python

```python
res24 = r.xreadgroup(
    streams={"race:italy": ">"},
    consumername="Bob",
    groupname="italy_riders",
    count=2,
)
print(
    res24
)
# >>> [
#       ['race:italy', [
#           ('1692629925789-0',
#               {'rider': 'Royce'}
#           ),
#           ('1692629925790-0',
#               {'rider': 'Sam-Bodden'}
#           )
#       ]
#       ]
# ]
```

##### Ruby

```ruby
res24 = r.xreadgroup('italy_riders', 'Bob', ['race:italy'], ['>'], count: 2)
puts res24.inspect
# >>> {"race:italy"=>[["1692632647899-0", {"rider" => "Royce"}],
#                 ["1692632662819-0", {"rider" => "Sam-Bodden"}]]}
```

##### Rust (Asynchronous)

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Bob").count(2);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts).await {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("bob should receive data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632647899-0", [("rider", "Royce")]), ("1692632662819-0", [("rider", "Sam-Bodden")])])]
        }
```

##### Rust (Synchronous)

```rust
        let opts = StreamReadOptions::default().group("italy_riders", "Bob").count(2);
        if let Ok(res) = r.xread_options(&["race:italy"], &[">"], &opts) {
            let res: Option<StreamReadReply> = res;
            let view: Vec<_> = res
                .expect("bob should receive data")
                .keys
                .iter()
                .map(|stream| {
                    (
                        stream.key.clone(),
                        stream
                            .ids
                            .iter()
                            .map(|entry| {
                                (
                                    entry.id.clone(),
                                    vec![(
                                        "rider".to_string(),
                                        entry.get::<String>("rider").expect("missing rider"),
                                    )],
                                )
                            })
                            .collect::<Vec<_>>(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("race:italy", [("1692632647899-0", [("rider", "Royce")]), ("1692632662819-0", [("rider", "Sam-Bodden")])])]
        }
```



Bob asked for a maximum of two messages and is reading via the same group `mygroup`. So what happens is that Redis reports just *new* messages. As you can see the "Castilla" message is not delivered, since it was already delivered to Alice, so Bob gets Royce and Sam-Bodden and so forth.

This way Alice, Bob, and any other consumer in the group, are able to read different messages from the same stream, to read their history of yet to process messages, or to mark messages as processed. This allows creating different topologies and semantics for consuming messages from a stream.

There are a few things to keep in mind:

* Consumers are auto-created the first time they are mentioned, no need for explicit creation.
* Even with [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) you can read from multiple keys at the same time, however for this to work, you need to create a consumer group with the same name in every stream. This is not a common need, but it is worth mentioning that the feature is technically available.
* [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) is a *write command* because even if it reads from the stream, the consumer group is modified as a side effect of reading, so it can only be called on master instances.

An example of a consumer implementation, using consumer groups, written in the Ruby language could be the following. The Ruby code is aimed to be readable by virtually any experienced programmer, even if they do not know Ruby:

```ruby
require 'redis'

if ARGV.length == 0
    puts "Please specify a consumer name"
    exit 1
end

ConsumerName = ARGV[0]
GroupName = "mygroup"
r = Redis.new

def process_message(id,msg)
    puts "[#{ConsumerName}] #{id} = #{msg.inspect}"
end

$lastid = '0-0'

puts "Consumer #{ConsumerName} starting..."
check_backlog = true
while true
    # Pick the ID based on the iteration: the first time we want to
    # read our pending messages, in case we crashed and are recovering.
    # Once we consumed our history, we can start getting new messages.
    if check_backlog
        myid = $lastid
    else
        myid = '>'
    end

    items = r.xreadgroup('GROUP',GroupName,ConsumerName,'BLOCK','2000','COUNT','10','STREAMS',:my_stream_key,myid)

    if items == nil
        puts "Timeout!"
        next
    end

    # If we receive an empty reply, it means we were consuming our history
    # and that the history is now empty. Let's start to consume new messages.
    check_backlog = false if items[0][1].length == 0

    items[0][1].each{|i|
        id,fields = i

        # Process the message
        process_message(id,fields)

        # Acknowledge the message as processed
        r.xack(:my_stream_key,GroupName,id)

        $lastid = id
    }
end
```

As you can see the idea here is to start by consuming the history, that is, our list of pending messages. This is useful because the consumer may have crashed before, so in the event of a restart we want to re-read messages that were delivered to us without getting acknowledged. Note that we might process a message multiple times or one time (at least in the case of consumer failures, but there are also the limits of Redis persistence and replication involved, see the specific section about this topic).

Once the history was consumed, and we get an empty list of messages, we can switch to using the `>` special ID in order to consume new messages.

## Recovering from permanent failures

The example above allows us to write consumers that participate in the same consumer group, each taking a subset of messages to process, and when recovering from failures re-reading the pending messages that were delivered just to them. However in the real world consumers may permanently fail and never recover. What happens to the pending messages of the consumer that never recovers after stopping for any reason?

Redis consumer groups offer a feature that is used in these situations in order to *claim* the pending messages of a given consumer so that such messages will change ownership and will be re-assigned to a different consumer. The feature is very explicit. A consumer has to inspect the list of pending messages, and will have to claim specific messages using a special command, otherwise the server will leave the messages pending forever and assigned to the old consumer. In this way different applications can choose if to use such a feature or not, and exactly how to use it.

The first step of this process is just a command that provides observability of pending entries in the consumer group and is called [`XPENDING`](https://redis.io/docs/latest/commands/xpending).
This is a read-only command which is always safe to call and will not change ownership of any message.
In its simplest form, the command is called with two arguments, which are the name of the stream and the name of the consumer group.

View pending message summary for a consumer group using XPENDING to monitor unacknowledged messages

**Difficulty:** Intermediate

**Commands:** XPENDING

**Complexity:**
- XPENDING: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XPENDING race:italy italy_riders
1) (integer) 2
2) "1692632647899-0"
3) "1692632662819-0"
4) 1) 1) "Bob"
      2) "2"
```

##### C#

```csharp
        StreamPendingInfo res26 = db.StreamPending("race:italy", "italy_riders");
        Console.WriteLine($"pending: {res26.PendingMessageCount}, min: {res26.LowestPendingMessageId}, max: {res26.HighestPendingMessageId}, consumers:[{string.Join(", ", res26.Consumers.Select(c => $"{c.Name}: {c.PendingMessageCount}"))}]");
        // >>> pending: 2, min: 1712747506906-0, max: 1712747506907-0, consumers:[name: Bob, pending:2]
```

##### Go

```go
	res26, err := rdb.XPending(ctx, "race:italy", "italy_riders").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res26)
	// >>> &{2 1692632647899-0 1692632662819-0 map[Bob:2]}
```

##### Java (Synchronous - Jedis)

```java
    StreamPendingSummary res26 = jedis.xpending("race:italy","italy_riders");
    System.out.println(res26.getConsumerMessageCount()); // >>> {Bob=2}
```

##### JavaScript (Node.js)

```javascript
const res25 = await client.xPending('race:italy', 'italy_riders');
console.log(res25); // >>> {'pending': 2, 'firstId': '1692629925789-0', 'lastId': '1692629925790-0', 'consumers': [{'name': 'Bob', 'deliveriesCounter': 2}]}
```

##### Python

```python
res25 = r.xpending("race:italy", "italy_riders")
print(
    res25
)
# >>> {
#       'pending': 2, 'min': '1692629925789-0', 'max': '1692629925790-0',
#       'consumers': [{'name': 'Bob', 'pending': 2}]
# }
```

##### Ruby

```ruby
res25 = r.xpending('race:italy', 'italy_riders')
puts res25.inspect
# >>> {"size"=>2, "min_entry_id" => "1692632647899-0", "max_entry_id" => "1692632662819-0", "consumers"=>{"Bob" => "2"}}
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xpending("race:italy", "italy_riders").await {
            let res: StreamPendingReply = res;
            let view = match res {
                StreamPendingReply::Empty => None,
                StreamPendingReply::Data(data) => Some((
                    data.count,
                    data.start_id.clone(),
                    data.end_id.clone(),
                    data.consumers
                        .iter()
                        .map(|consumer| (consumer.name.clone(), consumer.pending))
                        .collect::<Vec<_>>(),
                )),
            }
            .expect("pending summary");
            println!("{view:?}");
            // >>> (2, "1692632647899-0", "1692632662819-0", [("Bob", 2)])
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xpending("race:italy", "italy_riders") {
            let res: StreamPendingReply = res;
            let view = match res {
                StreamPendingReply::Empty => None,
                StreamPendingReply::Data(data) => Some((
                    data.count,
                    data.start_id.clone(),
                    data.end_id.clone(),
                    data.consumers
                        .iter()
                        .map(|consumer| (consumer.name.clone(), consumer.pending))
                        .collect::<Vec<_>>(),
                )),
            }
            .expect("pending summary");
            println!("{view:?}");
            // >>> (2, "1692632647899-0", "1692632662819-0", [("Bob", 2)])
        }
```



When called in this way, the command outputs the total number of pending messages in the consumer group (two in this case), the lower and higher message ID among the pending messages, and finally a list of consumers and the number of pending messages they have.
We have only Bob with two pending messages because the single message that Alice requested was acknowledged using [`XACK`](https://redis.io/docs/latest/commands/xack).

We can ask for more information by giving more arguments to [`XPENDING`](https://redis.io/docs/latest/commands/xpending), because the full command signature is the following:

```
XPENDING <key> <groupname> [[IDLE <min-idle-time>] <start-id> <end-id> <count> [<consumer-name>]]
```

By providing a start and end ID (that can be just `-` and `+` as in [`XRANGE`](https://redis.io/docs/latest/commands/xrange)) and a count to control the amount of information returned by the command, we are able to know more about the pending messages. The optional final argument, the consumer name, is used if we want to limit the output to just messages pending for a given consumer, but won't use this feature in the following example.

Get detailed pending message information including idle time and delivery count using XPENDING with range

**Difficulty:** Advanced

**Commands:** XPENDING

**Complexity:**
- XPENDING: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XPENDING race:italy italy_riders - + 10
1) 1) "1692632647899-0"
   2) "Bob"
   3) (integer) 74642
   4) (integer) 1
2) 1) "1692632662819-0"
   2) "Bob"
   3) (integer) 74642
   4) (integer) 1
```

##### C#

```csharp
        StreamPendingMessageInfo[] res27 = db.StreamPendingMessages(
            "race:italy", "italy_riders", 10, "", "-", "+"
        );

        foreach (StreamPendingMessageInfo info in res27)
        {
            Console.WriteLine($"message_id: {info.MessageId}, consumer: {info.ConsumerName}, time_since_delivered: {info.IdleTimeInMilliseconds}, times_delivered: {info.DeliveryCount}");
        }
        // >>> message_id: min: 1712747506906-0, consumer: Bob, time_since_delivered: 31084, times_delivered: 1
        // >>> message_id: min: 1712747506907-0, consumer: Bob, time_since_delivered: 31084, times_delivered: 1
```

##### Go

```go
	res27, err := rdb.XPendingExt(ctx, &redis.XPendingExtArgs{
		Stream: "race:italy",
		Group:  "italy_riders",
		Start:  "-",
		End:    "+",
		Count:  10,
	}).Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res27)
	// >>> [{1692632647899-0 Bob 0s 1} {1692632662819-0 Bob 0s 1}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamPendingEntry> res27 = jedis.xpending("race:italy","italy_riders",XPendingParams.xPendingParams().start(StreamEntryID.MINIMUM_ID).end(StreamEntryID.MAXIMUM_ID).count(10));
    System.out.println(res27); // >>> [1701768567412-1 Bob idle:0 times:1, 1701768567412-2 Bob idle:0 times:1]
```

##### JavaScript (Node.js)

```javascript
const res26 = await client.xPendingRange('race:italy', 'italy_riders', '-', '+', 10);
console.log(res26); // >>> [{'id': '1692629925789-0', 'consumer': 'Bob', 'millisecondsSinceLastDelivery': 31084, 'deliveriesCounter:': 1}, {'id': '1692629925790-0', 'consumer': 'Bob', 'millisecondsSinceLastDelivery': 31084, 'deliveriesCounter': 1}]
```

##### Python

```python
res26 = r.xpending_range("race:italy", "italy_riders", "-", "+", 10)
print(
    res26
)
# >>> [
#       {
#           'message_id': '1692629925789-0', 'consumer': 'Bob',
#           'time_since_delivered': 31084, 'times_delivered': 1
#       },
#       {
#           'message_id': '1692629925790-0', 'consumer': 'Bob',
#           'time_since_delivered': 31084, 'times_delivered': 1
#       }
# ]
```

##### Ruby

```ruby
res26 = r.xpending('race:italy', 'italy_riders', '-', '+', 10)
puts res26.inspect
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xpending_count("race:italy", "italy_riders", "-", "+", 10).await {
            let res: StreamPendingCountReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        entry.consumer.clone(),
                        entry.last_delivered_ms,
                        entry.times_delivered,
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632647899-0", "Bob", 5, 1), ("1692632662819-0", "Bob", 5, 1)]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xpending_count("race:italy", "italy_riders", "-", "+", 10) {
            let res: StreamPendingCountReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        entry.consumer.clone(),
                        entry.last_delivered_ms,
                        entry.times_delivered,
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("1692632647899-0", "Bob", 5, 1), ("1692632662819-0", "Bob", 5, 1)]
        }
```



Now we have the details for each message: the ID, the consumer name, the *idle time* in milliseconds, which is how many milliseconds have passed since the last time the message was delivered to some consumer, and finally the number of times that a given message was delivered.
We have two messages from Bob, and they are idle for 60000+ milliseconds, about a minute.

Note that nobody prevents us from checking what the first message content was by just using [`XRANGE`](https://redis.io/docs/latest/commands/xrange).

Retrieve the content of pending messages using XRANGE to inspect what needs to be processed

**Difficulty:** Intermediate

**Commands:** XRANGE

**Complexity:**
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:italy 1692632647899-0 1692632647899-0
1) 1) "1692632647899-0"
   2) 1) "rider"
      2) "Royce"
```

##### C#

```csharp
        StreamEntry[] res28 = db.StreamRange("race:italy", "1712744358384-0", "1712744358384-0");

        foreach (StreamEntry entry in res28)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744358384-0: [rider: Royce]
```

##### Go

```go
	res28, err := rdb.XRange(ctx, "race:italy",
		"1692632647899-0", "1692632647899-0",
	).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res28) // >>> [{1692632647899-0 map[rider:Royce] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res28 = jedis.xrange("race:italy",id2.toString(),id2.toString());
    System.out.println(res28); // >>> [1701768744819-1 {rider=Royce}]
```

##### JavaScript (Node.js)

```javascript
const res27 = await client.xRange('race:italy', '1692629925789-0', '1692629925789-0');
console.log(res27); // >>> [{ id: '1692629925789-0', message: { rider: 'Royce' } }]
```

##### Python

```python
res27 = r.xrange("race:italy", "1692629925789-0", "1692629925789-0")
print(res27)  # >>> [('1692629925789-0', {'rider': 'Royce'})]
```

##### Ruby

```ruby
res27 = r.xrange('race:italy', '1692632647899-0', '1692632647899-0')
puts res27.inspect
# >>> [["1692632647899-0", {"rider" => "Royce"}]]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xrange("race:italy", "1692632647899-0", "1692632647899-0").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xrange("race:italy", "1692632647899-0", "1692632647899-0") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```



We have just to repeat the same ID twice in the arguments. Now that we have some ideas, Alice may decide that after 1 minute of not processing messages, Bob will probably not recover quickly, and it's time to *claim* such messages and resume the processing in place of Bob. To do so, we use the [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim) command.

This command is very complex and full of options in its full form, since it is used for replication of consumer groups changes, but we'll use just the arguments that we need normally. In this case it is as simple as:

```
XCLAIM <key> <group> <consumer> <min-idle-time> <ID-1> <ID-2> ... <ID-N>
```

Basically we say, for this specific key and group, I want that the message IDs specified will change ownership, and will be assigned to the specified consumer name `<consumer>`. However, we also provide a minimum idle time, so that the operation will only work if the idle time of the mentioned messages is greater than the specified idle time. This is useful because maybe two clients are retrying to claim a message at the same time:

```
Client 1: XCLAIM race:italy italy_riders Alice 60000 1692632647899-0
Client 2: XCLAIM race:italy italy_riders Lora 60000 1692632647899-0
```

However, as a side effect, claiming a message will reset its idle time and will increment its number of deliveries counter, so the second client will fail claiming it. In this way we avoid trivial re-processing of messages (even if in the general case you cannot obtain exactly once processing).

This is the result of the command execution:

Claim pending messages from another consumer using XCLAIM when a consumer fails to process messages

**Difficulty:** Advanced

**Commands:** XCLAIM

**Complexity:**
- XCLAIM: O(log N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XCLAIM race:italy italy_riders Alice 60000 1692632647899-0
1) 1) "1692632647899-0"
   2) 1) "rider"
      2) "Royce"
```

##### C#

```csharp
        StreamEntry[] res29 = db.StreamClaim(
            "race:italy", "italy_riders", "Alice", 60000, [1712744358384 - 0]
        );

        foreach (StreamEntry entry in res29)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712744358384-0: [rider: Royce]
```

##### Go

```go
	res29, err := rdb.XClaim(ctx, &redis.XClaimArgs{
		Stream:   "race:italy",
		Group:    "italy_riders",
		Consumer: "Alice",
		MinIdle:  0,
		Messages: []string{"1692632647899-0"},
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res29)
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res29 = jedis.xclaim("race:italy","italy_riders","Alice", 0L, XClaimParams.xClaimParams().time(60000),id2);
    System.out.println(res29); // >>> [1701769004195-1 {rider=Royce}]
```

##### JavaScript (Node.js)

```javascript
const res28 = await client.xClaim(
  'race:italy', 'italy_riders', 'Alice', 60000, ['1692629925789-0']
);
console.log(res28); // >>> [{ id: '1692629925789-0', message: { rider: 'Royce' } }]
```

##### Python

```python
res28 = r.xclaim("race:italy", "italy_riders", "Alice", 60000, ["1692629925789-0"])
print(res28)  # >>> [('1692629925789-0', {'rider': 'Royce'})]
```

##### Ruby

```ruby
res28 = r.xclaim('race:italy', 'italy_riders', 'Alice', 0, '1692632647899-0')
puts res28.inspect
# >>> [["1692632647899-0", {"rider" => "Royce"}]]
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r
            .xclaim("race:italy", "italy_riders", "Alice", 1, &["1692632647899-0"])
            .await
        {
            let res: redis::streams::StreamClaimReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xclaim("race:italy", "italy_riders", "Alice", 1, &["1692632647899-0"]) {
            let res: redis::streams::StreamClaimReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("1692632647899-0", [("rider", "Royce")])]
        }
```



The message was successfully claimed by Alice, who can now process the message and acknowledge it, and move things forward even if the original consumer is not recovering.

It is clear from the example above that as a side effect of successfully claiming a given message, the [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim) command also returns it. However this is not mandatory. The **JUSTID** option can be used in order to return just the IDs of the message successfully claimed. This is useful if you want to reduce the bandwidth used between the client and the server (and also the performance of the command) and you are not interested in the message because your consumer is implemented in a way that it will rescan the history of pending messages from time to time.

Claiming may also be implemented by a separate process: one that just checks the list of pending messages, and assigns idle messages to consumers that appear to be active. Active consumers can be obtained using one of the observability features of Redis streams. This is the topic of the next section.

## Automatic claiming

The [`XAUTOCLAIM`](https://redis.io/docs/latest/commands/xautoclaim) command, added in Redis 6.2, implements the claiming process that we've described above.
[`XPENDING`](https://redis.io/docs/latest/commands/xpending) and [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim) provide the basic building blocks for different types of recovery mechanisms.
This command optimizes the generic process by having Redis manage it and offers a simple solution for most recovery needs.

[`XAUTOCLAIM`](https://redis.io/docs/latest/commands/xautoclaim) identifies idle pending messages and transfers ownership of them to a consumer.
The command's signature looks like this:

```
XAUTOCLAIM <key> <group> <consumer> <min-idle-time> <start> [COUNT count] [JUSTID]
```

So, in the example above, I could have used automatic claiming to claim a single message like this:

Practical pattern: Automatically claim idle pending messages using XAUTOCLAIM for simplified consumer failure recovery

**Difficulty:** Advanced

**Commands:** XAUTOCLAIM

**Complexity:**
- XAUTOCLAIM: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XAUTOCLAIM race:italy italy_riders Alice 60000 0-0 COUNT 1
1) "0-0"
2) 1) 1) "1692632662819-0"
      2) 1) "rider"
         2) "Sam-Bodden"
```

##### C#

```csharp
        StreamAutoClaimResult res30 = db.StreamAutoClaim(
            "race:italy", "italy_riders", "Alice", 1, "0-0", 1
        );

        Console.WriteLine($"{res30.NextStartId}, ({string.Join(", ", res30.ClaimedEntries.Select(entry => $"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"))})");
        // >>> 1712744379676-0, (1712744358384-0: [rider: Royce])
```

##### Go

```go
	res30, res30a, err := rdb.XAutoClaim(ctx, &redis.XAutoClaimArgs{
		Stream:   "race:italy",
		Group:    "italy_riders",
		Consumer: "Alice",
		Start:    "0-0",
		Count:    1,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res30)  // >>> [{1692632647899-0 map[rider:Royce] 0 0}]
	fmt.Println(res30a) // >>> 1692632662819-0
```

##### Java (Synchronous - Jedis)

```java
    Map.Entry<StreamEntryID, List<StreamEntry>> res30 = jedis.xautoclaim("race:italy","italy_riders","Alice",1L,new StreamEntryID("0-0"),XAutoClaimParams.xAutoClaimParams().count(1));
    System.out.println(res30); // >>> [1701769266831-2=[1701769266831-1 {rider=Royce}]
```

##### JavaScript (Node.js)

```javascript
const res29 = await client.xAutoClaim('race:italy', 'italy_riders', 'Alice', 1, '0-0', {
  COUNT: 1
});
console.log(res29); // >>> { nextId: '1692629925790-0', messages: [{ id: '1692629925789-0', message: { rider: 'Royce' } }], deletedMessages: [] }
```

##### Python

```python
res29 = r.xautoclaim("race:italy", "italy_riders", "Alice", 1, "0-0", 1)
print(res29)  # >>> ['1692629925790-0', [('1692629925789-0', {'rider': 'Royce'})]]
```

##### Ruby

```ruby
res29 = r.xautoclaim('race:italy', 'italy_riders', 'Alice', 0, '0-0', count: 1)
puts res29.inspect
# >>> {"next" => "1692632662819-0", "entries"=>[["1692632647899-0", {"rider" => "Royce"}]]}
```

##### Rust (Asynchronous)

```rust
        let opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r
            .xautoclaim_options("race:italy", "italy_riders", "Alice", 1, "0-0", opts)
            .await
        {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("1692632662819-0", [("1692632647899-0", [("rider", "Royce")])])
        }
```

##### Rust (Synchronous)

```rust
        let opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r.xautoclaim_options("race:italy", "italy_riders", "Alice", 1, "0-0", opts) {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("1692632662819-0", [("1692632647899-0", [("rider", "Royce")])])
        }
```



Like [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim), the command replies with an array of the claimed messages, but it also returns a stream ID that allows iterating the pending entries.
The stream ID is a cursor, and I can use it in my next call to continue in claiming idle pending messages:

Continue automatic claiming using the cursor returned by XAUTOCLAIM to iterate through pending messages

**Difficulty:** Advanced

**Commands:** XAUTOCLAIM

**Complexity:**
- XAUTOCLAIM: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XAUTOCLAIM race:italy italy_riders Lora 60000 (1692632662819-0 COUNT 1
1) "1692632662819-0"
2) 1) 1) "1692632647899-0"
      2) 1) "rider"
         2) "Royce"
```

##### C#

```csharp
        StreamAutoClaimResult res31 = db.StreamAutoClaim(
            "race:italy", "italy_riders", "Alice", 1, "(1712744358384-0", 1
        );

        Console.WriteLine($"{res31.NextStartId}, ({string.Join(", ", res31.ClaimedEntries.Select(entry => $"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"))})");
        // >>> 0-0, (1712744379676-0: [rider: Sam-Bodden])
```

##### Go

```go
	res31, res31a, err := rdb.XAutoClaim(ctx, &redis.XAutoClaimArgs{
		Stream:   "race:italy",
		Group:    "italy_riders",
		Consumer: "Lora",
		Start:    "(1692632662819-0",
		Count:    1,
	}).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res31)  // >>> []
	fmt.Println(res31a) // >>> 0-0
```

##### Java (Synchronous - Jedis)

```java
    Map.Entry<StreamEntryID, List<StreamEntry>> res31 = jedis.xautoclaim("race:italy","italy_riders","Alice",1L,new StreamEntryID(id2.toString()),XAutoClaimParams.xAutoClaimParams().count(1));
    System.out.println(res31); // >>> [0-0=[1701769605847-2 {rider=Sam-Bodden}]
```

##### JavaScript (Node.js)

```javascript
const res30 = await client.xAutoClaim(
  'race:italy', 'italy_riders', 'Alice', 1, '(1692629925789-0',
  {
    COUNT: 1
  }
);
console.log(res30); // >>> { nextId: '0-0', messages: [{ id: '1692629925790-0', message: { rider: 'Sam-Bodden' } }], deletedMessages: [] }
```

##### Python

```python
res30 = r.xautoclaim("race:italy", "italy_riders", "Alice", 1, "(1692629925789-0", 1)
print(res30)  # >>> ['0-0', [('1692629925790-0', {'rider': 'Sam-Bodden'})]]
```

##### Ruby

```ruby
res30 = r.xautoclaim('race:italy', 'italy_riders', 'Lora', 0, res29['next'], count: 1)
puts res30.inspect
# >>> {"next" => "0-0", "entries"=>[["1692632662819-0", {"rider" => "Sam-Bodden"}]]}
```

##### Rust (Asynchronous)

```rust
        let next_opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r
            .xautoclaim_options(
                "race:italy",
                "italy_riders",
                "Lora",
                1,
                "(1692632647899-0",
                next_opts,
            )
            .await
        {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("0-0", [("1692632662819-0", [("rider", "Sam-Bodden")])])
        }
```

##### Rust (Synchronous)

```rust
        let next_opts = StreamAutoClaimOptions::default().count(1);
        if let Ok(res) = r.xautoclaim_options(
            "race:italy",
            "italy_riders",
            "Lora",
            1,
            "(1692632647899-0",
            next_opts,
        ) {
            let res: redis::streams::StreamAutoClaimReply = res;
            let claimed: Vec<_> = res
                .claimed
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{:?}", (res.next_stream_id.clone(), &claimed));
            // >>> ("0-0", [("1692632662819-0", [("rider", "Sam-Bodden")])])
        }
```



When [`XAUTOCLAIM`](https://redis.io/docs/latest/commands/xautoclaim) returns the "0-0" stream ID as a cursor, that means that it reached the end of the consumer group pending entries list.
That doesn't mean that there are no new idle pending messages, so the process continues by calling [`XAUTOCLAIM`](https://redis.io/docs/latest/commands/xautoclaim) from the beginning of the stream.

## Claiming and the delivery counter

The counter that you observe in the [`XPENDING`](https://redis.io/docs/latest/commands/xpending) output is the number of deliveries of each message. The counter is incremented in two ways: when a message is successfully claimed via [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim) or when an [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) call is used in order to access the history of pending messages.

When there are failures, it is normal that messages will be delivered multiple times, but eventually they usually get processed and acknowledged. However there might be a problem processing some specific message, because it is corrupted or crafted in a way that triggers a bug in the processing code. In such a case what happens is that consumers will continuously fail to process this particular message. Because we have the counter of the delivery attempts, we can use that counter to detect messages that for some reason are not processable. So once the deliveries counter reaches a given large number that you chose, it is probably wiser to put such messages in another stream and send a notification to the system administrator. This is basically the way that Redis Streams implements the *dead letter* concept.

## Releasing messages back to the group: XNACK

Starting with Redis 8.8, the [`XNACK`](https://redis.io/docs/latest/commands/xnack) command provides a way for consumers to explicitly release pending messages back to the group without acknowledging them. This is the opposite of claiming - instead of taking ownership of messages from other consumers, a consumer can release its own messages back to the group for immediate re-delivery.

This capability addresses several common scenarios:

1. **Graceful shutdown**: When a consumer is shutting down, it can release all its pending messages so other consumers can pick them up immediately without waiting for idle timeouts.

2. **Consumer-side failures**: When a consumer encounters consumer-side issues (like network connectivity problems or resource constraints), it can release messages it cannot process rather than letting them sit idle.

3. **Resource management**: A consumer under resource pressure can release complex or large messages that it cannot handle, allowing other consumers with more resources to process them.

4. **Poison message handling**: A consumer can mark messages as permanently failed when it detects invalid or malicious content.

The command provides three modes that control how the delivery counter is adjusted:

- **SILENT**: Decrements the delivery counter, essentially "undoing" the delivery. Use this for graceful shutdowns or when the failure is unrelated to the message content.
- **FAIL**: Keeps the delivery counter unchanged. Use this when the current consumer cannot handle the message but others might be able to.
- **FATAL**: Sets the delivery counter to maximum value, marking the message as permanently failed for dead letter processing.

Released messages are placed in a special "NACK zone" at the head of the consumer group's PEL, ensuring they are prioritized for re-delivery over other idle pending messages. This makes recovery much faster than traditional claiming mechanisms that rely on idle timeouts.

```
> XNACK mystream mygroup FAIL IDS 1 1526569498055-0
(integer) 1
```

After NACKing, the message appears with an empty consumer in [`XPENDING`](https://redis.io/docs/latest/commands/xpending) output and becomes immediately available for claiming or consumption via [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) with the CLAIM option.

## Working with multiple consumer groups

Redis Streams can be associated with multiple consumer groups, where each entry is delivered to all the stream's consumer groups. Within each consumer group, consumers handle a portion of the entries collaboratively. This design enables different applications or services to process the same stream data independently.

Traditionally, when a consumer processesed a message, it acknowledged it using the [`XACK`](https://redis.io/docs/latest/commands/xack) command, which removed the entry reference from the Pending Entries List (PEL) of that specific consumer group. However, the entry remained in the stream and in the PELs of other consumer groups until they also acknowledge it. Applications needed to implement complex logic to delete entries from the stream only after all consumer groups had acknowledged them. This coordination was challenging to implement correctly and efficiently.

### Enhanced deletion control in Redis 8.2

Starting with Redis 8.2, several commands provide enhanced control over how entries are handled with respect to multiple consumer groups:

* [`XADD`](https://redis.io/docs/latest/commands/xadd) with trimming options now supports `KEEPREF`, `DELREF`, and `ACKED` modes
* [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) supports the same reference handling options
* [`XDELEX`](https://redis.io/docs/latest/commands/xdelex) provides fine-grained deletion control
* [`XACKDEL`](https://redis.io/docs/latest/commands/xackdel) combines acknowledgment and deletion atomically

These options control how consumer group references are handled:

- **KEEPREF** (default): Preserves existing references to entries in all consumer groups' PELs, maintaining backward compatibility
- **DELREF**: Removes all references to entries from all consumer groups' PELs, effectively cleaning up all traces of the messages
- **ACKED**: Only processes entries that have been acknowledged by all consumer groups

The `ACKED` option is particularly useful as it automates the complex logic of coordinating deletion across multiple consumer groups, ensuring entries are only removed when all groups have finished processing them.

## Streams observability

Messaging systems that lack observability are very hard to work with. Not knowing who is consuming messages, what messages are pending, the set of consumer groups active in a given stream, makes everything opaque. For this reason, Redis Streams and consumer groups have different ways to observe what is happening. We already covered [`XPENDING`](https://redis.io/docs/latest/commands/xpending), which allows us to inspect the list of messages that are under processing at a given moment, together with their idle time and number of deliveries.

However we may want to do more than that, and the [`XINFO`](https://redis.io/docs/latest/commands/xinfo) command is an observability interface that can be used with sub-commands in order to get information about streams or consumer groups.

This command uses subcommands in order to show different information about the status of the stream and its consumer groups. For instance **XINFO STREAM <key>** reports information about the stream itself.

Get detailed stream information including length, encoding, and consumer groups using XINFO STREAM

**Difficulty:** Intermediate

**Commands:** XINFO

**Complexity:**
- XINFO: Depends on subcommand

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XINFO STREAM race:italy
 1) "length"
 2) (integer) 5
 3) "radix-tree-keys"
 4) (integer) 1
 5) "radix-tree-nodes"
 6) (integer) 2
 7) "last-generated-id"
 8) "1692632678249-0"
 9) "groups"
10) (integer) 1
11) "first-entry"
12) 1) "1692632639151-0"
    2) 1) "rider"
       2) "Castilla"
13) "last-entry"
14) 1) "1692632678249-0"
    2) 1) "rider"
       2) "Norem"
```

##### C#

```csharp
        StreamInfo res32 = db.StreamInfo("race:italy");
        Console.WriteLine($"length: {res32.Length}, radix-tree-keys: {res32.RadixTreeKeys}, radix-tree-nodes: {res32.RadixTreeNodes}, last-generated-id: {res32.LastGeneratedId}, first-entry: {$"{res32.FirstEntry.Id}: [{string.Join(", ", res32.FirstEntry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"}, last-entry: {$"{res32.LastEntry.Id}: [{string.Join(", ", res32.LastEntry.Values.Select(b => $"{b.Name}: {b.Value}"))}]"}");
        // >>> length: 5, radix-tree-keys: 1, radix-tree-nodes: 2, last-generated-id: 1712756762686-1, first-entry: 1712756762685-0: [rider: Castilla], last-entry: 1712756762686-1: [rider: Norem]
```

##### Go

```go
	res33, err := rdb.XInfoStream(ctx, "race:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res33.Length)
	// >>> 5
	fmt.Println(res33.FirstEntry)
	// >>> {1692632639151-0 map[rider:Castilla] 0 0}
```

##### Java (Synchronous - Jedis)

```java
    StreamInfo res32 = jedis.xinfoStream("race:italy");
    System.out.println(
      res32.getStreamInfo()
    ); // >>> {radix-tree-keys=1, radix-tree-nodes=2, entries-added=5, length=5, groups=1, max-deleted-entry-id=0-0, first-entry=1701769637612-0 {rider=Castilaa}, last-generated-id=1701769637612-4, last-entry=1701769637612-4 {rider=Norem}, recorded-first-entry-id=1701769637612-0}
```

##### JavaScript (Node.js)

```javascript
const res31 = await client.xInfoStream('race:italy');
console.log(res31); // >>> { length: 5, 'radix-tree-keys': 1, 'radix-tree-nodes': 2, 'last-generated-id': '1692629926436-0', 'max-deleted-entry-id': '0-0', 'entries-added': 5, 'recorded-first-entry-id': '1692629925771-0', groups: 1, 'first-entry': { id: '1692629925771-0', message: { rider: 'Castilla' } }, 'last-entry': { id: '1692629926436-0', message: { rider: 'Norem' } } }
```

##### Python

```python
res31 = r.xinfo_stream("race:italy")
print(
    res31
)
# >>> {
#       'length': 5, 'radix-tree-keys': 1, 'radix-tree-nodes': 2,
#       'last-generated-id': '1692629926436-0', 'groups': 1,
#       'first-entry': ('1692629925771-0', {'rider': 'Castilla'}),
#       'last-entry': ('1692629926436-0', {'rider': 'Norem'})
# }
```

##### Ruby

```ruby
res31 = r.xinfo(:stream, 'race:italy')
puts res31.inspect
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xinfo_stream("race:italy").await {
            let res: StreamInfoStreamReply = res;
            let view = (
                res.length,
                res.radix_tree_keys,
                res.groups,
                res.last_generated_id.clone(),
                res.first_entry.id.clone(),
                res.last_entry.id.clone(),
            );
            println!("{view:?}");
            // >>> (5, 1, 1, "1692632678249-0", "1692632639151-0", "1692632678249-0")
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xinfo_stream("race:italy") {
            let res: StreamInfoStreamReply = res;
            let view = (
                res.length,
                res.radix_tree_keys,
                res.groups,
                res.last_generated_id.clone(),
                res.first_entry.id.clone(),
                res.last_entry.id.clone(),
            );
            println!("{view:?}");
            // >>> (5, 1, 1, "1692632678249-0", "1692632639151-0", "1692632678249-0")
        }
```



The output shows information about how the stream is encoded internally, and also shows the first and last message in the stream. Another piece of information available is the number of consumer groups associated with this stream. We can dig further asking for more information about the consumer groups.

List all consumer groups for a stream using XINFO GROUPS to see group status and pending message counts

**Difficulty:** Intermediate

**Commands:** XINFO

**Complexity:**
- XINFO: Depends on subcommand

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XINFO GROUPS race:italy
1) 1) "name"
   2) "italy_riders"
   3) "consumers"
   4) (integer) 3
   5) "pending"
   6) (integer) 2
   7) "last-delivered-id"
   8) "1692632662819-0"
```

##### C#

```csharp
        StreamGroupInfo[] res33 = db.StreamGroupInfo("race:italy");

        foreach (StreamGroupInfo info in res33)
        {
            Console.WriteLine($"name: {info.Name}, consumers: {info.ConsumerCount}, pending: {info.PendingMessageCount}, last-delivered-id: {info.LastDeliveredId}");
        }
        // >>> name: italy_riders, consumers: 2, pending: 2, last-delivered-id: 1712757192730-2
```

##### Go

```go
	res34, err := rdb.XInfoGroups(ctx, "race:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res34)
	// >>> [{italy_riders 3 2 1692632662819-0 3 2}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamGroupInfo> res33 = jedis.xinfoGroups("race:italy");
    for (StreamGroupInfo a : res33){
      System.out.println(
        a.getGroupInfo()
      ); // >>> {last-delivered-id=1701770253659-0, lag=2, pending=2, name=italy_riders, consumers=2, entries-read=3}
    }
```

##### JavaScript (Node.js)

```javascript
const res32 = await client.xInfoGroups('race:italy');
console.log(res32); // >>> [{ name: 'italy_riders', consumers: 2, pending: 3, 'last-delivered-id': '1692629925790-0', 'entries-read': 3, lag: 2 }]
```

##### Python

```python
res32 = r.xinfo_groups("race:italy")
print(
    res32
)
# >>> [
#       {
#           'name': 'italy_riders', 'consumers': 2, 'pending': 2,
#           'last-delivered-id': '1692629925790-0'
#       }
# ]
```

##### Ruby

```ruby
res32 = r.xinfo(:groups, 'race:italy')
puts res32.inspect
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xinfo_groups("race:italy").await {
            let res: StreamInfoGroupsReply = res;
            let view: Vec<_> = res
                .groups
                .iter()
                .map(|group| {
                    (
                        group.name.clone(),
                        group.consumers,
                        group.pending,
                        group.last_delivered_id.clone(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("italy_riders", 3, 2, "1692632662819-0")]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xinfo_groups("race:italy") {
            let res: StreamInfoGroupsReply = res;
            let view: Vec<_> = res
                .groups
                .iter()
                .map(|group| {
                    (
                        group.name.clone(),
                        group.consumers,
                        group.pending,
                        group.last_delivered_id.clone(),
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("italy_riders", 3, 2, "1692632662819-0")]
        }
```



As you can see in this and in the previous output, the [`XINFO`](https://redis.io/docs/latest/commands/xinfo) command outputs a sequence of field-value items. Because it is an observability command this allows the human user to immediately understand what information is reported, and allows the command to report more information in the future by adding more fields without breaking compatibility with older clients. Other commands that must be more bandwidth efficient, like [`XPENDING`](https://redis.io/docs/latest/commands/xpending), just report the information without the field names.

The output of the example above, where the **GROUPS** subcommand is used, should be clear observing the field names. We can check in more detail the state of a specific consumer group by checking the consumers that are registered in the group.

Get detailed consumer information for a group using XINFO CONSUMERS to monitor individual consumer status

**Difficulty:** Advanced

**Commands:** XINFO

**Complexity:**
- XINFO: Depends on subcommand

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XINFO CONSUMERS race:italy italy_riders
1) 1) "name"
   2) "Alice"
   3) "pending"
   4) (integer) 1
   5) "idle"
   6) (integer) 177546
2) 1) "name"
   2) "Bob"
   3) "pending"
   4) (integer) 0
   5) "idle"
   6) (integer) 424686
3) 1) "name"
   2) "Lora"
   3) "pending"
   4) (integer) 1
   5) "idle"
   6) (integer) 72241
```

##### C#

```csharp
        StreamConsumerInfo[] res34 = db.StreamConsumerInfo("race:italy", "italy_riders");

        foreach (StreamConsumerInfo info in res34)
        {
            Console.WriteLine($"name: {info.Name}, pending: {info.PendingMessageCount}, idle: {info.IdleTimeInMilliseconds}");
        }
        // >>> name: Alice, pending: 1, idle: 7717
        // >>> name: Bob, pending: 0, idle: 7722
```

##### Go

```go
	res35, err := rdb.XInfoConsumers(ctx, "race:italy", "italy_riders").Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res35)
	// >>> [{Alice 1 1ms 1ms} {Bob 1 2ms 2ms} {Lora 0 1ms -1ms}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamConsumersInfo> res34 = jedis.xinfoConsumers("race:italy","italy_riders");
    for (StreamConsumerInfo a : res34){
      System.out.println(
        a.getConsumerInfo()
      ); // {inactive=1, idle=1, pending=1, name=Alice} , {inactive=3, idle=3, pending=1, name=Bob}
    }
```

##### JavaScript (Node.js)

```javascript
const res33 = await client.xInfoConsumers('race:italy', 'italy_riders');
console.log(res33); // >>> [{ name: 'Alice', pending: 3, idle: 170582, inactive: 170582 }, { name: 'Bob', pending: 0, idle: 489404, inactive: 489404 }]
```

##### Python

```python
res33 = r.xinfo_consumers("race:italy", "italy_riders")
print(
    res33
)
# >>> [
#       {'name': 'Alice', 'pending': 2, 'idle': 199332},
#       {'name': 'Bob', 'pending': 0, 'idle': 489170}
# ]
```

##### Ruby

```ruby
res33 = r.xinfo(:consumers, 'race:italy', 'italy_riders')
puts res33.inspect
```

##### Rust (Asynchronous)

```rust
        if let Ok(res) = r.xinfo_consumers("race:italy", "italy_riders").await {
            let res: StreamInfoConsumersReply = res;
            let mut view: Vec<_> = res
                .consumers
                .iter()
                .map(|consumer| (consumer.name.clone(), consumer.pending, consumer.idle))
                .collect();
            view.sort_by(|a, b| a.0.cmp(&b.0));
            println!("{view:?}");
            // >>> [("Alice", 1, 5), ("Bob", 0, 5), ("Lora", 1, 5)]
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res) = r.xinfo_consumers("race:italy", "italy_riders") {
            let res: StreamInfoConsumersReply = res;
            let mut view: Vec<_> = res
                .consumers
                .iter()
                .map(|consumer| (consumer.name.clone(), consumer.pending, consumer.idle))
                .collect();
            view.sort_by(|a, b| a.0.cmp(&b.0));
            println!("{view:?}");
            // >>> [("Alice", 1, 5), ("Bob", 0, 5), ("Lora", 1, 5)]
        }
```



In case you do not remember the syntax of the command, just ask the command itself for help:

```
> XINFO HELP
1) XINFO <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
2) CONSUMERS <key> <groupname>
3)     Show consumers of <groupname>.
4) GROUPS <key>
5)     Show the stream consumer groups.
6) STREAM <key> [FULL [COUNT <count>]
7)     Show information about the stream.
8) HELP
9)     Prints this help.
```

## Differences with Kafka (TM) partitions

Consumer groups in Redis streams may resemble in some way Kafka (TM) partitioning-based consumer groups, however note that Redis streams are, in practical terms, very different. The partitions are only *logical* and the messages are just put into a single Redis key, so the way the different clients are served is based on who is ready to process new messages, and not from which partition clients are reading. For instance, if the consumer C3 at some point fails permanently, Redis will continue to serve C1 and C2 all the new messages arriving, as if now there are only two *logical* partitions.

Similarly, if a given consumer is much faster at processing messages than the other consumers, this consumer will receive proportionally more messages in the same unit of time. This is possible since Redis tracks all the unacknowledged messages explicitly, and remembers who received which message and the ID of the first message never delivered to any consumer.

However, this also means that in Redis if you really want to partition messages in the same stream into multiple Redis instances, you have to use multiple keys and some sharding system such as Redis Cluster or some other application-specific sharding system. A single Redis stream is not automatically partitioned to multiple instances.

We could say that schematically the following is true:

* If you use 1 stream -> 1 consumer, you are processing messages in order.
* If you use N streams with N consumers, so that only a given consumer hits a subset of the N streams, you can scale the above model of 1 stream -> 1 consumer.
* If you use 1 stream -> N consumers, you are load balancing to N consumers, however in that case, messages about the same logical item may be consumed out of order, because a given consumer may process message 3 faster than another consumer is processing message 4.

So basically Kafka partitions are more similar to using N different Redis keys, while Redis consumer groups are a server-side load balancing system of messages from a given stream to N different consumers.

## Capped Streams

Many applications do not want to collect data into a stream forever. Sometimes it is useful to have at maximum a given number of items inside a stream, other times once a given size is reached, it is useful to move data from Redis to a storage which is not in memory and not as fast but suited to store the history for, potentially, decades to come. Redis streams have some support for this. One is the **MAXLEN** option of the [`XADD`](https://redis.io/docs/latest/commands/xadd) command. This option is very simple to use:

Limit stream size using MAXLEN option with XADD to automatically evict old entries and maintain constant memory usage

**Difficulty:** Intermediate

**Commands:** XADD, XLEN, XRANGE

**Complexity:**
- XADD: O(1)
- XLEN: O(1)
- XRANGE: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XADD race:italy MAXLEN 2 * rider Jones
"1692633189161-0"
> XADD race:italy MAXLEN 2 * rider Wood
"1692633198206-0"
> XADD race:italy MAXLEN 2 * rider Henshaw
"1692633208557-0"
> XLEN race:italy
(integer) 2
> XRANGE race:italy - +
1) 1) "1692633198206-0"
   2) 1) "rider"
      2) "Wood"
2) 1) "1692633208557-0"
   2) 1) "rider"
      2) "Henshaw"
```

##### C#

```csharp
        db.StreamAdd(
            "race:italy", [new("rider", "Jones")], null, 2, true
        );

        db.StreamAdd(
            "race:italy", [new("rider", "Wood")], null, 2, true
        );

        db.StreamAdd(
            "race:italy", [new("rider", "Henshaw")], null, 2, true
        );

        long res35 = db.StreamLength("race:italy");
        Console.WriteLine(res35); // >>> 8

        StreamEntry[] res36 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res36)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712758336128-0: [rider: Castilla]
        // >>> 1712758336128-1: [rider: Royce]
        // >>> 1712758336128-2: [rider: Sam-Bodden]
        // >>> 1712758336129-0: [rider: Prickett]
        // >>> 1712758336139-0: [rider: Norem]
        // >>> 1712758340854-0: [rider: Jones]
        // >>> 1712758341645-0: [rider: Wood]
        // >>> 1712758342134-0: [rider: Henshaw]

        db.StreamAdd(
            "race:italy", [new("rider", "Smith")], null, 2, false
        );

        StreamEntry[] res37 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res37)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // 1712758746476-1: [rider: Henshaw]
        // 1712758746477-0: [rider: Smith]
```

##### Go

```go
	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		MaxLen: 2,
		Values: map[string]interface{}{"rider": "Jones"},
	},
	).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		MaxLen: 2,
		Values: map[string]interface{}{"rider": "Wood"},
	},
	).Result()

	if err != nil {
		panic(err)
	}

	_, err = rdb.XAdd(ctx, &redis.XAddArgs{
		Stream: "race:italy",
		MaxLen: 2,
		Values: map[string]interface{}{"rider": "Henshaw"},
	},
	).Result()

	if err != nil {
		panic(err)
	}

	res36, err := rdb.XLen(ctx, "race:italy").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res36) // >>> 2

	res37, err := rdb.XRange(ctx, "race:italy", "-", "+").Result()

	if err != nil {
		panic(err)
	}

	// fmt.Println(res37)
	// >>> [{1726649529170-1 map[rider:Wood] 0 0} {1726649529171-0 map[rider:Henshaw] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Jones");}},XAddParams.xAddParams().maxLen(10));
    jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Wood");}},XAddParams.xAddParams().maxLen(10));
    jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Henshaw");}},XAddParams.xAddParams().maxLen(10));
    long res35 = jedis.xlen("race:italy");
    System.out.println(res35); // >>> 8

    List<StreamEntry> res36 = jedis.xrange("race:italy","-","+");
    System.out.println(res36); // >>> [1701771219852-0 {rider=Castilaa}, 1701771219852-1 {rider=Royce}, 1701771219853-0 {rider=Sam-Bodden}, 1701771219853-1 {rider=Prickett}, 1701771219853-2 {rider=Norem}, 1701771219858-0 {rider=Jones}, 1701771219858-1 {rider=Wood}, 1701771219859-0 {rider=Henshaw}]

    StreamEntryID id6 = jedis.xadd("race:italy", new HashMap<String,String>(){{put("rider","Smith");}},XAddParams.xAddParams().maxLen(2));

    List<StreamEntry> res37 = jedis.xrange("race:italy","-","+");
    System.out.println(res37); // >>> [1701771067332-1 {rider=Henshaw}, 1701771067332-2 {rider=Smith}]
```

##### JavaScript (Node.js)

```javascript
await client.xAdd('race:italy', '*', {
  'rider': 'Jones'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '~',
    threshold: 2
  }
});
await client.xAdd('race:italy', '*', {
  'rider': 'Wood'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '~',
    threshold: 2
  }
});
await client.xAdd('race:italy', '*', {
  'rider': 'Henshaw'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '~',
    threshold: 2
  }
});

const res34 = await client.xLen('race:italy');
console.log(res34); // >>> 8

const res35 = await client.xRange('race:italy', '-', '+');
console.log(res35); // >>> [{ id: '1692629925771-0', message: { rider: 'Castilla' } }, { id: '1692629925789-0', message: { rider: 'Royce' } }, { id: '1692629925790-0', message: { rider: 'Sam-Bodden' } }, { id: '1692629925791-0', message: { rider: 'Prickett' } }, { id: '1692629926436-0', message: { rider: 'Norem' } }, { id: '1692630612602-0', message: { rider: 'Jones' } }, { id: '1692630641947-0', message: { rider: 'Wood' } }, { id: '1692630648281-0', message: { rider: 'Henshaw' } }]

await client.xAdd('race:italy', '*', {
  'rider': 'Smith'
}, {
  TRIM: {
    strategy: 'MAXLEN',
    strategyModifier: '=',
    threshold: 2
  }
});

const res36 = await client.xRange('race:italy', '-', '+');
console.log(res36); // >>> [{ id: '1692630648281-0', message: { rider: 'Henshaw' } }, { id: '1692631018238-0', message: { rider: 'Smith' } }]
```

##### Python

```python
r.xadd("race:italy", {"rider": "Jones"}, maxlen=2)
r.xadd("race:italy", {"rider": "Wood"}, maxlen=2)
r.xadd("race:italy", {"rider": "Henshaw"}, maxlen=2)

res34 = r.xlen("race:italy")
print(res34)  # >>> 8

res35 = r.xrange("race:italy", "-", "+")
print(
    res35
)
# >>> [
#       ('1692629925771-0', {'rider': 'Castilla'}),
#       ('1692629925789-0', {'rider': 'Royce'}),
#       ('1692629925790-0', {'rider': 'Sam-Bodden'}),
#       ('1692629925791-0', {'rider': 'Prickett'}),
#       ('1692629926436-0', {'rider': 'Norem'}),
#       ('1692630612602-0', {'rider': 'Jones'}),
#       ('1692630641947-0', {'rider': 'Wood'}),
#       ('1692630648281-0', {'rider': 'Henshaw'})
# ]

r.xadd("race:italy", {"rider": "Smith"}, maxlen=2, approximate=False)

res36 = r.xrange("race:italy", "-", "+")
print(
    res36
)
# >>> [
#       ('1692630648281-0', {'rider': 'Henshaw'}),
#       ('1692631018238-0', {'rider': 'Smith'})
# ]
```

##### Ruby

```ruby
r.del('race:italy')
r.xadd('race:italy', {'rider' => 'Castilla'}, id: '1692632639151-0')
r.xadd('race:italy', {'rider' => 'Royce'}, id: '1692632647899-0')
r.xadd('race:italy', {'rider' => 'Sam-Bodden'}, id: '1692632662819-0')
r.xadd('race:italy', {'rider' => 'Prickett'}, id: '1692632670501-0')
r.xadd('race:italy', {'rider' => 'Norem'}, id: '1692632678249-0')
r.xadd('race:italy', {'rider' => 'Jones'}, id: '1692633189161-0', maxlen: 2)
r.xadd('race:italy', {'rider' => 'Wood'}, id: '1692633198206-0', maxlen: 2)
r.xadd('race:italy', {'rider' => 'Henshaw'}, id: '1692633208557-0', maxlen: 2)

res34 = r.xlen('race:italy')
puts res34 # >>> 2

res35 = r.xrange('race:italy', '-', '+')
puts res35.inspect
# >>> [["1692633198206-0", {"rider" => "Wood"}], ["1692633208557-0", {"rider" => "Henshaw"}]]
```

##### Rust (Asynchronous)

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        let max1: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "1-0", &[("rider", "Jones")])
            .await
            .expect("maxlen add 1");
        let max1 = max1.expect("missing stream id");
        println!("{max1}"); // >>> 1-0
        let max2: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "2-0", &[("rider", "Wood")])
            .await
            .expect("maxlen add 2");
        let max2 = max2.expect("missing stream id");
        println!("{max2}"); // >>> 2-0
        let max3: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "3-0", &[("rider", "Henshaw")])
            .await
            .expect("maxlen add 3");
        let max3 = max3.expect("missing stream id");
        println!("{max3}"); // >>> 3-0
        if let Ok(res) = r.xlen("race:italy").await {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }
        if let Ok(res) = r.xrange_all("race:italy").await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }
```

##### Rust (Synchronous)

```rust
        delete_keys(&mut r, &["race:italy"]);
        let max1: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "1-0", &[("rider", "Jones")])
            .expect("maxlen add 1");
        let max1 = max1.expect("missing stream id");
        println!("{max1}"); // >>> 1-0
        let max2: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "2-0", &[("rider", "Wood")])
            .expect("maxlen add 2");
        let max2 = max2.expect("missing stream id");
        println!("{max2}"); // >>> 2-0
        let max3: Option<String> = r
            .xadd_maxlen("race:italy", StreamMaxlen::Equals(2), "3-0", &[("rider", "Henshaw")])
            .expect("maxlen add 3");
        let max3 = max3.expect("missing stream id");
        println!("{max3}"); // >>> 3-0

        if let Ok(res) = r.xlen("race:italy") {
            let res: usize = res;
            println!("{res}"); // >>> 2
        }

        if let Ok(res) = r.xrange_all("race:italy") {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}");
            // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }
```



Using **MAXLEN** the old entries are automatically evicted when the specified length is reached, so that the stream is left at a constant size. There is currently no option to tell the stream to just retain items that are not older than a given period, because such command, in order to run consistently, would potentially block for a long time in order to evict items. Imagine for example what happens if there is an insertion spike, then a long pause, and another insertion, all with the same maximum time. The stream would block to evict the data that became too old during the pause. So it is up to the user to do some planning and understand what is the maximum stream length desired. Moreover, while the length of the stream is proportional to the memory used, trimming by time is less simple to control and anticipate: it depends on the insertion rate which often changes over time (and when it does not change, then to just trim by size is trivial).

However trimming with **MAXLEN** can be expensive: streams are represented by macro nodes into a radix tree, in order to be very memory efficient. Altering the single macro node, consisting of a few tens of elements, is not optimal. So it's possible to use the command in the following special form:

```
XADD race:italy MAXLEN ~ 1000 * ... entry fields here ...
```

The `~` argument between the **MAXLEN** option and the actual count means, I don't really need this to be exactly 1000 items. It can be 1000 or 1010 or 1030, just make sure to save at least 1000 items. With this argument, the trimming is performed only when we can remove a whole node. This makes it much more efficient, and it is usually what you want. You'll note here that the client libraries have various implementations of this. For example, the Python client defaults to approximate and has to be explicitly set to a true length.

There is also the [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) command, which performs something very similar to what the **MAXLEN** option does above, except that it can be run by itself:

Trim a stream to a maximum length using XTRIM MAXLEN to remove old entries

**Difficulty:** Intermediate

**Commands:** XTRIM

**Complexity:**
- XTRIM: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XTRIM race:italy MAXLEN 10
(integer) 0
```

##### C#

```csharp
        long res38 = db.StreamTrim("race:italy", 10, false);
        Console.WriteLine(res38);   // >>> 0
```

##### Go

```go
	res38, err := rdb.XTrimMaxLen(ctx, "race:italy", 10).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res38) // >>> 0
```

##### Java (Synchronous - Jedis)

```java
    long res38 = jedis.xtrim("race:italy",XTrimParams.xTrimParams().maxLen(10).exactTrimming());
    System.out.println(res38); /// >>> 0
```

##### JavaScript (Node.js)

```javascript
const res37 = await client.xTrim('race:italy', 'MAXLEN', 10, {
  strategyModifier: '=',
});
console.log(res37); // >>> 0
```

##### Python

```python
res37 = r.xtrim("race:italy", maxlen=10, approximate=False)
print(res37)  # >>> 0
```

##### Ruby

```ruby
res36 = r.xtrim('race:italy', 10, approximate: false)
puts res36 # >>> 0
```

##### Rust (Asynchronous)

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        let _: Option<String> = r.xadd("race:italy", "1-0", &[("rider", "Wood")]).await.expect("trim seed 1");
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Henshaw")]).await.expect("trim seed 2");
        if let Ok(res) = r.xtrim("race:italy", StreamMaxlen::Equals(10)).await {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

##### Rust (Synchronous)

```rust
        delete_keys(&mut r, &["race:italy"]);
        let _: Option<String> = r.xadd("race:italy", "1-0", &[("rider", "Wood")]).expect("trim seed 1");
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Henshaw")]).expect("trim seed 2");
        if let Ok(res) = r.xtrim("race:italy", StreamMaxlen::Equals(10)) {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```



Or, as for the [`XADD`](https://redis.io/docs/latest/commands/xadd) option:

Use approximate trimming with XTRIM MAXLEN ~ for more efficient memory management

**Difficulty:** Intermediate

**Commands:** XTRIM

**Complexity:**
- XTRIM: O(N)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XTRIM mystream MAXLEN ~ 10
(integer) 0
```

##### C#

```csharp
        long res39 = db.StreamTrim("race:italy", 10, true);
        Console.WriteLine(res39);   // >>> 0
```

##### Go

```go
	res39, err := rdb.XTrimMaxLenApprox(ctx, "race:italy", 10, 20).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res39) // >>> 0
```

##### Java (Synchronous - Jedis)

```java
    long res39 = jedis.xtrim("race:italy",XTrimParams.xTrimParams().maxLen(10));
    System.out.println(res39); /// >>> 0
```

##### JavaScript (Node.js)

```javascript
const res38 = await client.xTrim('race:italy', "MAXLEN", 10);
console.log(res38); // >>> 0
```

##### Python

```python
res38 = r.xtrim("race:italy", maxlen=10)
print(res38)  # >>> 0
```

##### Ruby

```ruby
r.del('mystream')
1.upto(10) do |n|
  r.xadd('mystream', {'field' => 'value'}, id: "#{n}-0")
end
res37 = r.xtrim('mystream', 10, approximate: true)
puts res37 # >>> 0
```

##### Rust (Asynchronous)

```rust
        seed_trim_stream(&mut r).await;
        if let Ok(res) = r
            .xtrim_options(
                "mystream",
                &StreamTrimOptions::maxlen(StreamTrimmingMode::Approx, 10),
            )
            .await
        {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```

##### Rust (Synchronous)

```rust
        seed_trim_stream(&mut r);
        if let Ok(res) = r.xtrim_options(
            "mystream",
            &StreamTrimOptions::maxlen(StreamTrimmingMode::Approx, 10),
        ) {
            let res: usize = res;
            println!("{res}"); // >>> 0
        }
```



However, [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) is designed to accept different trimming strategies. Another trimming strategy is **MINID**, that evicts entries with IDs lower than the one specified.

As [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) is an explicit command, the user is expected to know about the possible shortcomings of different trimming strategies.

### Trimming with consumer group awareness

Starting with Redis 8.2, both [`XADD`](https://redis.io/docs/latest/commands/xadd) with trimming options and [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) support enhanced control over how trimming interacts with consumer groups through the `KEEPREF`, `DELREF`, and `ACKED` options:

```
XADD mystream KEEPREF MAXLEN 1000 * field value
XTRIM mystream ACKED MAXLEN 1000
```

- **KEEPREF** (default): Trims entries according to the strategy but preserves references in consumer group PELs
- **DELREF**: Trims entries and removes all references from consumer group PELs
- **ACKED**: Only trims entries that have been acknowledged by all consumer groups

The `ACKED` option is particularly useful for maintaining data integrity across multiple consumer groups, ensuring that entries are only removed when all groups have finished processing them.

Another useful eviction strategy that may be added to [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) in the future, is to remove by a range of IDs to ease use of [`XRANGE`](https://redis.io/docs/latest/commands/xrange) and [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) to move data from Redis to other storage systems if needed.

## Special IDs in the streams API

You may have noticed that there are several special IDs that can be used in the Redis API. Here is a short recap, so that they can make more sense in the future.

The first two special IDs are `-` and `+`, and are used in range queries with the [`XRANGE`](https://redis.io/docs/latest/commands/xrange) command. Those two IDs respectively mean the smallest ID possible (that is basically `0-1`) and the greatest ID possible (that is `18446744073709551615-18446744073709551615`). As you can see it is a lot cleaner to write `-` and `+` instead of those numbers.

Then there are APIs where we want to say, the ID of the item with the greatest ID inside the stream. This is what `$` means. So for instance if I want only new entries with [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) I use this ID to signify I already have all the existing entries, but not the new ones that will be inserted in the future. Similarly when I create or set the ID of a consumer group, I can set the last delivered item to `$` in order to just deliver new entries to the consumers in the group.

As you can see `$` does not mean `+`, they are two different things, as `+` is the greatest ID possible in every possible stream, while `$` is the greatest ID in a given stream containing given entries. Moreover APIs will usually only understand `+` or `$`, yet it was useful to avoid loading a given symbol with multiple meanings.

Another special ID is `>`, that is a special meaning only related to consumer groups and only when the [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) command is used. This special ID means that we want only entries that were never delivered to other consumers so far. So basically the `>` ID is the *last delivered ID* of a consumer group.

Finally the special ID `*`, that can be used only with the [`XADD`](https://redis.io/docs/latest/commands/xadd) command, means to auto select an ID for us for the new entry.

So we have `-`, `+`, `$`, `>` and `*`, and all have a different meaning, and most of the time, can be used in different contexts.

## Persistence, replication and message safety

A Stream, like any other Redis data structure, is asynchronously replicated to replicas and persisted into AOF and RDB files. However what may not be so obvious is that also the consumer groups full state is propagated to AOF, RDB and replicas, so if a message is pending in the master, also the replica will have the same information. Similarly, after a restart, the AOF will restore the consumer groups' state.

However note that Redis streams and consumer groups are persisted and replicated using the Redis default replication, so:

* AOF must be used with a strong fsync policy if persistence of messages is important in your application.
* By default the asynchronous replication will not guarantee that [`XADD`](https://redis.io/docs/latest/commands/xadd) commands or consumer groups state changes are replicated: after a failover something can be missing depending on the ability of replicas to receive the data from the master.
* The [`WAIT`](https://redis.io/docs/latest/commands/wait) command may be used in order to force the propagation of the changes to a set of replicas. However note that while this makes it very unlikely that data is lost, the Redis failover process as operated by Sentinel or Redis Cluster performs only a *best effort* check to failover to the replica which is the most updated, and under certain specific failure conditions may promote a replica that lacks some data.

So when designing an application using Redis streams and consumer groups, make sure to understand the semantical properties your application should have during failures, and configure things accordingly, evaluating whether it is safe enough for your use case.

## Removing single items from a stream

Streams also have a special command for removing items from the middle of a stream, just by ID. Normally for an append only data structure this may look like an odd feature, but it is actually useful for applications involving, for instance, privacy regulations. The command is called [`XDEL`](https://redis.io/docs/latest/commands/xdel) and receives the name of the stream followed by the IDs to delete:

Delete specific entries from a stream by ID using XDEL for privacy or data cleanup purposes

**Difficulty:** Advanced

**Commands:** XRANGE, XDEL

**Complexity:**
- XRANGE: O(N)
- XDEL: O(1)

**Available in:** Redis CLI, C#, Go, Java (Synchronous - Jedis), JavaScript (Node.js), Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
> XRANGE race:italy - + COUNT 2
1) 1) "1692633198206-0"
   2) 1) "rider"
      2) "Wood"
2) 1) "1692633208557-0"
   2) 1) "rider"
      2) "Henshaw"
> XDEL race:italy 1692633208557-0
(integer) 1
> XRANGE race:italy - + COUNT 2
1) 1) "1692633198206-0"
   2) 1) "rider"
      2) "Wood"
```

##### C#

```csharp
        StreamEntry[] res40 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res40)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");
        }
        // >>> 1712759694003-0: [rider: Henshaw]
        // >>> 1712759694003-1: [rider: Smith]

        long res41 = db.StreamDelete("race:italy", ["1712759694003-1"]);
        Console.WriteLine(res41);   // >>> 1

        StreamEntry[] res42 = db.StreamRange("race:italy", "-", "+");

        foreach (StreamEntry entry in res42)
        {
            Console.WriteLine($"{entry.Id}: [{string.Join(", ", entry.Values.Select(b => $"{b.Name}: {b.Value}"))}]");

        }
        // >>> 1712759694003-0: [rider: Henshaw]
```

##### Go

```go
	res39, err := rdb.XRangeN(ctx, "race:italy", "-", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res39)
	// >>> [{1692633198206-0 map[rider:Wood] 0 0} {1692633208557-0 map[rider:Henshaw] 0 0}]

	res40, err := rdb.XDel(ctx, "race:italy", "1692633208557-0").Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res40) // 1

	res41, err := rdb.XRangeN(ctx, "race:italy", "-", "+", 2).Result()

	if err != nil {
		panic(err)
	}

	fmt.Println(res41)
	// >>> [{1692633198206-0 map[rider:Wood] 0 0}]
```

##### Java (Synchronous - Jedis)

```java
    List<StreamEntry> res40 = jedis.xrange("race:italy","-","+");
    System.out.println(res40); // >>> [1701771356428-2 {rider=Henshaw}, 1701771356429-0 {rider=Smith}]

    long res41 = jedis.xdel("race:italy",id6);
    System.out.println(res41); // >>> 1

    List<StreamEntry> res42 = jedis.xrange("race:italy","-","+");
    System.out.println(res42); // >>> [1701771517639-1 {rider=Henshaw}]
```

##### JavaScript (Node.js)

```javascript
const res39 = await client.xRange('race:italy', '-', '+');
console.log(res39); // >>> [{ id: '1692630648281-0', message: { rider: 'Henshaw' } }, { id: '1692631018238-0', message: { rider: 'Smith' } }]

const res40 = await client.xDel('race:italy', '1692631018238-0');
console.log(res40); // >>> 1

const res41 = await client.xRange('race:italy', '-', '+');
console.log(res41); // >>> [{ id: '1692630648281-0', message: { rider: 'Henshaw' } }]
```

##### Python

```python
res39 = r.xrange("race:italy", "-", "+")
print(
    res39
)
# >>> [
#       ('1692630648281-0', {'rider': 'Henshaw'}),
#       ('1692631018238-0', {'rider': 'Smith'})
# ]

res40 = r.xdel("race:italy", "1692631018238-0")
print(res40)  # >>> 1

res41 = r.xrange("race:italy", "-", "+")
print(res41)  # >>> [('1692630648281-0', {'rider': 'Henshaw'})]
```

##### Ruby

```ruby
r.del('race:italy')
r.xadd('race:italy', {'rider' => 'Wood'}, id: '1692633198206-0')
r.xadd('race:italy', {'rider' => 'Henshaw'}, id: '1692633208557-0')
res38 = r.xrange('race:italy', '-', '+', count: 2)
puts res38.inspect
# >>> [["1692633198206-0", {"rider" => "Wood"}], ["1692633208557-0", {"rider" => "Henshaw"}]]

res39 = r.xdel('race:italy', '1692633208557-0')
puts res39 # >>> 1

res40 = r.xrange('race:italy', '-', '+', count: 2)
puts res40.inspect
# >>> [["1692633198206-0", {"rider" => "Wood"}]]
```

##### Rust (Asynchronous)

```rust
        delete_keys(&mut r, &["race:italy"]).await;
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Wood")]).await.expect("xdel seed 1");
        let _: Option<String> = r.xadd("race:italy", "3-0", &[("rider", "Henshaw")]).await.expect("xdel seed 2");
        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }
        if let Ok(res) = r.xdel("race:italy", &["3-0"]).await {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }
        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2).await {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")])]
        }
```

##### Rust (Synchronous)

```rust
        delete_keys(&mut r, &["race:italy"]);
        let _: Option<String> = r.xadd("race:italy", "2-0", &[("rider", "Wood")]).expect("xdel seed 1");
        let _: Option<String> = r.xadd("race:italy", "3-0", &[("rider", "Henshaw")]).expect("xdel seed 2");
        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")]), ("3-0", [("rider", "Henshaw")])]
        }

        if let Ok(res) = r.xdel("race:italy", &["3-0"]) {
            let res: usize = res;
            println!("{res}"); // >>> 1
        }

        if let Ok(res) = r.xrange_count("race:italy", "-", "+", 2) {
            let res: StreamRangeReply = res;
            let view: Vec<_> = res
                .ids
                .iter()
                .map(|entry| {
                    (
                        entry.id.clone(),
                        vec![(
                            "rider".to_string(),
                            entry.get::<String>("rider").expect("missing rider"),
                        )],
                    )
                })
                .collect();
            println!("{view:?}"); // >>> [("2-0", [("rider", "Wood")])]
        }
```



### Enhanced deletion with XDELEX

Starting with Redis 8.2, the [`XDELEX`](https://redis.io/docs/latest/commands/xdelex) command provides enhanced control over entry deletion, particularly when working with consumer groups. Like other enhanced commands, it supports `KEEPREF`, `DELREF`, and `ACKED` options:

```
XDELEX mystream ACKED IDS 2 1692633198206-0 1692633208557-0
```

This allows you to delete entries only when they have been acknowledged by all consumer groups (`ACKED`), remove all consumer group references (`DELREF`), or preserve existing references (`KEEPREF`).

## Zero length streams

A difference between streams and other Redis data structures is that when the other data structures no longer have any elements, as a side effect of calling commands that remove elements, the key itself will be removed. So for instance, a sorted set will be completely removed when a call to [`ZREM`](https://redis.io/docs/latest/commands/zrem) will remove the last element in the sorted set. Streams, on the other hand, are allowed to stay at zero elements, both as a result of using a **MAXLEN** option with a count of zero ([`XADD`](https://redis.io/docs/latest/commands/xadd) and [`XTRIM`](https://redis.io/docs/latest/commands/xtrim) commands), or because [`XDEL`](https://redis.io/docs/latest/commands/xdel) was called.

The reason why such an asymmetry exists is because Streams may have associated consumer groups, and we do not want to lose the state that the consumer groups defined just because there are no longer any items in the stream. Currently the stream is not deleted even when it has no associated consumer groups.

## Total latency of consuming a message

Non blocking stream commands like [`XRANGE`](https://redis.io/docs/latest/commands/xrange) and [`XREAD`](https://redis.io/docs/latest/commands/xread) or [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) without the BLOCK option are served synchronously like any other Redis command, so to discuss latency of such commands is meaningless: it is more interesting to check the time complexity of the commands in the Redis documentation. It should be enough to say that stream commands are at least as fast as sorted set commands when extracting ranges, and that [`XADD`](https://redis.io/docs/latest/commands/xadd) is very fast and can easily insert from half a million to one million items per second in an average machine if pipelining is used.

However latency becomes an interesting parameter if we want to understand the delay of processing a message, in the context of blocking consumers in a consumer group, from the moment the message is produced via [`XADD`](https://redis.io/docs/latest/commands/xadd), to the moment the message is obtained by the consumer because [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) returned with the message.

## How serving blocked consumers works

Before providing the results of performed tests, it is interesting to understand what model Redis uses in order to route stream messages (and in general actually how any blocking operation waiting for data is managed).

* The blocked client is referenced in a hash table that maps keys for which there is at least one blocking consumer, to a list of consumers that are waiting for such key. This way, given a key that received data, we can resolve all the clients that are waiting for such data.
* When a write happens, in this case when the [`XADD`](https://redis.io/docs/latest/commands/xadd) command is called, it calls the `signalKeyAsReady()` function. This function will put the key into a list of keys that need to be processed, because such keys may have new data for blocked consumers. Note that such *ready keys* will be processed later, so in the course of the same event loop cycle, it is possible that the key will receive other writes.
* Finally, before returning into the event loop, the *ready keys* are finally processed. For each key the list of clients waiting for data is scanned, and if applicable, such clients will receive the new data that arrived. In the case of streams the data is the messages in the applicable range requested by the consumer.

As you can see, basically, before returning to the event loop both the client calling [`XADD`](https://redis.io/docs/latest/commands/xadd) and the clients blocked to consume messages, will have their reply in the output buffers, so the caller of [`XADD`](https://redis.io/docs/latest/commands/xadd) should receive the reply from Redis at about the same time the consumers will receive the new messages.

This model is *push-based*, since adding data to the consumers buffers will be performed directly by the action of calling [`XADD`](https://redis.io/docs/latest/commands/xadd), so the latency tends to be quite predictable.

## Latency tests results

In order to check these latency characteristics a test was performed using multiple instances of Ruby programs pushing messages having as an additional field the computer millisecond time, and Ruby programs reading the messages from the consumer group and processing them. The message processing step consisted of comparing the current computer time with the message timestamp, in order to understand the total latency.

Results obtained:

```
Processed between 0 and 1 ms -> 74.11%
Processed between 1 and 2 ms -> 25.80%
Processed between 2 and 3 ms -> 0.06%
Processed between 3 and 4 ms -> 0.01%
Processed between 4 and 5 ms -> 0.02%
```

So 99.9% of requests have a latency <= 2 milliseconds, with the outliers that remain still very close to the average.

Adding a few million unacknowledged messages to the stream does not change the gist of the benchmark, with most queries still processed with very short latency.

A few remarks:

* Here we processed up to 10k messages per iteration, this means that the `COUNT` parameter of [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) was set to 10000. This adds a lot of latency but is needed in order to allow the slow consumers to be able to keep with the message flow. So you can expect a real world latency that is a lot smaller.
* The system used for this benchmark is very slow compared to today's standards.

## Learn more

* [Redis Streams Explained](https://www.youtube.com/watch?v=Z8qcpXyMAiA) is an entertaining introduction to streams in Redis.
* [Redis University's RU202](https://university.redis.com/courses/ru202/) is a free, online course dedicated to Redis Streams.

