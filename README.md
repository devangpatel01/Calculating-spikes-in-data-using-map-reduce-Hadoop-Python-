## Spike identification in given weblog dataset which represents a website a random user has visited, his start date time and his end date time.
## Calculating total annual sales per department across all stores in salesdata dataset which is weekly sales data of a company which has several stores and each store has several departments.

**Commands** for running various map-reduce jobs are as follows:

**Job 1:**

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator="\t" -D stream.num.map.output.key.fields=2 -D mapreduce.partition.keypartitioner.options=-k1,2 -files salesdata/mapper.py,salesdata/reducer.py -input salesdata/salesdata.tsv -output task1final_output -mapper mapper.py -reducer reducer.py


**Job 2.1**

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator="\t" -D stream.num.map.output.key.fields=2 -D mapreduce.partition.keypartitioner.options=-k1,2 -files weblog/mapper1.py,weblog/reducer1.py -input weblog/weblog.tsv -output task2.1output -mapper mapper1.py -reducer reducer1.py

**Job 2.2**

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator="\t" -D stream.num.map.output.key.fields=2 -D mapreduce.partition.keypartitioner.options=-k1,2 -files weblog/mapper2.py,weblog/reducer2.py -input task2.1output/part-00000  -output task2.2output -mapper mapper2.py -reducer reducer2.py

**Job 2.3**

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator="\t" -D stream.num.map.output.key.fields=1 -D mapreduce.partition.keypartitioner.options=-k1,1 -files weblog/mapper3.py,weblog/reducer3.py -input task2.2output/part-00000  -output task2.3output -mapper mapper3.py -reducer reducer3.py

