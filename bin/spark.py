import fixpath

from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Twitter Application").setMaster("local"

spark_context = SparkContext(conf=conf)
text_file = spark_context.textFile("/tmp/breweries_us.csv")

counts = text_file \
    .flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a,b: a + b)

counts.saveAsTextFile("/tmp/processedFile.txt")