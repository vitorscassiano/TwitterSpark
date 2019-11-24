import fixpath

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext 
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

from src.models.Tweet import Tweet

conf = SparkConf().setAppName("Twitter Application").setMaster("local")
spark_context = SparkContext(conf=conf)
spark_streaming_context = StreamingContext(spark_context, 20)
spark_streaming_context.checkpoint("checkpoint_TwitterApp")

spark_sql_context = SQLContext(spark_context)

socket_stream = spark_streaming_context.socketTextStream("127.0.0.1", 5555)

lines = socket_stream.window(20)

(
  lines
    .flatMap(lambda text: text.split(" "))
    .filter(lambda word: word.lower().startswith("#"))
    .map(lambda word: (word.lower(), 1))
    .reduceByKey(lambda prev, curr: prev + curr)
    .map(lambda rec: Tweet(rec[0], rec[1]))
    .foreachRDD(lambda rdd: rdd.toDF().sort( desc("count") )
      .limit(10)
      .registerTempTable("tweets")
    )
)


spark_streaming_context.start()