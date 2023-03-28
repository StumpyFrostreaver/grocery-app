from src.common import reader_types
from src.job.job import Job
from src.job.job_runner import JobRunner

job_runner = JobRunner()

# job = Job.create_job(reader_types.NO_FRILLS, "https://www.nofrills.ca/search?search-bar=coffee%20food")
# job_runner.run_job(job)
# job_runner.dump_to_csv("../csv_files/mark/nofrills_coffee.csv")

# job = Job.create_job(reader_types.METRO, "https://www.metro.ca/en/online-grocery/search?filter=coffee&freeText=true")
# job_runner.run_job(job)
# job_runner.dump_to_csv("../csv_files/mark/metro_coffee.csv")
# blah
job = Job.create_job(reader_types.VOILA, "https://voila.ca/products/search?q=coffee")
job_runner.run_job(job)
job_runner.dump_to_csv("../csv_files/mark/voila_coffee.csv")

