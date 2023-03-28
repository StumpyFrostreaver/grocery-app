from src.job.job_reader import JobReader
from src.job.job_runner import JobRunner

job_reader = JobReader()
job_reader.with_file("../csv_files/mark/jobs.csv")
jobs = job_reader.read_jobs()

job_runner = JobRunner()
job_runner.with_output_folder("../csv_files/mark/")

for job in jobs:
    job_runner.run_job(job)

