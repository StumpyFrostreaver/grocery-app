import csv

from src.common.string_utils import StringUtils

from src.job.job import Job

class JobReader:
    def __init__(self):
        self.__file = None

    def with_file(self, file):
        self.__file = file

    def read_jobs(self):
        jobs = []
        if StringUtils.is_blank(self.__file):
            print("You must enter the input file to read in the jobs from.")
        else:
            try:
                with open(self.__file) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                    job_count = 0
                    for row in csv_reader:
                        reader_type = StringUtils.decsvify_field(row[0])
                        product_type = StringUtils.decsvify_field(row[1])
                        url = StringUtils.decsvify_field(row[2])

                        # Let's skip the header row if it's there...
                        if reader_type != "reader_type":
                            job_count += 1
                            job = Job.create_job(reader_type, product_type, url)
                            jobs.append(job)

                    print(f"Read in {job_count} jobs.")
            except FileNotFoundError:
                print(f"ERROR: Could not find the file: '{self.__file}'")

        return jobs
