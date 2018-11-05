from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper =self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
        ]

    def mapper_get_ratings(self,_,line):
        (user_id,movie_id,ratings,timestamp) = line.split('\t')
        yield ratings,1

    def reducer_count_ratings(self,key,values):
        yield key,sum(values)

if __name__ == '__main__':
    RatingsBreakdown.run()