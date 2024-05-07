# -*- coding: utf-8 -*-
import shutil
import os
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.Config import Config as cfg
from src.data.remove_dublicate import DuplicateRemover

@click.command()
@click.argument('input_folderpath', type=click.Path(exists=True))
@click.argument('output_folderpath', type=click.Path())
def main(input_folderpath, output_folderpath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    # Initialize logger
    logger = logging.getLogger(__name__)
    logger.info('Starting data processing...')

    try:
        # copy data to processed directory
        copyDataFolders(input_folderpath, output_folderpath)
        dr = DuplicateRemover(cfg.PROJECT_DIR, cfg.CLASSES)
        hash_dict = dr.list_files()
        dr.remove_duplicates(hash_dict)
            
        logger.info('Data processing completed successfully.')
    except Exception as e:
        logger.error(f'An error occurred during data processing: {str(e)}')
    

def copyDataFolders(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Copy each file from the source directory to the destination directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        # Check if it's a file and not a directory
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_file)
        elif os.path.isdir(source_file):
            shutil.copytree(source_file, destination_file, dirs_exist_ok=True)

    print('Copied')



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
