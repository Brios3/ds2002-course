#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --partition=standard
#SBATCH --job-name=lolcow_jokes
#SBATCH --output=jokes_%j.out
#SBATCH --error=jokes_%j.err
#SBATCH --time=00:01:00
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=0-9

module load apptainer

apptainer run ~/lolcow-latest.sif
