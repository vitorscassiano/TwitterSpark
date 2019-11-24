import fixpath

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

conf = SparkConf().setAppName("Twitter Application").setMaster("local")
spark_context = SparkContext(conf=conf)

text_file = spark_context.textFile("breweries_us.csv")

counts = (
  text_file
    .flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a,b: a + b)
)

counts.saveAsTextFile("/tmp/counts")