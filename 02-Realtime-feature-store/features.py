from datetime import timedelta
from feast import Entity, Field, FeatureView, FileSource
from feast.types import Int64, Float32

# Define user entity
user_entity = Entity(name="user_id", join_keys=["user_id"])

# Define offline data source
user_source = FileSource(
    name="user_stats_source",
    path="data/user_stats.parquet",
    timestamp_field="event_timestamp",
)

# Define feature view for point-in-time correctness
user_feature_view = FeatureView(
    name="user_stats_view",
    entities=[user_entity],
    ttl=timedelta(days=365),
    schema=[
        Field(name="transaction_count", dtype=Int64),
        Field(name="avg_spend", dtype=Float32),
    ],
    online=True,
    source=user_source,
)
