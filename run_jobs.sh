#!/bin/bash
#SBATCH --job-name=transfer_sims  
#SBATCH --time=4-00:00:00   
#SBATCH --nodes=4 
#SBATCH --cpus-per-task=16
#SBATCH --ntasks-per-node=1
#SBATCH --mem=64000
#SBATCH --output=random_transfers.%j.out   ## current_director.%j.out
#SBATCH --error=random_transfers.%j.err
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jgibso04@tufts.edu   

module load anaconda/2021.05

source activate /cluster/tufts/mggg/jgibso04/condaenv/votes 

python3 experiments.py 10000 2003-2017 

conda deactivate