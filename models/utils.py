from typing import List
from dataclasses import dataclass
from os.path import exists, curdir, join, abspath, splitext, basename, dirname
import os
import subprocess
from sspipe import p
import glob
from zipfile import ZipFile


@dataclass
class KaggleData:
    name: str
    competition: str
    source_filename: str
    destination_dir: str

    def cli_download_command(self) -> List[str]:
        return [
            "kaggle",
            "competitions",
            "download",
            self.competition,
            "--file",
            self.source_filename,
            "--path",
            self.destination_dir,
        ]

    def get_path(self):
        return join(self.destination_dir, self.source_filename.split("/")[-1])


    
def download_data(directory):
    
    if dirname(directory) != 'data':
        directory = join(directory, 'data')
    
    if not exists(directory):
        print(f'{directory} not found. Creating..')
        os.makedirs(directory)
    
    datasets = [
        KaggleData(
            name="aisles",
            competition="instacart-market-basket-analysis",
            source_filename="aisles.csv.zip",
            destination_dir=directory,
        ),
        KaggleData(
            name="orders",
            competition="instacart-market-basket-analysis",
            source_filename="orders.csv.zip",
            destination_dir=directory,
        ),
        KaggleData(
            name="departments",
            competition="instacart-market-basket-analysis",
            source_filename="departments.csv.zip",
            destination_dir=directory,
        ),
        KaggleData(
            name="products",
            competition="instacart-market-basket-analysis",
            source_filename="products.csv.zip",
            destination_dir=directory,
        ),
        KaggleData(
            name="order-products-train",
            competition="instacart-market-basket-analysis",
            source_filename="order_products__train.csv.zip",
            destination_dir=directory,
        ),
        KaggleData(
            name="order-products-prior",
            competition="instacart-market-basket-analysis",
            source_filename="order_products__prior.csv.zip",
            destination_dir=directory,
        ),
        KaggleData(
            name="sample-submission",
            competition="instacart-market-basket-analysis",
            source_filename="sample_submission.csv.zip",
            destination_dir=directory,
        ),
    ]
    
    for source in datasets:
        dest = join(source.destination_dir, source.source_filename)
        if (not dest | p(exists)) and (not splitext(dest)[0] | p(exists)):
            subprocess.run(source.cli_download_command())
        else:
            # To do log warning (do not print)
            pass

    unzip_files(directory)
    
    results = {}
    
    for d in datasets:
        path = d.get_path()
        
        if splitext(path)[1] == '.zip':
            path = splitext(path)[0]
            
        results[d.name] = path
        
    return results


def unzip_files(source_dir):
    files = glob.glob(join(source_dir, "*.zip"))
    
    for f in files:
        filepath = os.path.splitext(f)[0]  # unzipped path
        
        if not exists(filepath):
            file = filepath | p(basename)
            path = filepath | p(dirname)

            ZipFile(f).extract(member=file, path=path)
        
        if exists(f):
            os.remove(f)
            